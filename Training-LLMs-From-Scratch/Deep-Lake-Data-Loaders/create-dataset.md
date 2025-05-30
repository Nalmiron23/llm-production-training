## Creating and Populating a Dataset

```python
import deeplake

username = "<YOUR_ACTIVELOOP_USERNAME>"
dataset_name = "test_dataset"
ds = deeplake.dataset(f"hub://{username}/{dataset_name}")

ds.create_tensor('text', htype="text")

texts = [f"text {i}" for i in range(1, 11)]
for text in texts:
    ds.append({"text": text})

ds.commit("added texts")
```

🎯 View your dataset at:
```
https://app.activeloop.ai/<YOUR_ACTIVELOOP_USERNAME>/test_dataset
```