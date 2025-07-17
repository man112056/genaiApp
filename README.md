
# GenAI Setup on macOS

### Step-by-Step Guide

---

### 1. **Create a Project Folder**

Open your terminal and run:

```bash
mkdir genaiApp && cd genaiApp
code .
```

> This opens the folder in VS Code.

---

### 2. **Create a Virtual Environment using `uv`**

>  **Do NOT use**:

```bash
pip install uv
```

> Instead, if `uv` is already installed:

```bash
uv venv
```

This will create a `.venv` folder.

---

### 3. **Activate the Virtual Environment**

Run:

```bash
source .venv/bin/activate
```

> If you see `Permission denied`, run this:

```bash
chmod +x .venv/bin/activate
source .venv/bin/activate
```

---

### 4. **Initialize `uv` Project**

```bash
uv init
```

---

### 5. **Install Dependencies**

Assuming you have a `requirements.txt`:

```bash
uv pip install -r requirements.txt
```

---

### 6. **Run Your GenAI Python Script**

```bash
python ollama_without_langchain.py
```