When to Train an LLM from Scratch

## Introduction

The increasing popularity of LLMs has led businesses to integrate them for task handling and employee productivity enhancement.

There are several ways to use LLMs in daily activities, such as incorporating proprietary models via APIs, deploying pre-trained open-source options, or developing one's own language model. Of course, the trade-offs are between quality, costs, and ease of use.

In this lesson, we will discuss different approaches and what might be the best solution for your use case.

---

## Few-Shot (In-Context) Learning

Up to 2020, language models were already good at picking up patterns from the data. However, teaching them new knowledge from a different domain was difficult. The only solution was to finetune them by adjusting the weights.

### What makes LLMs different?

Few-shot learning (also called In-Context learning) enables the LLMs to learn from the examples provided to them. For instance, it is possible to show a couple of examples of JSON-formatted responses to receive the model’s output in JSON format. It means that the models can learn from examples and follow directions without changing weights or repeating the training process.

There are multiple use cases where this approach could be the best option. The model can adapt to a writing style, set specific formatting guidelines, or provide additional context for answering questions.

LLMs are able to answer questions using external knowledge bases through in-context learning. Let’s think about how we could create a Q\&A chatbot leveraging an LLM. The LLM has a cut-off training date, so it can’t access the information or events after that date. Also, they tend to hallucinate, which refers to generating non-factual responses based on their limited knowledge.

As a solution, it is possible to provide additional context to the LLM through the Internet (e.g., Google search) or retrieve it from a database and include it in the prompt so that the model can leverage it to generate the correct response. It is like taking an open-book exam!

The beauty of this approach is that the model does not need domain-specific knowledge. Instead, it can extract information or patterns from the provided context. Creating applications, such as chatbots, becomes more accessible and faster. Whether you are utilizing proprietary APIs or open-source models, this approach offers a budget-friendly solution for many use cases.

---

## Fine-Tuning

The fine-tuning method proves valuable when adapting the model to a more complex use case. This technique can improve model understanding by providing more examples and adjusting weights based on errors, for tasks like classification or summarization.

There are different approaches to doing this. We could either adjust the weights with a small learning rate to minimally affect the model’s current abilities, or a more recent technique is to freeze the network and introduce new weights for fine-tuning. The latter approach (like LoRA) is a great alternative for fine-tuning models with hundreds of billions of parameters since we will deal with a much smaller number of parameters. (\~100x less)

The fine-tuning approach is an excellent option for creating a model with task-specific knowledge and building on top of the available powerful LLMs. However, before considering this option, it is essential to acknowledge the associated costs and required resource implications.

---

## Training

Lastly, let's talk about training your own model from scratch!

Among the approaches mentioned earlier, this option stands out as the most demanding and challenging. Of course, the scale of requirements depends on the model size. However, acquiring several millions of data points, such as web pages, books, and articles, not to mention the task-specific documents held by your organization (if you want to train a domain-specific LLM), is essential. Furthermore, completing the training process could cost upward of several hundreds of thousands of dollars. The training costs of these models are rarely revealed by the organizations that publish them. Nevertheless, considering the hardware utilized, speculations have estimated the training expenses for the GPT-3 model to be approximately \$4.6 million.

However, the more critical aspect of training from scratch is curating the dataset. While the intention is to train a domain-specific model, the training loop that processes vast quantities of general documents, such as web pages, articles, and books, empowers LLMs' language understanding capabilities. Therefore, to create a model that excels in a specific domain, it is essential to have a sizable dataset comprising top-quality samples from that particular domain.

An example of this approach is the BloombergGPT 50B model, which is specifically designed for the finance industry. They used a dataset of 708 billion tokens for training, consisting of 51.2% (363 billion tokens) domain-specific resources and the rest general resources.

Training a model from scratch demands substantial resources, including hardware and dataset resources, and expertise within the organization to train and maintain these models.

---

## Main Takeaways

* **Few-Shot Learning:** The LLMs are able to learn from the examples given to them, allowing them to handle more complicated tasks without the need for training or fine-tuning. This method is significantly less expensive than other options, as it only requires the cost of adding examples to each prompt. If your task can be solved just with few-shot learning, then it’s always the most efficient approach.

* **Fine-Tuning:** If few-shot learning is not effective for your task, an alternative method is fine-tuning. This involves using some data points to create a task-specific model. Although finetuning can be challenging when acquiring new knowledge, it is more effective in adapting to different styles, and tones, or incorporating new vocabulary.

* **Training From Scratch:** If fine-tuning is not effective, consider training a model from scratch with domain-specific data. However, this requires significant resources, such as cost, dataset availability, and expertise.

---
