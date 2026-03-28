from llm_engine import analyze_claim
from prompts import build_analysis_prompt
from rules import calculate_risk_score, decide_action


def run_agent(claim_data):
    prompt = build_analysis_prompt(claim_data)

    llm_output = analyze_claim(prompt)

    if "error" in llm_output:
        return llm_output

    risk_score = calculate_risk_score(claim_data, llm_output)
    action = decide_action(risk_score)

    llm_conf = llm_output.get("confidence_score", 50)
    try:
        llm_conf = int(llm_conf)
    except:
        llm_conf = 50

    final_confidence = (llm_conf + risk_score) // 2


    fraud_explanation = generate_fraud_explanation(llm_output, risk_score)


    return {
    "claim_type": llm_output.get("claim_type"),
    "risk_level": llm_output.get("risk_level"),
    "risk_score": risk_score,
    "confidence_score": final_confidence,
    "fraud_suspicion": llm_output.get("fraud_suspicion"),
    "recommended_action": action,
    "key_risk_factors": llm_output.get("key_risk_factors"),
    "reasoning": llm_output.get("reasoning"),
    "fraud_explanation": fraud_explanation
}

def generate_fraud_explanation(llm_output, risk_score):
    reasons = llm_output.get("key_risk_factors") or []

    if not reasons:
        base = "No strong fraud indicators detected"
    else:
        base = f"The claim shows risk indicators such as: {', '.join(reasons)}."


    if risk_score > 70:
        decision = "These combined factors significantly increase the likelihood of fraud, so the claim is flagged for manual review."
    elif risk_score > 40:
        decision = "These factors introduce moderate risk, so additional verification is recommended."
    else:
        decision = "The overall risk is low, and the claim appears safe to process."

    return base + " " + decision