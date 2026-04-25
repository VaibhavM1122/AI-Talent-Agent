import random

def simulate_interest(candidate_name):
    responses = ["Yes", "Maybe", "No"]
    response = random.choice(responses)

    if response == "Yes":
        score = 1.0
    elif response == "Maybe":
        score = 0.5
    else:
        score = 0.0

    return response, score
