# 🤖 AI-Powered Talent Scouting & Engagement Agent

##  Overview

This project is an AI-driven recruitment assistant that automates talent discovery, engagement, and ranking. It takes a Job Description (JD) as input, identifies the most relevant candidates, simulates their interest, and generates a ranked shortlist based on match quality and engagement level.

---

##  Problem Statement

Recruiters spend significant time manually screening profiles and assessing candidate interest. This system reduces that effort by:

* Automatically analyzing job descriptions
* Matching candidates using intelligent text similarity
* Simulating engagement to estimate interest
* Generating a ranked shortlist for faster decision-making

---

##  Key Features

###  Job Description Parsing

* Extracts key skills and requirements from JD
* Supports multiple roles (Data Analyst, Java Developer, Frontend, Cloud, etc.)

###  Candidate Matching

* Lightweight **text similarity matching (no heavy ML dependencies)**
* Role-based score boosting
* Matches based on skills, profile, and role relevance

###  Engagement Simulation

* Simulates candidate responses (Yes / Maybe / No)
* Converts responses into an **Interest Score**

###  Smart Ranking System

Final Score is calculated as:

```
Final Score = 0.7 × Match Score + 0.3 × Interest Score
```

###  Interactive UI

* Built using Streamlit
* Sidebar filters (role, experience)
* Real-time candidate ranking
* Highlighted top candidate
* Explainable outputs (matched skills)

---

##  System Architecture

```
User Input (Job Description)
        ↓
JD Processing Module
        ↓
Matching Engine (Text Similarity + Role Boosting)
        ↓
Engagement Simulation (Interest Score)
        ↓
Ranking Engine (Final Score Calculation)
        ↓
Interactive UI (Streamlit Dashboard)
```

---

##  Tech Stack

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
│── chat_agent.py
│── ranking.py
│── data/
│     └── candidates.csv
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

##  Sample Input

```
Looking for Java Developer with Spring Boot and Microservices experience.
```

---

##  Sample Output

* Ranked list of candidates
* Match Score
* Interest Score
* Final Score
* Explanation of matching

---

##  Example Use Case

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

##  Future Improvements

* Integration with real job portals (LinkedIn, Naukri)
* Real-time chatbot for candidate interaction
* LLM-based JD parsing (GPT/Gemini)
* Advanced semantic matching using embeddings

---

## 👨‍💻 Author

**Vaibhav Mahale**

* 💼 LinkedIn: [View Profile](https://www.linkedin.com/in/vaibhavm1122/)
