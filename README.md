# 🚀 JobPrep AI Agent

An **Agentic AI-powered job preparation assistant** built using **LangGraph + FastAPI**, enhanced with **LangSmith tracing** for observability and debugging, and managed using **uv** for fast Python dependency management.

---

## 📌 Features

* 🔍 Job Description Parsing
* 👤 Candidate Profile Extraction (from resume + skills)
* 📊 Skill Gap Analysis
* 🧠 Intelligent Planning (Agentic decision-making)
* ⚡ Parallel Execution using LangGraph:

  * Roadmap Generator
  * Interview Topic Generator
  * Project Recommender
  * Resume Alignment Suggestions
  * Learning Resource Suggestions
* 🔗 Aggregation & Final Response Formatting
* 🧪 LangSmith Tracing & Observability
* ⚡ Ultra-fast dependency management with **uv**

---

## 🏗️ Architecture Overview

```id="graph-flow"
START
  ↓
input_parser
  ↓
jd_extractor
  ↓
candidate_profile_extractor
  ↓
skill_gap_analyzer
  ↓
planner
  ↓ (parallel fan-out)
 ├── roadmap_generator
 ├── interview_topic_generator
 ├── project_recommender
 ├── resume_alignment_suggester
 └── learning_resource_suggester
  ↓ (fan-in)
merge_results
  ↓
response_formatter
  ↓
END
```

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **Agent Framework:** LangGraph
* **Observability:** LangSmith
* **Package Manager:** uv
* **LLM Integrations:**

  * Google GenAI
  * Mistral
* **Validation:** Pydantic
* **Environment:** Python 3.11+

---

## 🧠 How It Works

1. Input Parsing → Normalize inputs
2. JD Extraction → Extract requirements
3. Candidate Profile → Structure resume
4. Skill Gap Analysis → Identify missing skills
5. Planner → Decide execution
6. Parallel Agents → Generate outputs
7. Merge + Format → Final response

---

## 🧪 LangSmith Integration (Tracing)

This project integrates **LangSmith** for:

* Tracing each LangGraph node execution
* Debugging agent flows
* Monitoring LLM performance

### 🔧 Setup

```env id="langsmith-env"
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=jobprep-ai-agent
```

---

## 📁 Project Structure

```id="project-structure"
app/
│
├── graph/
│   ├── builder.py
│   ├── state.py
│   └── nodes/
│
├── schemas/
│   ├── request.py
│   └── response.py
│
├── api/
│   └── routes.py
│
└── main.py
```

---

## 🚀 API Usage

### Endpoint

```id="endpoint"
POST /analyze-job
```

### Request Body

```json id="request-body"
{
  "job_description": "string",
  "user_skills": ["Node.js", "React"],
  "resume_text": "string",
  "prep_days": 30
}
```

### Response

```json id="response-body"
{
  "roadmap": "...",
  "projects": "...",
  "interview_topics": "...",
  "resume_suggestions": "...",
  "learning_resources": "..."
}
```

---

## 🛠️ Installation (Using uv)

### 1. Install uv

```bash id="install-uv"
curl -Ls https://astral.sh/uv/install.sh | sh
```

or (Mac):

```bash id="install-uv-brew"
brew install uv
```

---

### 2. Initialize Project (if needed)

```bash id="init"
uv init
```

---

### 3. Add Dependencies

```bash id="deps"
uv add fastapi langchain langchain-openai langchain-google-genai langchain-mistralai langgraph pydantic python-dotenv uvicorn
```

---

### 4. Create Virtual Environment & Sync

```bash id="sync"
uv venv
uv sync
```

---

### 5. Setup Environment Variables

```env id="env"
GOOGLE_API_KEY=your_key
MISTRAL_API_KEY=your_key

# LangSmith
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=jobprep-ai-agent
```

---

## ▶️ Run Server

```bash id="run"
uv run uvicorn app.main:app --reload
```

* API: http://127.0.0.1:8000
* Docs: http://127.0.0.1:8000/docs

---

## 🔍 Debugging with LangSmith

* Open LangSmith dashboard
* Select project: `jobprep-ai-agent`
* View:

  * Node execution traces
  * LLM calls
  * Latency and errors

---

## 🧩 Future Improvements

* 🔄 PostgreSQL / Neon memory integration
* 📁 Resume PDF upload
* ⚡ Streaming responses
* 🔐 Authentication
* 📊 User progress tracking

---

## 💡 Key Highlights

* ⚡ Uses **uv** (10-100x faster than pip)
* 🧠 Agentic workflow with LangGraph
* 🔍 Full observability via LangSmith
* 🧩 Modular and extensible architecture

---

## 📜 License

MIT License

---

## 🤝 Contribution

PRs are welcome. Open an issue for discussions.

---

## 👨‍💻 Author

Built as part of an **Agentic AI system design journey** focused on real-world job preparation.
