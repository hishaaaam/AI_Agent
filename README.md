# 🤖 Open-Source AI Agent Pro (Hugging Face)

A **production-ready AI Agent** built entirely with **open-source Hugging Face models**.
It can understand user queries, decide when to call tools, and respond intelligently — all wrapped in a **professional, interactive Streamlit UI**.

🔗 **Live Demo (Hugging Face Space):**
👉 https://huggingface.co/spaces/hishaaaam/AIagent

---

## ✨ Features

* 🧠 Open-source LLM (no OpenAI dependency)
* 🔧 Function / Tool Calling (Calculator + Weather)
* 💬 Persistent Chat Memory
* ⚡ Optimized for Hugging Face Spaces (CPU friendly)
* 🎨 Netflix-style professional UI
* 🚀 Cached model loading for fast performance
* 📱 Mobile-responsive interface
* 🧩 Clean modular architecture
* 🆓 Fully free and self-hostable

---

## 🏗️ Architecture

```
User → Streamlit UI → LLM → Tool Decision → Function Execution → Final Response
```

**Flow:**

1. Receives user input
2. LLM decides whether to call a tool
3. Tool executes
4. Agent returns formatted answer

---

## 📁 Project Structure

```
ai-agent-hf-pro/
│
├── app.py              # Streamlit UI
├── agent.py            # Agent brain + routing
├── tools.py            # External functions
├── config.py           # Model configuration
├── requirements.txt
├── README.md
└── .streamlit/
    └── config.toml
```

---

## 🧠 Model Used

**Default:** `TinyLlama/TinyLlama-1.1B-Chat-v1.0`

**Why this model?**

* ✅ Lightweight
* ✅ Fast on CPU
* ✅ Works on Hugging Face free tier
* ✅ Good instruction following

You can easily swap models in `config.py`.

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-agent-hf-pro.git
cd ai-agent-hf-pro
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the App

```bash
streamlit run app.py
```

App will open at:

```
http://localhost:8501
```

---

## 🚀 Hugging Face Spaces Deployment

This project is **Spaces-ready**.

### Recommended Settings

* **SDK:** Streamlit
* **Hardware:** CPU Basic
* **Python:** 3.10

Then simply upload the repository files.

---

## 🧪 Example Prompts

Try these in the chat:

```
What is 45 * 22?
Weather in Mumbai
Explain machine learning simply
```

---

## 🔧 Available Tools

### 🧮 Calculator

Evaluates mathematical expressions.

**Example**

```
User: What is 234 * 56?
Agent → calculator → result
```

---

### 🌤️ Weather (Mock)

Returns sample weather data.

**Example**

```
User: Weather in Delhi
Agent → get_weather → result
```

> 🔮 You can easily connect a real weather API.

---

## ⚡ Performance Optimizations

This project includes:

* `@st.cache_resource` model caching
* CPU-friendly lightweight model
* Low temperature for stable routing
* Lightweight UI rendering
* Hugging Face Spaces configuration

---

## 🎨 UI Highlights

* Glassmorphism chat bubbles
* Dark professional theme
* Typing spinner
* Persistent conversation memory
* Wide responsive layout
* Clean modern typography

---

## 🔄 How Tool Calling Works

The LLM is instructed to output in a strict format:

```
TOOL: calculator | expression=2+2
```

The agent then:

1. Parses the tool name
2. Executes the function
3. Returns the result

This keeps the system:

* simple
* transparent
* fully open-source

---

## 🧩 Future Improvements

Planned upgrades:

* [ ] Streaming responses
* [ ] Multi-tool reasoning
* [ ] RAG knowledge base
* [ ] Voice input
* [ ] LangGraph agent loop
* [ ] Real weather API
* [ ] Docker deployment

---

## 🤝 Contributing

Contributions are welcome!

You can help improve:

* UI/UX
* model performance
* new tools
* memory system

Feel free to fork and submit a PR.

---

## 📜 License

MIT License — free to use and modify.

---

## 👤 Author

**Hisham Hidayathulla**

If you found this useful, consider ⭐ starring the repo!

---

**Built with ❤️ using Hugging Face + Streamlit**
