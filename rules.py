def calculate_risk_score(claim_data, llm_output):
    score = 0

    amount = claim_data["amount"]
    history = claim_data["history"].lower()

    if amount > 100000:
        score += 30
    elif amount > 50000:
        score += 20

    if "previous claims" in history:
        score += 20

    if llm_output.get("fraud_suspicion") == "Yes":
        score += 30


    return min(score, 100)


def decide_action(score):
    if score >= 70:
        return "Manual Review"
    elif score >= 40:
        return "Request Additional Documents"
    else:
        return "Auto Approve"