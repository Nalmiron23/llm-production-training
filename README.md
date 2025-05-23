# llm-production-training

**Educational project based on the course _"Train & Fine-Tune LLMs for Production"_ by Activeloop, Towards AI, and Intel®.**

This repository contains code, tools, and resources for training, fine-tuning, and deploying Large Language Models (LLMs) in production environments using a range of platforms and open-source technologies.

---

## What I wil be doing in This Project

Use [Meta's LLaMA 2](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) locally via [LM Studio](https://lmstudio.ai)  
Build training and inference pipelines for LLMs using:
- 🤖 Transformers (Hugging Face)
- 🔄 Supervised Fine-Tuning (SFT)
- 🎯 Reinforcement Learning with Human Feedback (RLHF)
- 💡 LoRA / QLoRA
Use real-world data (e.g., financial sentiment, biomedical) with Deep Lake  
Use GPUs (Lambda Labs, GCP) and CPUs for fine-tuning  
Track experiments with Weights & Biases  
Deploy and test models with Colab, scripts, and cloud VMs

---

## 🛠 Technologies Covered

| Category            | Tools/Platforms                       |
|---------------------|----------------------------------------|
| **LLMs & NLP**       | LLaMA 2, Transformers, GPT, Cohere     |
| **Fine-Tuning**      | LoRA, QLoRA, SFT, RLHF, PEFT, Deepspeed |
| **Infra & Compute**  | LM Studio, Lambda Labs, GCP, AWS EC2   |
| **Data Management**  | Activeloop Deep Lake                   |
| **Experiment Tracking** | Weights & Biases (wandb)             |
| **Cloud Credits**    | Lambda ($100), Cohere ($75), GCP ($300) |

---

## Local Setup (LM Studio + LLaMA 2)

```bash
# Clone this repo
git clone https://github.com/Nalmiron23/llm-production-training.git
cd llm-production-training

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add your credentials
cp .env.example .env
