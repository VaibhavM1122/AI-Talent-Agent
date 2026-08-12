def parse_jd(jd_text):

    jd_text = jd_text.lower()

    skills = []

    skill_keywords = [
        "python",
        "java",
        "javascript",
        "react",
        "angular",
        "html",
        "css",
        "spring",
        "spring boot",
        "microservices",
        "sql",
        "mysql",
        "oracle",
        "power bi",
        "tableau",
        "excel",
        "machine learning",
        "deep learning",
        "tensorflow",
        "aws",
        "azure",
        "docker",
        "kubernetes",
        "git"
    ]


    for skill in skill_keywords:

        if skill in jd_text:
            skills.append(skill)


    return {
        "skills": skills,
        "raw_text": jd_text
    }
