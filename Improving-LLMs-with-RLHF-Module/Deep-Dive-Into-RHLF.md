# Deep Dive into RLHF

## Introduction

In this lesson, we explore **Reinforcement Learning from Human Feedback (RLHF)**—a method that combines human preferences with reinforcement learning to improve Large Language Models (LLMs).

You'll learn how RLHF compares to Supervised Fine-Tuning (SFT), and explore its prominent alternatives like **Direct Preference Optimization (DPO)** and **Reinforced Self-Training (ReST)**.

---

## Understanding RLHF

RLHF integrates human feedback into the training loop of LLMs, improving alignment with human values and producing safer, more useful models.

It was first introduced in **InstructGPT** and is a key component in models like **ChatGPT (GPT-3.5-turbo)** and **GPT-4**.

> Human rankings guide model behavior via a reward model, which is optimized using the **Proximal Policy Optimization (PPO)** algorithm.

---

## RLHF Training Process

The RLHF workflow involves several stages:

1. **(Optional) Instruction Tuning**  
   Fine-tune the base LLM on instruction-following datasets to speed up RL convergence.

2. **Dataset Creation**  
   Generate multiple completions per instruction using the LLM.

3. **Human Feedback Collection**  
   Rank completions based on quality (e.g., relevance, accuracy, safety).

4. **Reward Model Training**  
   Train a reward model to score completions based on collected feedback.

5. **Reinforcement Learning with PPO**  
   Use PPO to update the LLM based on reward scores while maintaining similarity (KL-divergence) with the original model.

---

## RLHF vs. SFT

While **SFT (Supervised Fine-Tuning)** with high-quality data (e.g., LIMA dataset) can produce aligned models, **RLHF** is more effective at:

- Capturing nuanced human preferences
- Fine-tuning safety and helpfulness aspects

> However, RLHF is computationally intensive and less stable than SFT. It requires careful hyperparameter tuning and often restarts.

---

## Alternatives to RLHF

### 1. Direct Preference Optimization (DPO)

- **No reward model or RL** required
- Uses **binary cross-entropy loss** on preference data
- Simplifies training and reduces instability
- Optimizes LLMs directly using preference comparisons

---

### 2. Reinforced Self-Training (ReST)

From **Google DeepMind**, ReST reduces compute and simplifies the RL pipeline:

- **Grow Step**: LLM generates multiple outputs
- **Improve Step**: Reward model filters outputs; LLM is fine-tuned offline

**Advantages**:
- Lower compute cost
- Stable and reproducible
- Easy to debug and inspect

---

### 3. Reinforcement Learning from AI Feedback (RLAIF)

From **Anthropic**, RLAIF replaces human feedback with an **AI Feedback Model** guided by a **constitution**.

- Feedback model ranks outputs using predefined principles
- Reward model is trained from this feedback
- LLM is fine-tuned using RL on AI-generated preferences

**Benefits**:
- More scalable and objective
- Improves harmlessness while preserving helpfulness
- Similar human preference ratings as RLHF

---

## Conclusion

This lesson gave you a comprehensive understanding of RLHF, including:

- The complete RLHF training pipeline
- A comparison with SFT
- Alternatives like DPO, ReST, and RLAIF

> As I continue advancing these methods, we move closer to building LLMs that are **aligned, efficient, and safe** for real-world use.
