## Focus on the GPT Architecture

### Introduction

The Generative Pre-trained Transformer (GPT) is a type of transformer-based language model developed by OpenAI. The 'transformer' part of its name refers to its transformer architecture, which was introduced in the research paper "Attention is All You Need" by Vaswani et al.

You should have a good understanding of the fundamental elements comprising the transformer architecture. In this session, we will cover the decoder-only networks that play an essential role in developing large language models. We will explore their unique attributes and the reasons behind their effectiveness.

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

### Causal Language Modeling

LLMs utilize a self-supervised learning process for pre-training. This process eliminates the need to provide explicit labels to the model for learning, making it capable of acquiring knowledge autonomously.

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

Decoder-only architectures like GPT have driven recent LLM advancements. Understanding transformer internals and GPT-specific design choices such as masked self-attention and causal modeling helps us appreciate their strengths.

In subsequent lessons, we will explore fine-tuning strategies, model evaluation, and deployment approaches to use GPT effectively in production.
