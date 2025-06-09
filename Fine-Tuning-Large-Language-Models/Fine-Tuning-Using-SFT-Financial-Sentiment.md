# Fine-Tuning using SFT for Financial Sentiment

## Introduction

In the previous lesson, we experimented with fine-tuning an LLM to follow instructions like a chatbot. This lesson expands that idea into a **domain-specific task**—performing sentiment analysis on financial tweets using **Supervised Fine-Tuning (SFT)**.

The goal: Fine-tune an LLM to classify tweets as **Positive, Negative, or Neutral**, using the FinGPT project's dataset. While we’ve already covered the core mechanics of SFT, this lesson emphasizes dataset usage and preprocessing. A full notebook script is provided at the end.

This tutorial runs on **4th Gen Intel® Xeon® Scalable Processors** (64GB RAM) using **Intel® AMX** optimization. You can spin up a GCP Compute Engine VM as described in previous lessons.

> ⚠️ Be cautious of costs when running VMs. Always stop them when not in use.

> 💡 Tip: Run a few training steps to test without incurring high costs.

---

## Load the Dataset

We use the **FinGPT sentiment dataset**, consisting of financial tweets, labels, and an instruction column.

```python
pip install deeplake==3.9.27

import deeplake

ds = deeplake.load('hub://genai360/FingGPT-sentiment-train-set')
ds_valid = deeplake.load('hub://genai360/FingGPT-sentiment-valid-set')

print(ds)

The output:
Dataset(path='hub://genai360/FingGPT-sentiment-train-set', read_only=True, tensors=['input', 'instruction', 'output'])

Prepare Samples
def prepare_sample_text(example):
    text = f"{example['instruction'].text()}\n\nContent: {example['input'].text()}\n\nSentiment: {example['output'].text()}"
    return text

Tokenization and Dataset Preparation
from transformers import AutoTokenizer
from trl.trainer import ConstantLengthDataset

tokenizer = AutoTokenizer.from_pretrained("facebook/opt-1.3b")

train_dataset = ConstantLengthDataset(
    tokenizer, ds, formatting_func=prepare_sample_text,
    infinite=True, seq_length=1024
)

eval_dataset = ConstantLengthDataset(
    tokenizer, ds_valid, formatting_func=prepare_sample_text,
    seq_length=1024
)

# Example sample
iterator = iter(train_dataset)
sample = next(iterator)
print(sample)

train_dataset.start_iteration = 0  # Reset if reusing iterator

Initialize the Model and Trainer
Configure LoRA and TrainingArguments

from peft import LoraConfig
from transformers import TrainingArguments

lora_config = LoraConfig(
    r=16, lora_alpha=32, lora_dropout=0.05,
    bias="none", task_type="CAUSAL_LM"
)

training_args = TrainingArguments(
    output_dir="./OPT-fine_tuned-FinGPT-CPU",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    num_train_epochs=10,
    logging_steps=5,
    per_device_train_batch_size=12,
    per_device_eval_batch_size=12,
    learning_rate=1e-4,
    lr_scheduler_type="cosine",
    warmup_steps=100,
    bf16=True,
    weight_decay=0.05,
    run_name="OPT-fine_tuned-FinGPT-CPU",
    report_to="wandb"
)

Load and Prepare Model
from transformers import AutoModelForCausalLM
import torch

model = AutoModelForCausalLM.from_pretrained(
    "facebook/opt-1.3b", torch_dtype=torch.bfloat16
)

from torch import nn
for param in model.parameters():
    param.requires_grad = False
    if param.ndim == 1:
        param.data = param.data.to(torch.float32)

model.gradient_checkpointing_enable()
model.enable_input_require_grads()

class CastOutputToFloat(nn.Sequential):
    def forward(self, x): return super().forward(x).to(torch.float32)

model.lm_head = CastOutputToFloat(model.lm_head)

Start Training
from trl import SFTTrainer

trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    peft_config=lora_config,
    packing=True,
)

trainer.train()

Merging LoRA and OPT
from transformers import AutoModelForCausalLM
from peft import PeftModel

model = AutoModelForCausalLM.from_pretrained(
    "facebook/opt-1.3b", return_dict=True, torch_dtype=torch.bfloat16
)

model = PeftModel.from_pretrained(model, "./OPT-fine_tuned-FinGPT-CPU/<desired_checkpoint>/")
model.eval()
model = model.merge_and_unload()

model.save_pretrained("./OPT-fine_tuned-FinGPT-CPU/merged")


Inference
inputs = tokenizer("""What is the sentiment of this news? Please choose an answer from {strong negative/moderately negative/mildly negative/neutral/mildly positive/moderately positive/strong positive}, then provide some short reasons.

Content: UPDATE 1-AstraZeneca sells rare cancer drug to Sanofi for up to S300 mln.

Sentiment: """, return_tensors="pt").to("cuda:0")

generation_output = model.generate(
    **inputs,
    return_dict_in_generate=True,
    output_scores=True,
    max_length=256,
    num_beams=1,
    do_sample=True,
    repetition_penalty=1.5,
    length_penalty=2.
)

print(tokenizer.decode(generation_output['sequences'][0]))

Sample output:
Sentiment: positive


Conclusion
This lesson showed how to:

Fine-tune an LLM for financial sentiment analysis using SFT and LoRA.

Run fine-tuning efficiently on Intel CPUs using bfloat16.

Merge and deploy LoRA adapters for downstream tasks.

Evaluate the effectiveness of fine-tuned vs. base models.

We also highlighted the cost and accessibility of using public datasets with open-source tooling. In the next lesson, we will explore RLHF (Reinforcement Learning from Human Feedback) and GPU-based training.
