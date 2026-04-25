import streamlit as st
import pandas as pd

from parser import parse_jd
from matcher import compute_match_scores
from chat_agent import simulate_interest
from ranking import calculate_final_score

# Page config
st.set_page_config(page_title="AI Talent Agent", layout="wide")

# Custom CSS 
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #2c3e50;
    }
    .card {
        padding: 20px;
        border-radius: 12px;
        background-color: white;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🤖 AI Talent Scouting & Engagement Agent</div>', unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([2, 1])

# LEFT SIDE - INPUT
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📄 Enter Job Description")
    jd_text = st.text_area("Paste JD here", height=150)
    find_btn = st.button("🔍 Find Candidates")
    st.markdown('</div>', unsafe_allow_html=True)

# RIGHT SIDE - INFO PANEL
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("ℹ️ How it works")
    st.write("""
    - Parses Job Description  
    - Matches candidates using AI similarity  
    - Simulates candidate interest  
    - Ranks candidates based on score  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# PROCESS
if find_btn:
    if not jd_text:
        st.warning("⚠️ Please enter a Job Description")
    else:
        df = pd.read_csv("data/candidates.csv")

        profiles = df["profile"].tolist()
        match_scores = compute_match_scores(jd_text, profiles)

        results = []

        for i, row in df.iterrows():
            name = row["name"]
            match_score = match_scores[i]

            interest_text, interest_score = simulate_interest(name)
            final_score = calculate_final_score(match_score, interest_score)

            explanation = f"{name} matches key skills from JD"

            results.append({
                "Name": name,
                "Match Score": round(match_score, 2),
                "Interest": interest_text,
                "Final Score": round(final_score, 2),
                "Explanation": explanation
            })

        result_df = pd.DataFrame(results)
        result_df = result_df.sort_values(by="Final Score", ascending=False)

        # SUCCESS MESSAGE
        st.success("✅ Candidates matched successfully!")

        # TOP CANDIDATE CARD 🔥
        top = result_df.iloc[0]

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🏆 Top Candidate")

        c1, c2, c3 = st.columns(3)
        c1.metric("Name", top["Name"])
        c2.metric("Match Score", top["Match Score"])
        c3.metric("Final Score", top["Final Score"])

        st.write(f"💡 {top['Explanation']}")
        st.markdown('</div>', unsafe_allow_html=True)

        # FULL TABLE
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📊 Ranked Candidates")

        st.dataframe(result_df, use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)
