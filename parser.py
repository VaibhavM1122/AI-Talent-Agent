def parse_jd(jd_text):
    jd_text = jd_text.lower()

    skills = []
    skill_keywords = ["python", "sql", "power bi", "tableau", "excel", "machine learning"]

    for skill in skill_keywords:
        if skill in jd_text:
            skills.append(skill)

    return {
        "skills": skills,
        "raw_text": jd_text
    }
