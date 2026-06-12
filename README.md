# 🤖 AgentHire AI

An AI-powered Resume Screening and ATS Analysis System built using **Python, Streamlit, and Large Language Models (LLMs)**. The application intelligently analyzes resumes against job descriptions by extracting technical skills, calculating ATS match scores, and generating AI-powered recruiter feedback using a modular agent-based architecture.

---

# 📌 Overview

AgentHire AI automates the initial resume screening process by leveraging Large Language Models for skill extraction and candidate evaluation.

The system accepts a PDF resume and a job description, extracts technical skills from both documents using an LLM, compares the extracted skills, calculates an ATS compatibility score, identifies matching and missing skills, and generates recruiter-style feedback.

The project demonstrates practical applications of AI, prompt engineering, modular software design, and Python development in recruitment automation.

---

# 🚀 Features

- 📄 PDF Resume Parsing
- 🧠 LLM-powered Skill Extraction
- 🎯 ATS Match Score Calculation
- ✅ Matching Skills Detection
- ❌ Missing Skills Identification
- 🤖 AI Recruiter Feedback Generation
- 🏗️ Modular Agent-based Architecture
- 🌐 Interactive Streamlit User Interface

---

# 🏛️ System Architecture

```
                  Resume PDF
                      │
                      ▼
               ParserAgent
                      │
                      ▼
                PDFService
                      │
                      ▼
                 Resume Text
                      │
                      ▼
          SkillAgent (LLM Extraction)
                      │
                      ▼
                Resume Skills

------------------------------------------------

               Job Description
                      │
                      ▼
          SkillAgent (LLM Extraction)
                      │
                      ▼
                   JD Skills

------------------------------------------------

                      │
                      ▼
              ComparisonAgent
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
   Matching Skills         Missing Skills
                      │
                      ▼
                 ATSScore Model
                      │
                      ▼
              FeedbackAgent
                      │
                      ▼
                 LLMService
                      │
                      ▼
              Large Language Model
                      │
                      ▼
         AI Recruiter Feedback Output
```

---

# 🛠️ Tech Stack

- Python
- Streamlit
- Groq API
- Llama 3 Large Language Model
- PyMuPDF (fitz)
- Git & GitHub

---

# 📂 Project Structure

```
AgentHire-AI/

│

├── agents/
│   ├── parser_agent.py
│   ├── skill_agent.py
│   ├── comparison_agent.py
│   └── feedback_agent.py

│

├── services/
│   ├── pdf_service.py
│   └── llm_service.py

│

├── models/
│   └── ats_score.py

│

├── app.py

├── requirements.txt

├── .env

└── README.md
```

---

# ⚙️ Workflow

1. User uploads a PDF resume.
2. User pastes a job description.
3. ParserAgent extracts resume text using PDFService.
4. SkillAgent uses an LLM to extract technical skills from both the resume and the job description.
5. ComparisonAgent identifies matching and missing skills.
6. ATSScore calculates the resume compatibility percentage.
7. FeedbackAgent generates recruiter-style feedback.
8. Streamlit displays the complete analysis to the user.

---

# 💡 Design Principles

The application follows a modular agent-based architecture where each component has a single responsibility.

- ParserAgent → Resume parsing
- PDFService → PDF text extraction
- SkillAgent → AI-powered skill extraction
- ComparisonAgent → Skill comparison
- ATSScore → Resume scoring logic
- FeedbackAgent → Prompt engineering and recruiter feedback generation
- LLMService → Communication with the Large Language Model

This separation improves maintainability, scalability, and allows individual components to be replaced or upgraded independently.

---

# 🎯 ATS Score Logic

The ATS score is calculated based on the proportion of required job description skills found in the candidate's resume.

```
ATS Score =

(Number of Matching Skills / Total Required JD Skills) × 100
```

This provides a transparent and interpretable measure of resume-job compatibility.

---

# 🔮 Future Enhancements

- Semantic similarity using embeddings
- Vector database integration (Pinecone / Chroma)
- Multi-agent orchestration using CrewAI
- Interview question generation
- Resume improvement recommendations
- Learning roadmap generation
- Multi-LLM provider support (Claude, OpenAI, Groq)

---

# 📚 Key Learnings

- Large Language Model Integration
- Prompt Engineering
- Modular Software Architecture
- Agent-based System Design
- ATS Resume Analysis
- Python Application Development
- Streamlit UI Development
- Git & GitHub Version Control

---

# 📷 Demo

Upload a PDF resume and paste a job description to receive:

- Extracted Technical Skills
- Matching Skills
- Missing Skills
- ATS Match Score
- AI Recruiter Feedback

---

# 🤝 Contributing

Contributions, feature requests, and suggestions are welcome.

Feel free to fork the repository and submit pull requests.

---

# 📄 License

This project is developed for educational and learning purposes.
