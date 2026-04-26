import streamlit as st
import pandas as pd
import time

from parser import parse_jd
from matcher import compute_match_scores
from chat_agent import simulate_interest
from ranking import calculate_final_score

st.set_page_config(page_title="AI Talent Agent", layout="wide")

# Title
st.title("🤖 AI Talent Scouting & Engagement Agent")

# Sidebar filters
st.sidebar.header("🔎 Filters")

role_filter = st.sidebar.selectbox(
    "Select Role",
    ["All", "Data Analyst", "Java Developer", "Frontend Developer", "Cloud Engineer"]
)

min_exp = st.sidebar.slider("Minimum Experience (Years)", 0, 5, 0)

# Input section
st.subheader("📄 Enter Job Description")
jd_text = st.text_area("Paste job description here...", height=150)

find_btn = st.button("🚀 Find Candidates")

if find_btn:

    if not jd_text:
        st.warning("⚠️ Please enter a Job Description")
    else:
        df = pd.read_csv("data/candidates.csv")

        # Apply filters
        if role_filter != "All":
            df = df[df["role"] == role_filter]

        df = df[df["experience"] >= min_exp]

        if df.empty:
            st.error("❌ No candidates match selected filters")
        else:
            # Simulate AI processing
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)

            profiles = df["profile"].tolist()
            roles = df["role"].tolist()

            match_scores = compute_match_scores(jd_text, profiles, roles)

            results = []

            for i, row in df.iterrows():
                name = row["name"]
                match_score = match_scores[i]

                interest_text, interest_score = simulate_interest(name)
                final_score = calculate_final_score(match_score, interest_score)

                # Highlight matched skills
                matched_skills = []
                for skill in row["skills"].split():
                    if skill.lower() in jd_text.lower():
                        matched_skills.append(skill)

                explanation = f"Matched skills: {', '.join(matched_skills) if matched_skills else 'General match'}"

                results.append({
                    "Name": name,
                    "Role": row["role"],
                    "Experience": row["experience"],
                    "Location": row["location"],
                    "Match Score": round(match_score, 2),
                    "Interest": interest_text,
                    "Final Score": round(final_score, 2),
                    "Explanation": explanation
                })

            result_df = pd.DataFrame(results)
            result_df = result_df.sort_values(by="Final Score", ascending=False)

            st.success("✅ Candidates matched successfully!")

            # Top candidate highlight
            top = result_df.iloc[0]

            st.subheader("🏆 Top Candidate")
            col1, col2, col3 = st.columns(3)
            col1.metric("Name", top["Name"])
            col2.metric("Role", top["Role"])
            col3.metric("Final Score", top["Final Score"])

            st.write(f"💡 {top['Explanation']}")

            # Show table
            st.subheader("📊 Ranked Candidates")
            st.dataframe(result_df, use_container_width=True)

            # Expandable details
            with st.expander("🔍 View Detailed Candidate Info"):
                for _, row in result_df.iterrows():
                    st.write(f"**{row['Name']} ({row['Role']})**")
                    st.write(f"Experience: {row['Experience']} years")
                    st.write(f"Location: {row['Location']}")
                    st.write(f"Score: {row['Final Score']}")
                    st.write("---")
