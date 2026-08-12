# 🤖 AI-Powered Talent Scouting & Engagement Agent

## Overview

This project is an AI-driven recruitment assistant that automates candidate discovery and matching. It takes a Job Description (JD) as input, analyzes requirements, identifies relevant candidates from a dataset, and generates a ranked shortlist based on candidate-job compatibility.

The system helps recruiters reduce manual screening effort by providing fast, explainable candidate recommendations.

---

## Problem Statement

Recruiters spend significant time manually reviewing candidate profiles and matching them with job requirements.

This system reduces recruitment effort by:

- Automatically analyzing job descriptions
- Extracting relevant skills and requirements
- Matching candidates using text similarity
- Ranking candidates based on Match Score
- Providing explainable matching results

---

# Key Features

## 📄 Job Description Parsing

- Analyzes job descriptions
- Extracts important skills and keywords
- Supports multiple roles:
  - Data Analyst
  - Java Developer
  - Frontend Developer
  - Cloud Engineer
  - Backend Developer
  - DevOps Engineer

---

## 🔍 Candidate Matching

- Uses lightweight text similarity matching
- Compares job requirements with candidate profiles
- Applies role-based score boosting
- Matches candidates based on:
  - Skills
  - Profile information
  - Job role relevance

---

## 📊 Match Score Ranking

Each candidate receives a Match Score based on:

- Number of matching keywords
- Skill overlap
- Role relevance

Candidates are sorted from highest to lowest Match Score.

---

## 🎨 Interactive UI

Built using Streamlit:

- Job description input
- Role filter
- Experience filter
- Ranked candidate table
- Top candidate highlight
- Matched skill explanation

---

## System Architecture

User Input (Job Description)
↓
JD Processing Module
↓
Candidate Dataset (CSV)
↓
Matching Engine
(Text Similarity + Role Boosting)
↓
Match Score Calculation
↓
Candidate Ranking
↓
Streamlit Dashboard

---

#  Tech Stack

* **Python**
* **Streamlit** (Frontend UI)
* **Pandas** (Data Handling)

---

##  Project Structure

```
AI-Talent-Agent/

│── app.py
│── parser.py
│── matcher.py
│── data/
│ └── candidates.csv
│── README.md
│── requirements.txt
```

---

##  How to Run Locally

1. Clone the repository:

```
git clone https://github.com/VaibhavM1122/AI-Talent-Agent.git
cd AI-Talent-Agent
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
streamlit run app.py
```

4. Open in browser:

```
http://localhost:8501
```
---

## Sample Input

```
Looking for Java Developer with Spring Boot and Microservices experience.
```

---

## Sample Output

* Student Name 
* Ranked list of candidates
* Match Score
* Explanation of matching

---

## Example Use Case

* Input: Frontend Developer JD
* Output: Frontend candidates ranked highest
* System dynamically adapts to different job roles

---

##  Key Highlight

✔ Supports multiple job roles
✔ Lightweight and fast (no heavy ML dependencies)
✔ Explainable matching results
✔ Interactive recruiter-friendly UI

---

## 👨‍💻 Author

**Vaibhav Mahale**

* 💼 LinkedIn: [View Profile](https://www.linkedin.com/in/vaibhavm1122/)
