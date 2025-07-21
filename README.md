GenAI Setup on macOS + Day 3 LLM Integration Log
🔧 Setup Guide: GenAI Python Project on macOS
1. Create a Project Folder
bash
Copy
Edit
mkdir genaiApp && cd genaiApp
code .
This opens the folder in VS Code.

2. Create a Virtual Environment Using uv
❌ Don’t run:

bash
Copy
Edit
pip install uv
✅ If uv is already installed:

bash
Copy
Edit
uv venv
This will create a .venv folder for isolated dependencies.

3. Activate the Virtual Environment
bash
Copy
Edit
source .venv/bin/activate
If you face a "Permission denied" error:

bash
Copy
Edit
chmod +x .venv/bin/activate
source .venv/bin/activate
4. Initialize the uv Project
bash
Copy
Edit
uv init
5. Install Project Dependencies
If you have a requirements.txt:

bash
Copy
Edit
uv pip install -r requirements.txt
6. Run Your GenAI Script
bash
Copy
Edit
python ollama_without_langchain.py
📘 Day 3: AI LLM Integration Learning Log
🔗 LangChain Key Concepts
Model: LLM provider (e.g., OpenAI, Gemini, Claude)

Chains: Sequences of logical calls using LLMs

Prompts: Templates to manage structured input/output

Memory: Retains conversational state across turns

🔐 Gemini AI Setup
API Key: AIzaSyAtDgyuy-4sv5OwTrxahy6iyKz4AVie894

✅ Successfully integrated using Python + LangChain

📌 Used for real-time LLM inference via Google Gemini

📌 Assignment 2: Integrate Claude (Anthropic)
🎯 Goal: Connect Claude with Python or LangChain

✅ Use Claude’s API key (from Anthropic)

🔜 Next Steps:

Generate Claude API key from Anthropic dashboard

Install & configure anthropic Python package

Explore LangChain's ChatAnthropic wrapper

☁️ Other Providers Plan
🧰 Boto3 (AWS)
Will explore integration via AWS Bedrock if needed

⚡ GROQ
High-speed LLM inference engine

Does not use GPUs, uses custom LPUs

📌 To test and compare latency vs Gemini/Claude

🤗 Hugging Face Integration
Option 1: Inference API
Call public models via API key

Limited free calls per month

✅ Best for light, real-time usage

Option 2: Run Locally
Download LLMs like in Ollama

Needs high config system (RAM, CPU, possibly GPU)

Tools: transformers, torch, etc.

📌 Will try if system supports

Option 3: Hugging Face Spaces
Free hosting platform for LLM-based apps

Like EC2 but limited compute

Great for demos, not fine-tuning models

📝 Practice & Review Plan
✅ Start: Gemini + LangChain integration

🔜 Next: Claude API integration

✅ Today: Run Hugging Face Inference API (Option 1)

📆 This Week: Test Option 2 (local model run)