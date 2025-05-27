# Controlling LLM Outputs

## Introduction

In this lesson, we explore various methods and parameters for controlling the outputs of Large Language Models (LLMs). We'll discuss different decoding strategies and how specific parameters can be tuned to guide text generation behavior.

---

## Decoding Methods
Decoding methods are fundamental strategies used by LLMs to generate text. Each method has its unique advantages and limitations.

At each decoding step, the LLM gives a score to each of its vocabulary tokens. A high score is related to a high probability of that token being the next token, according to the patterns learned by the model during training.

However, is the token with the highest probability always the best token to predict? By predicting the best token at step 1, the model may then find only tokens with low probabilities at step 2, thus having a low joint probability of the two consecutive tokens. Instead, predicting a slightly lower token at step 1 leads to a high probability token at step 2, thus having an overall higher joint probability of the tokens. Ideally, we’d want to do these computations for all the tokens in the model vocabulary and a large number of steps. However, this can’t be done in practice because it would require heavy computations.

All the decoding methods in this lesson try to find the right balance between:

Being “greedy” and instantly selecting the next token with higher probability.
A bit of exploration and trying to predict more tokens at once.


Then, decoding methods determine how an LLM chooses the next word/token during text generation. These methods aim to balance **accuracy**, **diversity**, and **efficiency**.

### Greedy Search

* Picks the token with the **highest probability** at each step.
* Fast and deterministic.
* Can lead to repetitive or suboptimal outputs.

### Sampling

Sampling introduces randomness into the text generation process, where the model randomly selects the next word based on its probability distribution. This method allows for more diverse and varied output but can sometimes produce less coherent or logical text. 

### Beam Search

Beam Search is a more sophisticated method. It selects the top N (with N being a parameter) candidate subsequent tokens with the highest probabilities at each step, but only up to a certain number of steps. In the end, the model generates the sequence of tokens (i.e., the beam) with the highest joint probability.

This significantly reduces the search space and produces more consistent results. However, this method might be slower and lead to suboptimal outputs as it can miss high-probability words hidden behind a low-probability word.

### Top-K Sampling

Top-K Sampling is a variant of the sampling method where the model narrows down the sampling pool to the top K (with K being a parameter) of the most probable words. This method provides a balance between diversity and relevance by limiting the sampling space, thus offering more control over the generated text.

### Top-p (Nucleus) Sampling

Top-p, or Nucleus Sampling, selects words from the smallest possible set of tokens whose cumulative probability exceeds a certain threshold P (with P being a parameter). This method offers fine-grained control and avoids the inclusion of rare or low-probability tokens. However, the dynamically determined shortlist sizes can sometimes be a limitation.

---

## Parameters That Influence Text Generation
Apart from the decoding methods, several parameters can be adjusted to influence text generation using LLMs. These include temperature, stop sequences, frequency, and presence penalties.

These parameters can be adjusted with the most popular LLM APIs and Hugging Face models.

### Temperature

The temperature parameter influences the randomness or determinism of the generated text. A lower value makes the output more deterministic and focused, while a higher value increases the randomness, leading to more diverse outputs.

It controls the randomness of predictions by scaling the logits before applying softmax during the text generation process. It's a crucial factor in the trade-off between diversity and quality of the generated text.

Controls **randomness** in predictions:

* **Low temperature (< 1)**: More conservative and focused.
* **High temperature (> 1)**: More creative and diverse.
* **Temperature = 1**: No scaling, neutral setting.

**Technical Insight:**

* Applies to the **logits** (raw token scores) before softmax.
* Affects the probability distribution over the vocabulary.

### Stop Sequences

* Predefined sequences that **halt generation** once encountered.
* Useful for delimiting output structure (e.g., stopping at "### End").

### Frequency Penalty

* Discourages repeated use of the **same token** based on its frequency in the generated text.

### Presence Penalty

* Penalizes tokens that **have already appeared**, regardless of frequency.

These parameters are adjustable in many LLM APIs and libraries such as Hugging Face.

---

## Conclusion

To effectively control the behavior of an LLM, we can:

* Choose appropriate **decoding strategies** (greedy, beam, sampling).
* Adjust **temperature, stop sequences, and penalties** to shape the style and accuracy of outputs.

These tools allow us to tailor LLMs for tasks that require either **focused, deterministic responses** or **creative, varied outputs**, depending on the application.

---

