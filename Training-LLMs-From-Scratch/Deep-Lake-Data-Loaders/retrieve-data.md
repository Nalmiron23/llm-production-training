## Retrieving Data

### 🔁 Option 1: Deep Lake Native Loader (Fastest)

```python
batch_size = 3
train_loader = ds.dataloader().batch(batch_size).shuffle().pytorch()

for i, batch in enumerate(train_loader):
    print(f"Batch {i}")
    for j, sample in enumerate(batch["text"]):
        print(f"Sample {j}: {sample}")
```

### 🧩 Option 2: PyTorch Custom Loader (More Flexible)

```python
from torch.utils.data import DataLoader, Dataset

class DeepLakePyTorchDataset(Dataset):
    def __init__(self, ds):
        self.ds = ds

    def __len__(self):
        return len(self.ds)

    def __getitem__(self, idx):
        return {"text": self.ds.text[idx].text().astype(str)}

ds_pt = DeepLakePyTorchDataset(ds)
dataloader_pytorch = DataLoader(ds_pt, batch_size=3, shuffle=True)

for i, batch in enumerate(dataloader_pytorch):
    print(f"Batch {i}")
    for j, sample in enumerate(batch["text"]):
        print(f"Sample {j}: {sample}")
```
