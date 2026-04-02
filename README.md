# 🚀 JobPrep AI Agent

An **Agentic AI-powered job preparation assistant** built using a **multi-agent DAG architecture with parallel fan-out/fan-in execution**, enabling scalable and modular LLM workflows.

Built with **LangGraph + FastAPI**, enhanced with **LangSmith tracing** for observability and debugging, and managed using **uv** for ultra-fast Python dependency management.

---

## 📌 Features

* 🔍 Job Description Parsing
* 👤 Candidate Profile Extraction (resume + skills)
* 📊 Skill Gap Analysis
* 🧠 Planning Node (task decomposition for parallel execution)

### ⚡ Parallel Multi-Agent Execution

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

```
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

## 🤖 Why Multi-Agent Architecture?

Instead of relying on a single LLM call, this system decomposes the problem into **specialized agents**:

* Improves accuracy through task isolation
* Enables parallel execution for faster responses
* Makes the system modular, scalable, and maintainable

The system follows a **DAG-based orchestration pattern** using LangGraph.

---

## 🧠 How It Works

1. **Input Parsing** → Normalize user input
2. **JD Extraction** → Extract structured job requirements
3. **Candidate Profiling** → Structure resume into usable data
4. **Skill Gap Analysis** → Identify missing skills
5. **Planner** → Decompose tasks for execution
6. **Parallel Agents** → Generate outputs concurrently
7. **Merge + Format** → Final structured response

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **Agent Framework:** LangGraph
* **LLM Integrations:** Google GenAI, Mistral
* **Prompt Engineering:** LangChain (ChatPromptTemplate)
* **Validation:** Pydantic
* **Observability:** LangSmith
* **Package Manager:** uv
* **Environment:** Python 3.11+

---

## 🧩 Prompt Engineering

Each agent uses structured prompting via:

* LangChain `ChatPromptTemplate`
* Role-based prompts for task specialization
* Structured output parsing (JSON)

This ensures:

* Consistent outputs
* Reduced hallucination
* Better control over LLM behavior

---

## 🧪 LangSmith Integration (Tracing)

This project integrates **LangSmith** for:

* Tracing each LangGraph node execution
* Debugging agent workflows
* Monitoring LLM performance and latency

### 🔧 Setup

```
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=jobprep-ai-agent
```

---

## 🚀 API Usage

### Endpoint

```
POST /analyze-job
```

### Request Body

```
{
  "job_description": "string",
  "user_skills": ["Node.js", "React"],
  "resume_text": "string",
  "prep_days": 30
}
```

### Response

```
{
  "match_score": 75,
  "skill_gaps": ["Redis", "System Design"],
  "roadmap": "...",
  "recommended_projects": [...],
  "interview_topics": [...],
  "resume_suggestions": [...],
  "learning_resources": [...]
}
```

---

## 🐳 Docker Deployment

### Build Image

```
docker build -t sant99/jobprep-ai-agent .
```

### Run Container

```
docker run --rm --env-file .env -p 8888:8000 sant99/jobprep-ai-agent        
```

### Notes

* Uses Python 3.11 slim image
* Dependencies installed via `uv`
* Optimized for fast builds and smaller image size

---

## 🛠️ Installation (Using uv)

### 1. Install uv

```
curl -Ls https://astral.sh/uv/install.sh | sh
```

or (Mac):

```
brew install uv
```

### 2. Initialize Project (if needed)

```
uv init
```

### 3. Add Dependencies

```
uv add fastapi langchain langchain-openai langchain-google-genai langchain-mistralai langgraph pydantic python-dotenv uvicorn
```

### 4. Create Virtual Environment & Sync

```
uv venv
uv sync
```

### 5. Setup Environment Variables

```
GOOGLE_API_KEY=your_key
MISTRAL_API_KEY=your_key

LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=jobprep-ai-agent
```

---

## ▶️ Run Server

```
uv run uvicorn app.main:app --reload
```

* API: http://127.0.0.1:8000
* Docs: http://127.0.0.1:8000/docs

---

## 🔍 Debugging with LangSmith

* Open LangSmith dashboard
* Select project: `jobprep-ai-agent`
* Inspect:

  * Node execution traces
  * LLM calls
  * Latency and errors

---


## 🏷️ Tags

* Multi-Agent Systems
* LangGraph
* DAG Orchestration
* LLM Applications
* FastAPI
* AI Backend Engineering

---

## 👨‍💻 Author

Built as part of an **Agentic AI system design journey** focused on real-world job preparation.
