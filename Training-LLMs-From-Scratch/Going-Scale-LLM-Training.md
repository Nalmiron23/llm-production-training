# Going at Scale with LLM Training

## Introduction

In this lesson, we will share some tips for training LLMs at scale, focusing on the **Zero Redundancy Optimizer (ZeRO)** and its implementation in **DeepSpeed**. We explore how ZeRO optimizes memory and computational resources, its various stages of operation, and the benefits of DeepSpeed. We also touch on the **Hugging Face Accelerate** library. Finally, we discuss the importance of maintaining a **logbook of training runs** to manage potential challenges and instabilities during the training process.

---

## The Zero Redundancy Optimizer (ZeRO)

Training Large Language Models can be a formidable task due to immense computational and memory requirements. ZeRO, implemented in DeepSpeed, allows training these models with fewer hardware resources.

**ZeRO** is a parallelized optimizer that drastically reduces memory use and computation overhead by distributing model states across GPUs/CPUs:
- **Weights**
- **Gradients**
- **Optimizer States**

This allows ZeRO-powered data parallelism to accommodate **models of any size** as long as there is enough aggregated device memory.

---

### The Stages of ZeRO

Each stage introduces optimizations on top of the previous:

- **Stage 1 – Optimizer State Partitioning**  
  Reduces memory usage 4x. Suitable for 1.5B parameter GPT-2 on 8 V100 GPUs.

- **Stage 2 – Gradient Partitioning**  
  Adds gradient partitioning for 8x memory savings. Enables training of 10B parameter GPT-2 on 32 V100 GPUs.

- **Stage 3 – Parameter Partitioning**  
  Adds parameter sharding. Enables training trillion-parameter models on 512 GPUs.

- **Stage 3 Extra – CPU/NVMe Offloading (ZeRO-Infinity)**  
  Offloads states to CPU/NVMe memory, allowing single-GPU training of massive models.

---

## DeepSpeed

**DeepSpeed** is a high-performance library for distributed deep learning, incorporating ZeRO and more:

- 🚀 **Scale**: Enables training models up to 100B parameters  
- ⚡ **Speed**: Combines data/model parallelism for 5× throughput  
- 💰 **Cost**: Cuts compute costs by up to 3×  
- 🛠️ **Usability**: Works with minimal code changes and integrates easily with PyTorch

---

## Accelerate and DeepSpeed ZeRO

[Hugging Face Accelerate](https://huggingface.co/docs/accelerate/index) allows integration of **DeepSpeed ZeRO** with minimal modifications.  
With Accelerate + ZeRO, you can **increase batch sizes**, **reduce OOM errors**, and **scale training** seamlessly.

---

## Logbook of Training Runs

Even with ZeRO and Accelerate, training LLMs at scale can result in instabilities.  
Spikes in the **loss function** or sudden divergence may require **manual intervention**.

📝 **Checkpoint Rollbacks** are often used to recover training:
- Restore a saved checkpoint
- Reduce the learning rate
- Resume training

📘 For example:
- [Meta’s 114-page training logbook](https://huggingface.co/blog/optdiary) for OPT-175B
- Hugging Face’s Flamingo reproduction had multiple rollbacks during loss divergence

Maintaining a logbook helps track changes, issues, and tuning choices during long training runs.

---

## Conclusion

This lesson covered tips for **training Large Language Models at scale**, focusing on:
- **ZeRO optimizer** and its memory-saving stages
- **DeepSpeed** for distributed and accelerated training
- **Hugging Face Accelerate** for simple scaling
- The **importance of training logs** and check-pointing

If you're aiming to train models at the billion+ parameter level, understanding these techniques is essential. For more depth, explore the [official DeepSpeed docs](https://www.deepspeed.ai/).

