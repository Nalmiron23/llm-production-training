# Understanding Transformers

## Introduction

In this lesson, I will dive deeper into Transformers, covering their components, mechanisms, and how they're implemented in Hugging Face's `transformers` library.

I will explore the seminal paper **"Attention Is All You Need"**, examine a diagram of the architecture, and walk through practical examples with Facebook's `OPT` model.

---

## Attention Is All You Need

The Transformer architecture was introduced by researchers at Google Brain and the University of Toronto. It proposed an **encoder-decoder model based on self-attention** for translation tasks, achieving state-of-the-art performance at reduced training cost.

Highlights:

* Outperformed existing benchmarks (e.g., WMT 2014 English-French task).
* Introduced parallelism, making training more efficient.

Transformer models evolved into 3 broad categories:

* **Encoder-only**: For representation learning (e.g., BERT).
* **Encoder-decoder**: For seq2seq tasks (e.g., BART, T5).
* **Decoder-only**: For autoregressive generation (e.g., GPT).

---

## Transformer Architecture Components

### Input Embedding

* Converts input tokens into high-dimensional vectors.
* Size depends on model design (e.g., GPT-3 uses 12,000 dims).

### Positional Encoding

* Adds word order info to embeddings since Transformers lack recurrence.
* Can be sinusoidal or learned (as in OPT).

### Self-Attention Mechanism

* Calculates weighted relevance of all tokens to each token.
* Uses **Query (Q)**, **Key (K)**, and **Value (V)** vectors:

  * **Query**: What this word wants to attend to.
  * **Key**: What each word offers.
  * **Value**: What is returned if attention is paid.

### Multi-Head Attention

* Applies multiple attention mechanisms in parallel.
* Each head captures different semantic features.

---

## The Architecture in Practice

### Loading the Model

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

OPT = AutoModelForCausalLM.from_pretrained("facebook/opt-1.3b", load_in_8bit=True)
tokenizer = AutoTokenizer.from_pretrained("facebook/opt-1.3b")

inp = "The quick brown fox jumps over the lazy dog"
inp_tokenized = tokenizer(inp, return_tensors="pt")
print(inp_tokenized['input_ids'].size())
print(inp_tokenized)
```

### Inspecting Architecture

```python
print(OPT.model)
```

Shows:

* Decoder-only model
* 24 stacked decoder layers
* Self-attention components: `q_proj`, `k_proj`, `v_proj`, `out_proj`

### Embedding Layer

```python
embedded_input = OPT.model.decoder.embed_tokens(inp_tokenized['input_ids'])
print(embedded_input.size())  # Expected: [1, 10, 2048]
```

### Positional Embedding

```python
embed_pos_input = OPT.model.decoder.embed_positions(inp_tokenized['attention_mask'])
print(embed_pos_input.size())  # Expected: [1, 10, 2048]
```

### Self-Attention Output

```python
embed_position_input = embedded_input + embed_pos_input
hidden_states, _, _ = OPT.model.decoder.layers[0].self_attn(embed_position_input)
print(hidden_states.size())  # Expected: [1, 10, 2048]
```

The self-attention module processes the sum of token embeddings and positional encodings to determine contextually relevant information.

---

## Conclusion

The Transformer architecture fundamentally shifted deep learning by enabling parallel training and long-range dependency modeling through self-attention. Understanding each component—from embedding to multi-head attention—offers valuable insight into how LLMs like GPT and BERT operate internally.

Using Hugging Face's `transformers` library allows us to peek into these inner workings and experiment with cutting-edge models like `OPT`, making the learning process hands-on and transparent.
