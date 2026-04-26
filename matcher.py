def compute_match_scores(jd_text, candidate_profiles, roles):
    jd_words = set(jd_text.lower().split())
    scores = []

    for i, profile in enumerate(candidate_profiles):
        profile_words = set(profile.lower().split())

        # simple word overlap
        common_words = jd_words.intersection(profile_words)
        score = len(common_words) / (len(jd_words) + 1)

        # role boost
        if roles[i].lower() in jd_text.lower():
            score += 0.2

        scores.append(min(score, 1.0))

    return scores
