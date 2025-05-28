# Pretraining and Fine-Tuning of LLMs

## Introduction

This lesson will explore how pretrained LLMs learn from vast amounts of text, becoming great at language tasks. Then, we'll discover the power of finetuning, a process that molds these models into specialized experts, enabling them to tackle complex tasks. We'll also cover instruction finetuning, where we guide the models with explicit instructions, making them versatile and responsive to our needs. This lesson introduces several fine-tuning techniques we will use to finetune models later in the course.

## Pretraining LLMs

Pretrained LLMs have catalyzed a paradigm shift in AI. These models are trained on massive text corpora sourced from the Internet, honing their linguistic knowledge through the prediction of the following words within sentences. By training on billions of sentences, these models acquire an excellent grasp of grammar, context, and semantics, enabling them to capture the nuances of language effectively.

Aside from being good at generating text, pretrained LLMs are also good at other tasks, as was found in 2020 with the GPT3 paper “Language Models are Few-Shot Learners.” The paper showed that big enough LLMs are “few-shot learners”; that is, they are able to perform other tasks aside from text generation with the help of just a few examples of that task (hence the name “few-shot learners”). With those examples, the LLM is able to understand the logic behind what the user wants.

This was a huge step forward in the field, where each NLP task had very different models for each task. Now, a single model can do several of them and do them well.

## The Power of Finetuning

Finetuning complements pretraining for specialized tasks.

While pretrained LLMs are undeniably impressive, their true potential is unlocked through finetuning. Although pretrained models possess a deep understanding of language, they require further adaptation to excel in complex tasks. For example, if the task is to answer questions about medical texts, the model would be finetuned on a dataset of medical question-answer pairs.

Finetuning helps these models become specialized. Finetuning exposes pretrained models to task-specific datasets, enabling them to recalibrate internal parameters and representations to align with the intended task. This adaptation enhances their ability to handle domain-specific challenges effectively.

The necessity for finetuning arises from the inherent non-specificity of pretrained models. While they possess a wide-ranging grasp of language, they lack task-specific context. For instance, finetuning is essential when tackling sentiment analysis of financial news.

In the early days of GPT3 in 2020 and 2021, finetuning also allowed an LLM to be tuned for a specific task without the need for multiple few-shot examples in the prompt.

## Instruction Finetuning: Making General-Purpose Assistants out of LLMs

Instruction finetuning adds precise control over model behavior, making it a general-purpose assistant. The goal of instruction finetuning is to obtain an LLM that interprets prompts as instructions instead of text. It’s just a special type of finetuning.

For example, consider the following prompt:

**What is the capital of France?**

An LLM with instruction finetuning would likely interpret the prompt as an instruction, giving the following answer:

**Paris.**

However, a plain LLM without instruction finetuning could think that we are writing a list of exercises for our geography students, therefore merely continuing the text with a new question:

**What is the capital of Italy?**

Instruction finetuning takes things up a notch. Imagine giving precise instructions to our model: "Analyze the sentiment of this text and tell us if it's positive.” It's like coaching the model to paint exactly what you envision. With instruction finetuning, we provide explicit guidance, shaping the model's behavior to match our intentions.

Instruction tuning offers several advantages. It trains models on a collection of tasks described via instructions, granting LLMs the capacity to generalize to new tasks prompted by additional instructions. This sidesteps the need for vast amounts of task-specific data and instead uses textual instructions to guide learning.

While traditional finetuning acquaints models with task-specific data, instruction finetuning adds an extra layer by incorporating explicit instructions to guide model behavior. This approach empowers developers to shape desired outputs, encourage specific behaviors, and steer model responses.

## Finetuning Techniques

There are several finetuning methods. We’ll learn more about them later in the course.

There are multiple methods in fine-tuning with a focus on the number of parameters, such as:

* **Full Finetuning**: This method is based on adjusting all the parameters in the pretrained LLM models in order to adapt to a specific task. However, this method is relatively resource-intensive, requiring extensive computational power.
* **Low-Rank Adaptation (LoRA)**: LoRA aims to adapt LLMs to specific tasks and datasets while simultaneously reducing computational resources and costs. By applying low-rank approximations to the downstream layers of LLMs, LoRA significantly reduces the number of parameters to be trained, thereby lowering the GPU memory requirements and training costs.

Multiple methods are focusing on the learning algorithm used for finetuning, such as:

* **Supervised Finetuning (SFT)**: SFT involves doing standard supervised finetuning with a pretrained LLM on a small amount of demonstration data.
* **Reinforcement Learning from Human Feedback (RLHF)**: RLHF is a training methodology where models are trained to follow human feedback over multiple iterations.

Later in this course, we’ll see how to finetune a model using SFT and RLHF, both using LoRA.

## Conclusion

In this lesson, we covered the pretraining and finetuning of LLMs. Pretraining equips LLMs with a profound grasp of language by immersing them in vast text corpora.

Finetuning then bridges the gap between general understanding and specialized knowledge, allowing LLMs to perform well in specialized domains. Instruction finetuning makes LLMs become versatile assistants, enabling precise control over their behavior through explicit guidance.

From full finetuning to the resource-efficient Low-Rank Adaptation (LoRA) and from Supervised Finetuning (SFT) to Reinforcement Learning from Human Feedback (RLHF), we also learned about the most popular finetuning techniques.

