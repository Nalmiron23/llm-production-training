# Prompting and Few-Shot Prompting

## Introduction

In this lesson, we explore prompting and prompt engineering—techniques that enable effective interaction with Large Language Models (LLMs). Prompting can help LLMs perform tasks like answering questions, generating content, or reasoning through problems by crafting targeted instructions.

We’ll cover:

* Zero-shot prompting
* In-context learning
* Few-shot prompting

---

## Prompting and Prompt Engineering

Prompting involves crafting inputs that guide the model to produce the desired output. These can be simple instructions or include examples and context.

Prompt engineering is the optimization of those inputs to improve performance for specific applications such as:

* Text generation
* Question answering
* Reasoning tasks

### Best Practice:

The **clarity, structure, and context** of a prompt significantly affect the quality of the model’s response.

---

## Setup: Load Environment Variables

```python
from dotenv import load_dotenv
load_dotenv()
```

---

## Example: Story Generation
In this example, the prompt sets up the start of a story, providing initial context ("a world where animals could speak") and a character ("a courageous mouse named Benjamin"). The model's task is to generate the rest of the story based on this prompt.

Note that in this example we are defining separately a prompt_system and a prompt. This is because the OpenAI API works this way, requiring a “system prompt” to steer the model behaviour. This is different from other LLMs that require only a standard prompt.

```python
from openai import OpenAI
client = OpenAI()

prompt_system = "You are a helpful assistant whose goal is to help write stories."

prompt = """Continue the following story. Write no more than 50 words.

Once upon a time, in a world where animals could speak, a courageous mouse named Benjamin decided to"""

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": prompt_system},
    {"role": "user", "content": prompt},
  ]
)

print(response.choices[0]['message']['content'])
```

---

## Example: Product Description
Here, the prompt is a request for a product description with key details ("luxurious, hand-crafted, limited-edition fountain pen made from rosewood and gold"). The model is tasked with writing an appealing product description based on these details.

```python
prompt_system = "You are a helpful assistant whose goal is to help write product descriptions."

prompt = """Write a captivating product description for a luxurious, hand-crafted, limited-edition fountain pen made from rosewood and gold.
Write no more than 50 words."""

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": prompt_system},
    {"role": "user", "content": prompt},
  ]
)

print(response.choices[0]['message']['content'])
```

---

## Zero-Shot Prompting

In the context of prompting, **“zero-shot prompting”** is where we directly ask for the result without providing reference examples for the task. For many tasks, LLMs are smart enough to produce great results. This is exactly what we did in the examples above. Here’s a new example where we ask an LLM to write a short poem about summer.

### Example: Poem Generation

```python
prompt_system = "You are a helpful assistant whose goal is to write short poems."

prompt = """Write a short poem about {topic}."""

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": prompt_system},
    {"role": "user", "content": prompt.format(topic="summer")},
  ]
)

print(response.choices[0]['message']['content'])
```

---

##  In-Context Learning & Few-Shot Prompting

In the context of LLMs, **in-context learning** is a powerful approach where the model learns from demonstrations or exemplars provided within the prompt. **Few-shot prompting** is a technique under in-context learning that involves giving the language model a few examples or demonstrations of the task at hand to help it generalize and perform better on complex tasks.

Few-shot prompting allows language models to learn from a limited amount of data, making them more adaptable and capable of handling tasks with minimal training samples. Instead of relying solely on zero-shot capabilities (where the model predicts outputs for tasks it has never seen before), few-shot prompting leverages the in-context demonstrations to improve performance.

In few-shot prompting, the prompt typically includes multiple questions or inputs along with their corresponding answers. The language model learns from these examples and generalizes to respond to similar queries.

### Example: Few-Shot Poem Generation

```python
prompt_system = "You are a helpful assistant whose goal is to write short poems."

prompt = "Write a short poem about {topic}."

examples = {
    "nature": "Birdsong fills the air,\nMountains high and valleys deep,\nNature's music sweet.",
    "winter": "Snow blankets the ground,\nSilence is the only sound,\nWinter's beauty found."
}

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": prompt_system},
        {"role": "user", "content": prompt.format(topic="nature")},
        {"role": "assistant", "content": examples["nature"]},
        {"role": "user", "content": prompt.format(topic="winter")},
        {"role": "assistant", "content": examples["winter"]},
        {"role": "user", "content": prompt.format(topic="summer")}
    ]
)

print(response.choices[0].message.content)
```

---

## Limitations of Few-Shot Prompting

While effective, few-shot prompting may fall short on **complex reasoning tasks**. In such cases, **Chain-of-Thought (CoT) prompting** can help by guiding the model to reason step-by-step through examples.

---

## Conclusion

* **Prompting** is how we communicate tasks to LLMs.
* **Zero-shot prompting** is quick and simple, but may lack specificity.
* **Few-shot prompting** improves output quality by showing examples.
* Advanced strategies like **Chain-of-Thought** can handle complex reasoning.
