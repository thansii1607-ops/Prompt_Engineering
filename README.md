# 🤖 Prompt Engineering App

A simple and interactive **Prompt Engineering Web Application** built using **Python, Streamlit, Hugging Face, and Groq**.

This project demonstrates how different prompting techniques can change the way an LLM generates responses.

##  Live Demo

🔗 https://promptengineering-g2hrrdzaedfzi5conu9dho.streamlit.app/

##  Features

-  Interactive LLM-based response generation
-  Multiple Prompt Engineering techniques
-  Temperature control
-  Maximum token control
-  View generated prompts
-  Real-time response generation
-  Web-based Streamlit interface

##  Prompting Techniques

### 1. Zero-shot Prompting
Generates an answer without providing any example.

### 2. One-shot Prompting
Provides one example to guide the model's response.

### 3. Few-shot Prompting
Provides multiple examples to improve the expected response style.

### 4. Chain-of-Thought (CoT)
Encourages the model to solve a task using logical steps while showing only a concise explanation.

### 5. Manual Chain-of-Thought
Uses a predefined step-by-step reasoning structure.

### 6. Tree-of-Thoughts (ToT)
Explores multiple possible approaches and selects a suitable solution.

##  Technologies Used

- Python
- Streamlit
- Hugging Face
- Groq
- Hugging Face Hub
- python-dotenv

##  Project Structure

```text
Prompt-Engineering/
│
├── app.py
├── prompt_template.py
├── llm.py
├── requirements.txt
├── .gitignore
└── README.md
