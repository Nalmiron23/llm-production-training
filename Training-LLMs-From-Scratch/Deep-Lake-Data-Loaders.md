# Deep Lake and Data Loaders

## Introduction

In this lesson, we focus on **Deep Lake**, a powerful AI data system that merges the capabilities of Data Lakes and Vector Databases. We'll explore how Deep Lake can be leveraged for training and fine-tuning Large Language Models, especially through its efficient data streaming. You'll learn how to create a Deep Lake dataset, add data, and load it using both Deep Lake and PyTorch data loaders.

---

## Deep Lake

When training and finetuning LLMs, storing datasets externally is crucial—especially for pretraining, as datasets are often too large to fit in a single computing node. This is where Deep Lake shines.

**Deep Lake** is a multi-modal AI data system ideal for LLM training. It streams data from remote storage to GPUs efficiently and is especially useful for:

- Model training
- Dataset versioning
- Vector search and retrieval

### Deep Lake Loaders

There are two types of data loaders:

- **Open Source (OSS) Data Loader**
- **Performant Data Loader** (C++ based and 1.5–3× faster)

Once a dataset is stored in Deep Lake, you can easily create a `PyTorch Dataloader` or a `TensorFlow Dataset`.

---

## Creating a Deep Lake Dataset and Adding Data

Install Deep Lake:

```bash
pip install deeplake==3.9.27
```

🔑 **Create an Activeloop account and generate your API token. Save it in your environment as ACTIVELOOP_TOKEN.**
**Load the .env file in Python:**
```
from dotenv import load_dotenv
load_dotenv()
```

**Then create your dataset:**
```
import deeplake

username = "<YOUR_ACTIVELOOP_USERNAME>"
dataset_name = "test_dataset"
ds = deeplake.dataset(f"hub://{username}/{dataset_name}")

ds.create_tensor('text', htype="text")

texts = [f"text {i}" for i in range(1, 11)]
for text in texts:
    ds.append({"text": text})
```
**Commit the changes:**
``
ds.commit("added texts")
```
You can now view your dataset at:
https://app.activeloop.ai/<YOUR_ACTIVELOOP_USERNAME>/test_dataset

Retrieving Data From Deep Lake
There are two main ways to retrieve data:

1. Using Deep Lake's Native Data Loader (Fastest)
batch_size = 3
train_loader = ds.dataloader().batch(batch_size).shuffle().pytorch()

for i, batch in enumerate(train_loader):
    print(f"Batch {i}")
    samples = batch.get("text")
    for j, sample in enumerate(samples):
        print(f"Sample {j}: {sample}")

2. Using PyTorch’s Custom DataLoader (More Flexible, Slower)
from torch.utils.data import DataLoader, Dataset

class DeepLakePyTorchDataset(Dataset):
    def __init__(self, ds):
        self.ds = ds

    def __len__(self):
        return len(self.ds)

    def __getitem__(self, idx):
        texts = self.ds.text[idx].text().astype(str)
        return { "text": texts }

ds_pt = DeepLakePyTorchDataset(ds)
dataloader_pytorch = DataLoader(ds_pt, batch_size=3, shuffle=True)

for i, batch in enumerate(dataloader_pytorch):
    print(f"Batch {i}")
    samples = batch.get("text")
    for j, sample in enumerate(samples):
        print(f"Sample {j}: {sample}")
    Querying and Filtering Data
Deep Lake offers Tensor Query Language (TQL) to filter datasets efficiently.

python
Copy
Edit
view = ds.query('text.contains("1")')

for sample in view:
    print(sample['text'].numpy())
Save the view:

python
Copy
Edit
view.save_view(id="strings_with_1")
Load the view later:

python
Copy
Edit
ds = deeplake.dataset(f"hub://{username}/{dataset_name}/.queries/strings_with_1")
Advanced: Samplers
Use samplers to assign different importance to data samples. This helps prioritize higher-quality examples during training.

Conclusion
In this lesson, we explored how Deep Lake enables scalable, efficient data handling for LLMs:

✅ Store and retrieve large datasets

✅ Use fast performant data loaders

✅ Leverage PyTorch interoperability

✅ Query and filter data using TQL

✅ Version datasets and manage data quality

As we move forward in training and fine-tuning LLMs, Deep Lake will serve as a powerful and practical data backend.

