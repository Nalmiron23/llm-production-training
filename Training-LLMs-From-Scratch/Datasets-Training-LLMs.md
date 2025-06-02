# Datasets for Training LLMs

## Introduction

In this lesson, we talk about the datasets that fuel LLMs pretraining. We'll explore popular datasets like Falcon RefinedWeb, The Pile, Red Pajama Data, and Stack Overflow Posts, understanding their composition, sources, and usage. We'll also discuss the emerging trend of prioritizing data quality over quantity in pretraining LLMs.

---

## Popular Datasets for Training LLMs

In recent times, a variety of open-source datasets have been employed for pre-training Large Language Models.

Some of the notable datasets include:

- **Falcon RefinedWeb**
- **The Pile**
- **Red Pajama Data**
- **Stack Overflow Posts**

Assembling such datasets typically involves collecting and cleaning vast volumes of text data.

---

### Falcon RefinedWeb

- Developed by **TII**
- Based on rigorous filtering and deduplication of CommonCrawl
- Multimodal-friendly (includes image links and alt texts)
- Public extract: **500–650GT** tokens (~2.8TB unpacked)
- Contains ~1 billion deduplicated web pages
- Used for: **Falcon-7B/40B**, **Falcon-RW-1B/7B**

> Created using the Macrodata Refinement Pipeline with strict filtering and iterative evaluation.

---

### The Pile

- Created by **EleutherAI**
- 886GB dataset made of 22 sub-datasets (14 are original)
- Built to go beyond Common Crawl with more diversity
- Covers academic writing and various styles
- Public domain, not filtered for biases or profanity
- Used in GPT-Neo and many other LLMs

---

### Red Pajama Dataset

- Emulates the **LLaMa** dataset
- Composed of 2084 `.jsonl` files
- Includes: Commoncrawl, C4, GitHub, Books, ArXiv, Wikipedia, StackExchange
- Token count: **1.2 trillion**
- Structured with metadata (URL, source, language)

> High-quality deduplication and licensing filtering (e.g., GitHub: MIT/BSD/Apache only).

---

### Stack Overflow Posts

- ~60 million posts from StackOverflow (pre-June 14, 2023)
- Sourced from Internet Archive StackExchange Dump
- ~35GB, 65 billion characters
- Contains fields like: `Id`, `PostTypeId`, `Body`, `ContentLicense`

> Ideal for training models in software engineering and technical Q&A.

---

## Data Quality vs. Data Quantity in Pretraining

Many recent datasets (e.g., RefinedWeb, Red Pajama) are **cleaned versions** of earlier data sources.

### 📌 Trend Shift: Quantity → Quality

#### "Textbooks Are All You Need" (Phi-1 Model)

- **Phi-1:** 1.3B parameter model trained on **high-quality textbook-like data**
- Training: 6B tokens from curated web data + 1B synthetic tokens (GPT-3.5)
- Result: Outperformed larger models on **HumanEval**, **MBPP** benchmarks

> This proves high-quality, coherent data can significantly improve model capabilities—even with smaller architectures.

## Conclusion

This lesson provided a comprehensive overview of key datasets used in LLM pretraining.

We examined:

- **Falcon RefinedWeb**
- **The Pile**
- **Red Pajama**
- **Stack Overflow Posts**

We also highlighted the shift toward prioritizing **data quality** over just dataset size—demonstrated by Phi-1's success using carefully curated data.

> High-quality datasets are now considered critical to achieving top-performing LLMs, even when models are smaller in size.

