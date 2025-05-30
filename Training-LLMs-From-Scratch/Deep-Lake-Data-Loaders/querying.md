## Querying and Filtering with TQL

Deep Lake includes a SQL-like query language to filter datasets.

```python
view = ds.query('text.contains("1")')

for sample in view:
    print(sample['text'].numpy())
```

### Save and Load Views

```python
view.save_view(id="strings_with_1")
ds = deeplake.dataset(f"hub://{username}/{dataset_name}/.queries/strings_with_1")
```
