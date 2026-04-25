from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_match_scores(jd_text, candidate_profiles):
    documents = [jd_text] + candidate_profiles

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    return scores
