## Installation and Setup

### 1. Install Deep Lake

```bash
pip install deeplake==3.9.27
```

### 2. Generate API Token

- Sign up at [Activeloop Hub](https://app.activeloop.ai)
- Create an API token and set it as an environment variable:

```bash
export ACTIVELOOP_TOKEN=your_token_here
```

Or store it in a `.env` file and load it in Python:

```python
from dotenv import load_dotenv
load_dotenv()
```
