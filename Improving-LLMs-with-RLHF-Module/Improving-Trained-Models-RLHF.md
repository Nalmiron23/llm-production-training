# Improving Trained Models with RLHF

## Introduction

As previously stated, the RLHF process involves incorporating human feedback into the training process through a reward model that learns the desired patterns to amplify the model’s output. For instance, if the goal is to enhance politeness, the reward model will guide the model to generate more polite responses by assigning higher scores to polite outputs. This process can be resource-intensive due to the need to train an additional reward model using a dataset curated by humans, which can be costly. Nevertheless, we will leverage available open-source models and datasets whenever feasible to explore the technique thoroughly while maintaining acceptable costs.

It is recommended to begin the procedure by conducting a supervised fine-tuning phase, which enables the model to adjust to a conversational manner. This procedure can be accomplished by using the `SFTTrainer` class. The next phase involves training a reward model with the desired traits using the `RewardTrainer` class. Finally, the Reinforcement Learning phase employs the models from the preceding steps to construct the ultimate aligned model, utilizing the `PPOTrainer` class.

After each subsection, the fine-tuned models, the reports generated from the weights and biases, and the file detailing the requirements for the library can be accessed. Note that different steps might necessitate distinct versions of libraries. We employed the OPT-1.3B model as the foundational model and fine-tuned the DeBERTa (300M) model as the reward model for our experiments. While these are more compact models and might not incorporate the insights of recent larger models like GPT-4 and LLaMA2, the procedure we are exploring in this tutorial can be readily applied to other existing networks by simply modifying the model key name in the code.

We’ll be using a set of 8x100 A100 GPUs in this lesson.

## GPU Cloud - Lambda

In this lesson, we’ll leverage **Lambda**, a GPU cloud designed by ML engineers for training LLMs & Generative AI. For this lesson, we rented an 8x NVIDIA A100 instance comprising 40GB of memory at the price of \$8.80/h.

> ⚠️ Beware of costs when you borrow cloud GPUs. The total cost will depend on the machine type and the uptime of the instance. Always monitor your costs in Lambda Labs and stop your instances when not in use.

> 💡 Tip: Run just a few training iterations to minimize cost if you're replicating this lesson.

## Training Monitoring - Weights and Biases

To ensure everything is progressing smoothly, we’ll log the training metrics to **Weights & Biases**, allowing us to see the metrics in real-time.

---

The complete lesson continues with structured code samples that I have run and modified across diferents projects and requierements but that I won't add here since it becomes too long.

* Supervised Fine-Tuning (SFT)

  * Dataset: OpenOrca
  * LoRA + QLoRA quantization
  * Training pipeline with HuggingFace and `SFTTrainer`
* Reward Model Training

  * Dataset: Anthropic Helpful/Harmless (hh)
  * Model: DeBERTa-v3
  * `RewardTrainer` from TRL
* Reinforcement Learning (PPO)

  * PPO fine-tuning using reward scores
  * Dataset: Alpaca-OrcaChat
  * Model: OPT-1.3B + Value Head
  * `PPOTrainer` implementation
* Final model merge & evaluation
* Inference and practical usage
* QLoRA deep-dive

Each stage includes instructions, example code, and explanations to help replicate the workflow.

---

## Conclusion

This lesson experimented with the three essential RLHF stages:

1. **Supervised Fine-Tuning**
2. **Reward Model Training**
3. **Reinforcement Learning (PPO)**

We employed techniques like LoRA, QLoRA, and BitsAndBytes quantization to optimize training efficiency. While the models used are relatively small, the same methodology can be applied to larger models like LLaMA2 or GPT-style networks by updating the model keys.

In the next chapter, we will introduce **deployment procedures** for putting fine-tuned models into **production environments**.
