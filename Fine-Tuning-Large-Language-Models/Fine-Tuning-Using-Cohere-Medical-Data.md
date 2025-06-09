# Fine-Tuning using Cohere for Medical Data

## Introduction

In this lesson, we explore a no-code method for fine-tuning a large language model using **Cohere**, a platform that enables you to create personalized models by simply providing example inputs and outputs. The fine-tuning process is handled behind the scenes.

Cohere supports various model types via API: **generation**, **classification**, **embedding**, **rerank**, and more. These models are especially useful in **Retrieval Augmented Generation (RAG)** workflows.

We'll focus on **Named Entity Recognition (NER)** using scientific abstracts. Our goal is to extract **diseases, chemicals, and their relationships** from texts using a fine-tuned generative model.

---

## Cohere API Setup

1. Create an account at [Cohere](https://cohere.com).
2. Obtain your **API key** from the "API Keys" section.
3. Install the SDK:

```bash
pip install cohere

Run a basic generation example:
import cohere  

co = cohere.Client("<API_KEY>")

prompt = """The following article contains technical terms including diseases, drugs and chemicals. Create a list only of the diseases mentioned.

Progressive neurodegeneration of the optic nerve and the loss of retinal ganglion cells is a hallmark of glaucoma..."""

response = co.generate(  
    model='command',  
    prompt=prompt,  
    max_tokens=200,  
    temperature=0.75)

print(response.generations[0].text)

Sample Output:
- glaucoma
- primary open-angle glaucoma

Dataset: BC5CDR
We use the BioCreative V Chemical Disease Relation (BC5CDR) dataset:
📦 1,500 PubMed abstracts annotated with diseases, chemicals, and relations.
Our goal: fine-tune a model to extract structured info from unstructured abstracts.

Preprocessing and Formatting
Cohere supports input in JSONL format:
{"prompt": "text", "completion": "label"}

Example (Python):
import json

with open('bc5cdr.json') as json_file:
    data = json.load(json_file)

instruction = "The following article contains technical terms including diseases, drugs and chemicals. Create a list only of the diseases mentioned.\n\n"
output_instruction = "\n\nList of extracted diseases:\n"

the_list = []

for item in data:
    if item['dataset_type'] != "train":
        continue
    diseases = []
    for ent in item['passages'][1]['entities']:
        if ent['type'] == "Disease" and ent['text'][0] not in diseases:
            diseases.append(ent['text'][0])

    the_list.append({
        'prompt': instruction + item['passages'][1]['text'] + output_instruction,
        'completion': "- " + "\n- ".join(diseases)
    })

with open("disease_instruct_all.jsonl", "w") as outfile:
    for item in the_list:
        outfile.write(json.dumps(item) + "\n")

This gives you a clean, ready-to-upload training file: disease_instruct_all.jsonl.

Fine-Tuning on Cohere
Go to Cohere Dashboard → Models → “Create a custom model”.
Select Generative.
Upload your .jsonl file.
Name your model.
(Optional) Configure hyperparameters (training steps, batch size, learning rate).
Click Initiate Training.
📧 You’ll receive an email once the model is ready.


Inference with Custom Model
Use your model ID from the Cohere dashboard:

response = co.generate(  
    model='your-model-id',  
    prompt=prompt,  
    max_tokens=200,  
    temperature=0.75)

print(response.generations[0].text)

Sample Output (Fine-Tuned Model):
- neurodegeneration
- glaucoma
- blindness
- POAG
- glaucomas
- retinal degenerative diseases


Comparisons
Chemical Extraction
Prompt:

Create a list only of the chemicals mentioned in this abstract…

Base Model Output:
- 5-azacytidine (5-AzC)
- benzo[a]-pyrene
- N-methyl-N-nitrosourea
- 1,2-dimethylhydrazine
- CCl4
- 2-acetylaminofluorene

Fine-Tuned Output:
- 5-azacytidine
- 5-AzC
- benzo[a]-pyrene
- N-methyl-N-nitrosourea
- 1,2-dimethylhydrazine
- 1,2-DMH
- 2-acetylaminofluorene
- CCl4
- [3H]-5-azadeoxycytidine
- cytosine

Relation Extraction
Prompt:
Create a list only of the influences between chemicals and diseases…

severe cirrhosis of the liver influences … carbon tetrachloride, phenobarbitone

Fine-Tuned Output:
- Chemical phenobarbitone influences disease cirrhosis of the liver
- Chemical carbon tetrachloride influences disease cirrhosis of the liver

Conclusion
✅ You used Cohere to fine-tune a generative LLM with NER capabilities
✅ You saw clear improvements in extracting domain-specific information
✅ You used only ~1K examples per task
✅ No infrastructure setup or custom training loops required

Cohere offers an excellent no-code or low-code interface for rapid fine-tuning. It’s especially powerful for domain experts who want to adapt LLMs without deep ML engineering knowledge.

