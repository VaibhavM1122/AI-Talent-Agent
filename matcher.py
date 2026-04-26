from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_match_scores(jd_text, candidate_profiles, roles):
    """
    Computes similarity between job description and candidate profiles
    + boosts score if role matches
    """

    # Combine JD + profiles
    documents = [jd_text] + candidate_profiles

    # Convert text → TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Cosine similarity
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    jd_text_lower = jd_text.lower()
    final_scores = []

    for i, score in enumerate(similarity_scores):
        role = roles[i].lower()

        # 🎯 Role-based boost
        if role in jd_text_lower:
            score += 0.2

        # Normalize (max = 1)
        score = min(score, 1.0)

        final_scores.append(score)

    return final_scores
