def build_analysis_prompt(claim_data):
    return f"""
You are a senior insurance claims analyst in India.

Analyze the claim and return STRICT JSON.

Include:
- claim_type
- risk_level (Low/Medium/High)
- fraud_suspicion (Yes/No)
- confidence_score (0-100)
- key_risk_factors (list of reasons)
- reasoning (short explanation)

Claim Description: {claim_data['claim_text']}
Claim Amount: {claim_data['amount']}
User History: {claim_data['history']}
"""