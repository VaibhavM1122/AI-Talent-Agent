import streamlit as st
import pandas as pd
import time

from matcher import compute_match_scores


st.set_page_config(
    page_title="AI Talent Agent",
    layout="wide"
)

# Title
st.title("🤖 AI Talent Scouting & Engagement Agent")


# Sidebar Filters
st.sidebar.header("🔎 Filters")

role_filter = st.sidebar.selectbox(
    "Select Role",
    [
        "All",
        "Data Analyst",
        "Java Developer",
        "Frontend Developer",
        "Cloud Engineer",
        "Backend Developer",
        "DevOps Engineer",
        "AI Engineer"
    ]
)

min_exp = st.sidebar.slider(
    "Minimum Experience (Years)",
    0,
    5,
    0
)


# Job Description Input
st.subheader("📄 Enter Job Description")

jd_text = st.text_area(
    "Paste job description here...",
    height=150
)


find_btn = st.button("🚀 Find Candidates")


if find_btn:

    if not jd_text.strip():
        st.warning("⚠️ Please enter a Job Description")

    else:

        # Load dataset
        df = pd.read_csv("data/candidates.csv")


        # Apply role filter
        if role_filter != "All":
            df = df[df["role"] == role_filter]


        # Apply experience filter
        df = df[df["experience"] >= min_exp]


        # Reset index after filtering
        df = df.reset_index(drop=True)


        if df.empty:

            st.error("❌ No candidates match selected filters")


        else:

            # Loading animation
            progress = st.progress(0)

            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)


            # Candidate data
            profiles = df["profile"].tolist()
            roles = df["role"].tolist()


            # Calculate Match Score
            match_scores = compute_match_scores(
                jd_text,
                profiles,
                roles
            )


            results = []


            for i, row in df.iterrows():

                match_score = match_scores[i]


                # Find matched skills
                matched_skills = []

                for skill in row["skills"].split():

                    if skill.lower() in jd_text.lower():
                        matched_skills.append(skill)


                explanation = (
                    f"Matched skills: {', '.join(matched_skills)}"
                    if matched_skills
                    else "General match"
                )


                results.append({

                    "Name": row["name"],

                    "Role": row["role"],

                    "Experience": row["experience"],

                    "Location": row["location"],

                    "Match Score": round(match_score, 2),

                    "Explanation": explanation

                })


            # Convert result to dataframe
            result_df = pd.DataFrame(results)


            # Sort by Match Score
            result_df = result_df.sort_values(
                by="Match Score",
                ascending=False
            )


            st.success(
                "✅ Candidates matched successfully!"
            )


            # Top Candidate
            top = result_df.iloc[0]


            st.subheader("🏆 Top Candidate")


            col1, col2, col3 = st.columns(3)


            col1.metric(
                "Name",
                top["Name"]
            )


            col2.metric(
                "Role",
                top["Role"]
            )


            col3.metric(
                "Match Score",
                top["Match Score"]
            )


            st.write(
                f"💡 {top['Explanation']}"
            )


            # Results Table
            st.subheader(
                "📊 Ranked Candidates"
            )


            st.dataframe(
                result_df,
                width="stretch",
                hide_index=True
            )


            # Details
            with st.expander(
                "🔍 View Detailed Candidate Info"
            ):

                for _, row in result_df.iterrows():

                    st.write(
                        f"### {row['Name']} ({row['Role']})"
                    )

                    st.write(
                        f"Experience: {row['Experience']} years"
                    )

                    st.write(
                        f"Location: {row['Location']}"
                    )

                    st.write(
                        f"Match Score: {row['Match Score']}"
                    )

                    st.write(
                        row["Explanation"]
                    )

                    st.divider()
