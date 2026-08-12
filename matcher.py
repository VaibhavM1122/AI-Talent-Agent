def compute_match_scores(jd_text, candidate_profiles, roles):

    jd_words = set(jd_text.lower().split())

    scores = []


    for i, profile in enumerate(candidate_profiles):

        profile_words = set(profile.lower().split())


        # Find common skills/keywords
        common_words = jd_words.intersection(profile_words)


        # Calculate similarity
        if len(jd_words) > 0:
            score = len(common_words) / len(jd_words)

        else:
            score = 0


        candidate_role = roles[i].lower()
        jd_lower = jd_text.lower()


        # Role matching boost
        if candidate_role in jd_lower:

            score += 0.2

        else:

            # Reduce score for unrelated roles
            score *= 0.7


        # Keep score between 0 and 1
        scores.append(round(min(score, 1.0), 2))


    return scores
