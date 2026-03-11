[README.md](https://github.com/user-attachments/files/25699133/README.md)
# 👋 Hi, I'm Apirith Sothea

**Full-stack developer building AI-native tools that solve real problems.**  
I focus on shipping products that work — not demos, not prototypes. Real tools with real impact.

🌐 **Portfolio:** [https://apirithporfolio.netlify.app/](https://apirithporfolio.netlify.app/)  
💼 **LinkedIn:** [linkedin.com/in/apirith-sothea](https://www.linkedin.com/in/apirith-sothea/)  
📧 **Email:** apiriths@gmail.com

---

## 🚀 Featured Projects

### 1. ATS Resume Optimizer

> *Most resumes get rejected before a human sees them. This tool fixes that.*

A full-stack web tool that helps job seekers beat automated hiring filters (ATS systems). Users upload their resume, paste a job description, and Claude AI rewrites the resume with matched keywords and XYZ-format bullets — then returns a clean, downloadable file in the same format.

**The Problem it solves:** Recruiters use Applicant Tracking Systems that auto-reject resumes missing specific keywords. Most job seekers don't know how to tailor their resume correctly — or don't have time to do it for every application.

**How it works:**
1. User uploads resume (PDF or Word doc)
2. User pastes the job description
3. Claude AI analyzes both and rewrites the resume with matched keywords and strong XYZ-format bullets
4. User downloads the optimized file in the same format they uploaded

**Tech Stack:**

| Layer | Technology |
|---|---|
| Frontend | Next.js |
| Backend | FastAPI (Python) |
| AI Engine | Claude API (Anthropic) |
| Output | Rebuilt DOCX / PDF |

**Key Design Decisions:**
- ✅ Fully stateless — no login required, no files stored on the server
- ✅ Output is honest and human-readable, not just keyword-stuffed
- ✅ Returns the file in the same format it was uploaded

---

### 2. AwardIQ

> *Researching award nominations is time-consuming and easy to fall behind on. AwardIQ automates it.*

A lightweight, browser-based tool that uses Claude AI to automate business award nomination research. You describe what you're looking for, it searches and returns structured results — award name, deadline, cost, eligibility, and source — all filtered to what's actually relevant to your company.

**The Problem it solves:** PR teams and businesses miss award nomination deadlines constantly. The research is repetitive and relies entirely on one person manually checking dozens of sources.

**What it does:**
- 🔍 Searches for real, current award nominations on demand
- 📋 Tracks submissions with status updates and notes
- 🔔 Monitors specific URLs for new openings and deadline changes
- 📤 Exports your tracker to CSV for reporting

**Tech Stack:**

| Layer | Technology |
|---|---|
| Interface | HTML / JavaScript |
| AI Engine | Claude API (Anthropic) |
| Storage | Local (browser only) |
| Infrastructure | None — two files, no backend |

**Key Design Decisions:**
- ✅ Zero backend — runs entirely in your browser using VS Code and a Claude API key
- ✅ All data stays local on your machine — no subscriptions, no database
- ✅ Two files total — dead simple to set up and run

**Roadmap / Bigger Vision:**  
The MVP proves the concept. The full product adds 24/7 automated crawlers, email alerts, a database, and multi-user access — making it a standalone SaaS tool that PR agencies and corporate communications teams would pay a monthly subscription for. Natural acquisition targets include Cision, Meltwater, and Sprinklr.

---

## 🛠️ Skills & Technologies

**Languages**
- Python · JavaScript · HTML · CSS

**Frameworks & Tools**
- Next.js · FastAPI · Claude API (Anthropic)

**Concepts**
- AI-native product development · Full-stack architecture · Stateless API design · Browser-based tooling

---
### 3. Redacto

A full-stack document redaction platform that uses Claude AI to detect and permanently remove PII from PDFs and Word documents. Upload a file, choose what to redact, download a clean version with true black-box redactions, not blurs.
The Problem it solves: Legal teams, HR departments, and healthcare providers spend hours manually scrubbing sensitive data from documents before sharing them. One missed detail — a social security number buried on page 14, a name in a header — can mean a HIPAA violation or a lawsuit.
What it does:

-  🔍 Detects 30+ PII categories using Claude AI names, SSNs, medical conditions, financial data, and more
-  ⬛ Applies permanent black-box redactions (data is destroyed, not hidden behind a blur)
-  🏷️ Supports labeled redaction mode replace names with [NAME], dates with [DATE]
-  📁 Runs batch mode drop 100+ documents, walk away, download finished outputs
-  🎛️ Saves named Redaction Profiles for repeatable workflows (e.g. "HIPAA Profile", "HR Review Profile")
-  ✏️ Manual Studio editor for post-redaction fine-tuning click to restore or add redactions

**Tech Stack:** 
| Layer | Technology |
|---|---|
| Frontend | React + Vite |
| Backend | FastAPI (Python) |
| AI Engine | Claude API (Anthropic) |
| PDF Engine | PyMuPDF |
| DOCX Engine | python-docx |
| Batch Queue | Celery + Redis |

**Key Design Decisions:**
-  ✅ Redactions are permanent PyMuPDF destroys the underlying data at the pixel level, not just visually
-  ✅ Claude handles the ambiguity context-aware detection catches "Dr. Martinez" as a name even when it appears mid-sentence
-  ✅ Profile system means compliance teams configure once and apply consistently across every document
-  ✅ Batch mode is fire-and-forget no babysitting a redaction queue

---

## 📌 What I'm Building Toward

Both of my current projects are designed to grow:

- **ATS Optimizer** → can expand into interview prep, LinkedIn profile optimization, and cover letter generation
- **AwardIQ** → can expand into grants, fellowships, speaking opportunities, and a full SaaS platform with automated monitoring

I'm interested in building AI tools that automate repetitive, high-value work — the kind of tasks that are currently done manually, at scale, by people who have better things to do.

---

## 📬 Let's Connect

If you're interested in collaborating, investing, or just want to talk about what I'm building:

- 🌐 [Portfolio](https://apirithporfolio.netlify.app/)
- 💼 [LinkedIn](https://www.linkedin.com/in/apirith-sothea/)
- 📧 apiriths@gmail.com
