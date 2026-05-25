# ⚡ Fast Groq AI Agent

Ultra-fast AI chatbot powered by Groq + Streamlit.

Live streaming responses with a clean web interface.

Live demo : https://reactagent-hgvxbfusl2jzyuufajsgoh.streamlit.app/

---

## 🚀 Features

- ⚡ Extremely fast responses
- 🌐 Browser-based AI chatbot
- 💬 Chat history support
- 🔒 Secure API key handling
- 🎯 Lightweight architecture
- 📦 Easy deployment
- ☁️ Streamlit Cloud ready
- 🧠 Powered by Groq LLMs

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq SDK
- python-dotenv

---

## 📂 Project Structure

```text
fast-groq-agent/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/KishanG02/React_agent.git
```

```bash
cd fast-groq-agent
```

---

### 2. Create Virtual Environment

```bash
python3.11 -m venv venv
```

Activate:

#### Mac/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create `.env`

```env
GROQ_API_KEY=gsk_your_actual_key
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Open browser:

```text
http://localhost:8501
```

---

## ⚡ Recommended Models

| Model | Speed | Quality |
|---|---|---|
| llama-3.1-8b-instant | Very Fast | Good |
| llama-3.3-70b-versatile | Fast | Excellent |
| mixtral-8x7b-32768 | Medium | Very Good |

---

## ☁️ Deploy Online

Deploy free using Streamlit Cloud:

https://share.streamlit.io

### Deployment Steps

1. Push code to GitHub
2. Login to Streamlit Cloud
3. Select repository
4. Deploy app
5. Add Secrets:

```toml
GROQ_API_KEY="gsk_your_actual_key"
```

---

## 🔒 Important

Never upload `.env` file to GitHub.

Add this to `.gitignore`

```gitignore
.env
venv/
```

---

## 📸 Preview

```text
⚡ Fast Groq AI Agent
Ask anything...
```



## 🙌 Author

Krishna Gupta
