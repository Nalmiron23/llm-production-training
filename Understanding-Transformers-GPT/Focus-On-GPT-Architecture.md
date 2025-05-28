## Focus on the GPT Architecture

### Introduction

The Generative Pre-trained Transformer (GPT) is a type of transformer-based language model developed by OpenAI. The 'transformer' part of its name refers to its transformer architecture, which was introduced in the research paper "Attention is All You Need" by Vaswani et al.

In contrast to conventional Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) networks, the transformer architecture departs from recurrence and adopts self-attention mechanisms, resulting in substantial advancements in speed and scalability. An immensely powerful architecture was unleashed by harnessing the potential for parallelization within the network (simultaneously running multiple head attentions) along with the abundant small cores available in a GPU.

### The GPT Architecture

The GPT family comprises decoder-only models, wherein each block in the stack is comprised of a self-attention mechanism and a position-wise fully connected feed-forward network.

The self-attention mechanism, also known as scaled dot-product attention, allows the model to weigh the importance of each word in the input when generating the next word in the sequence. It computes a weighted sum of all the words in the sequence, where the weights are determined by the attention scores.

A critical aspect to focus on is the addition of "masking" to the self-attention that prevents the model from attending to certain positions/words.

#### Masked Self-Attention

Illustrating which tokens are attended to by masked self-attention at a particular timestamp: we pass the whole sequence to the model, but at timestep 5, the model tries to predict the next token by only looking at the previously generated tokens, masking the future tokens. This prevents the model from "cheating" by using future tokens.

```python
import numpy as np

def self_attention(query, key, value, mask=None):
    # Compute attention scores
    scores = np.dot(query, key.T)

    if mask is not None:
        # Apply mask by setting masked positions to a large negative value
        scores = scores + mask * -1e9

    # Apply softmax to obtain attention weights
    attention_weights = np.exp(scores) / np.sum(np.exp(scores), axis=-1, keepdims=True)

    # Compute weighted sum of value vectors
    output = np.dot(attention_weights, value)

    return output
```

This function showcases how to implement masked self-attention by applying a mask and computing softmax-based weights.

The first step is to compute a Query, Key, and Value vector for each word in the input sequence using separate learned linear transformations of the input vector. It is a simple feedforward linear layer that the model learns during training.

Then, we can calculate the attention scores by taking the dot product of its Query vector with the Key vector of every other word. Currently, the application of masking is feasible by setting the scores in specific locations to a large negative number. This effectively informs the model that those words are unimportant and should be disregarded during attention. To get the attention weights, apply the SoftMax function to the attention scores to convert them into probabilities. This gives the weights of the input words and effectively turns the significant negative scores to zero. Lastly, multiply each Value vector by its corresponding weight and sum them up. This produces the output of the masked self-attention mechanism for the word.

The provided code snippet illustrates the process of a single self-attention head, but in reality, each layer contains multiple heads, which could range from 16 to 32 heads, depending on the architecture. These heads operate simultaneously to enhance the model's performance.

### Causal Language Modeling

LLMs utilize a self-supervised learning process for pre-training. This process eliminates the need to provide explicit labels to the model for learning, making it capable of acquiring knowledge autonomously.For instance, when training a summarization model using supervised learning, it is necessary to provide articles and their corresponding summaries as reference points during the training process. However, LLMs employ the causal language modeling objective to acquire knowledge from any textual data without the explicit need for human-provided labels. Why is it called “causal”? Because the prediction at each step depends only on earlier steps in the sequence and not on future steps.

This process involves feeding a segment of the document to the model and asking it to predict the next word. The predicted word is then concatenated to the original input and fed back into the model. This loop continues, enabling the model to learn language and grammar.

Causal language modeling is distinct because prediction at each step depends only on earlier steps and not future ones. This method aligns closely with how humans write or speak.

Moreover, this method allows the use of extensive human-generated text from books, Wikipedia, and other sources, all available through datasets from Hugging Face or ActiveLoop.

### MinGPT

Numerous implementations of GPT exist, but "minGPT" by Andrej Karpathy offers a lightweight educational version. It's a simplified GPT-2 implementation written in PyTorch and condensed to about 300 lines of code.

It includes:

* `model.py` for architecture definition
* `bpe.py` for Byte Pair Encoding tokenization
* `train.py` for training loop logic
* `demo.ipynb` for an executable notebook showcasing inference

This implementation runs on modest hardware like a MacBook Air or Colab.

### Conclusion

The decoder-only architecture and GPT-family models have driven the recent advancements in large language models. It is essential to possess a strong grasp of the transformer architecture and comprehend the distinctive features that set the decoder-only models apart, making them well-suited for language modeling. 