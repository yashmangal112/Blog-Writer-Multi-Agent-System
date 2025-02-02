# AI-Powered Blog Writer: A Multi-Agent System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Gradio](https://img.shields.io/badge/Gradio-UI%20Framework-orange)
![CrewAI](https://img.shields.io/badge/CrewAI-MultiAgent%20Framework-green)
![LangChain](https://img.shields.io/badge/LangChain-LLM%20Integration-yellow)
![Groq](https://img.shields.io/badge/Groq-Llama%203%20LLM-red)

An AI-powered multi-agent system for automated blog content creation. This project uses **CrewAI**, **LangChain**, and **Groq (Llama 3)** to plan, write, and edit blog posts based on a given topic.


## 🚀 Features

- **Automated Content Planning**: Generates detailed outlines, identifies target audiences, and incorporates SEO strategies.
- **AI-Driven Writing**: Crafts well-structured, insightful, and SEO-optimized articles.
- **Editorial Excellence**: Ensures grammatical accuracy, brand alignment, and balanced viewpoints.
- **User-Friendly Interface**: Built with **Gradio** for easy interaction and testing.


## 🛠️ Tech Stack

- **Python**: Core programming language.
- **CrewAI**: Multi-agent framework for task delegation and workflow management.
- **LangChain**: Integration with LLMs (Groq and MistralAI).
- **Groq (Llama 3)**: High-performance LLM for content generation.
- **Gradio**: Simple and interactive UI for user input and output.


## 📦 Installation

1. **Clone the Repository**:
```bash
git clone https://github.com/your-username/ai-blog-writer.git
cd ai-blog-writer
```
2. **Set Up a Virtual Environment (Optional but Recommended)**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install Dependencies**:
```bash
pip install -r requirements.txt
```
4. **Set Up API Keys**:
```python
# Add your Groq API Key to the llm_model.py file
import os
os.environ["GROQ_API_KEY"] = 'your-groq-api-key-here'
```

## 🖥️ Usage

```bash
# Run the Application
python app.py
```

- **Access the Gradio Interface:**  
  Open the provided URL (e.g., http://127.0.0.1:7860/) in your browser.

- **Enter a topic in the input box and click Submit.**

### Example Input:
```text
Topic: "Comparative study of LangGraph, Autogen, and CrewAI for building multi-agent systems."
```

### Example Output:
A well-structured blog post in markdown format.


## 🧩 How It Works

- **Content Planner Agent:**  
  Plans the blog structure, identifies key points, and incorporates SEO strategies.

- **Blog Writer Agent:**  
  Writes the blog post based on the content plan, ensuring clarity and engagement.

- **Editor Agent:**  
  Reviews and edits the blog post for grammatical accuracy and brand alignment.

## 🌐 Deployment

### Local Deployment
```bash
python app.py
```

### Cloud Deployment
- **Hugging Face Spaces:**
  Create a new Space on Hugging Face and Push the code files to a HuggingFace Space repository.
  Add your groq_api_key into secrets section in your space
  Hugging Face will automatically deploy the Gradio app.

## 📂 Project Structure

```plaintext
ai-agents-blog-writer/
├── agents.py         # Handles AI agents like planner, writer, and editor
├── tasks.py         # Handles tasks info of all AI agents
├── app.py           # Entry point of the Gradio app
├── requirements.txt  # Project dependencies
├── README.md         # Documentation
├── .gitignore        # Files to ignore in version control
└── venv/             # (Optional) Virtual environment files
```


## 🙏 Acknowledgments

- **CrewAI:** For the multi-agent framework.
- **Groq:** For the high-performance Llama 3 LLM.
- **Gradio:** For the simple and interactive UI.

## 📧 Contact

For questions or feedback, feel free to reach out:

- **Email:** yashmangal240@gmail.com  
- **GitHub:** [yashmangal112](https://github.com/yashmangal112)

> 🚀 **Contributions are welcome!** Feel free to open issues or submit pull requests.
 
