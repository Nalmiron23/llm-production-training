# Benchmarking Your Own LLM

## Introduction

In a previous lesson, we touched upon several methodologies for assessing the effectiveness of different language models. Even with various available methodologies, evaluating a large language model continues to pose significant challenges.

The primary difficulty lies in the subjectivity of what defines a "good" answer—especially for generative tasks like summarization, where correctness is often not binary. This makes objective evaluation complex across nearly all generative tasks.

In this lesson, we’ll explore how benchmarks offer a potential solution.

---

## Benchmarks Over Several Tasks

To overcome subjective evaluation, we rely on curated benchmarks that assess models across a variety of tasks—ranging from instruction-following and world knowledge to programming and commonsense reasoning.

Some popular benchmark datasets include:

- **AI2 Reasoning Challenge (ARC)** – Grade-school science questions.
- **HumanEval** – Programming tasks from docstrings.
- **HellaSwag** – Tests commonsense inference.
- **MMLU** – Covers 57 tasks from various domains.
- **TruthfulQA** – Measures truthfulness across 817 real-world questions.

### Leaderboards

- [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
- [InstructEval Leaderboard](https://instructeval.github.io/)

These leaderboards often use overlapping tasks and metrics to ensure fair model comparisons.

---

## Language Model Evaluation Harness

[EleutherAI’s `lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness) is a benchmarking library capable of evaluating both open-source and API-based language models across 200+ tasks.

### Key Features

- Customizable for generative tasks
- Supports Hugging Face and OpenAI models
- Prompt standardization for fair comparison
- Task versioning for reproducibility

---

### Installation

```bash
git clone https://github.com/EleutherAI/lm-evaluation-harness
cd lm-evaluation-harness && git checkout e2eb966  # Pin to version 0.3.0

List Available tasks

from lm_eval import tasks
print(tasks.ALL_TASKS)

Run Evaluation (Example)
Evaluate facebook/opt-1.3b on hellaswag:
python main.py \
  --model hf-causal \
  --model_args pretrained=facebook/opt-1.3b \
  --tasks hellaswag \
  --device cuda:0

Sample Output
{
  "results": {
    "hellaswag": {
      "acc": 0.4147,
      "acc_stderr": 0.0049,
      "acc_norm": 0.5368,
      "acc_norm_stderr": 0.0050
    }
  }
}

Customize Model Arguments
You can specify model revisions and datatypes like this:
--model_args pretrained=EleutherAI/pythia-160m,revision=step100000,dtype=float

Evaluate OpenAI Models
export OPENAI_API_SECRET_KEY=YOUR_KEY_HERE

python main.py \
  --model gpt3 \
  --model_args engine=davinci \
  --tasks hellaswag

Combine Multiple Tasks
--tasks hellaswag,arc_challenge

InstructEval
InstructEval is another evaluation framework tailored for instruction-tuned models. It blends automated benchmarks with GPT-4-based scoring.

Three Main Evaluation Categories
1. Problem-Solving Evaluation
Tests include:

MMLU (World Knowledge)

BBH (Complex Instructions)

DROP (Reasoning over Paragraphs)

HumanEval (Programming)

CRASS (Causality)

2. Writing Evaluation
GPT-4 evaluates generated outputs on a 1–5 Likert scale using the following criteria:

Informative

Professional

Argumentative

Creative

3. Alignment to Human Values
Evaluates preference between pairs of completions to judge:

Helpfulness

Honesty

Harmlessness


Conclusion

Standardized evaluation metrics are crucial for comparing models fairly. In this lesson, we explored:

Popular benchmarks and leaderboards

The lm-evaluation-harness library

The InstructEval framework

Not every model must excel in every metric. Focus on benchmarks most relevant to your use case and keep an eye on evolving leaderboards.



Notebook: https://colab.research.google.com/drive/1d4gJso06wgSq6Rj7JmPKnNjY8i1Bd78g?usp=sharing