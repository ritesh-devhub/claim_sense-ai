import streamlit as st
from agent import run_agent

st.set_page_config(page_title="ClaimSense AI", layout="wide")

st.title("🧠 ClaimSense AI — Insurance Claims Triage Agent")
st.markdown("Analyze insurance claims with AI + rule-based reasoning")

# INPUT SECTION
st.sidebar.header("Input Claim Data")

claim_text = st.sidebar.text_area(
    "Claim Description",
    "Car accident with minor injuries"
)

amount = st.sidebar.number_input("Claim Amount", value=50000)

history = st.sidebar.text_input(
    "User History",
    "No previous claims"
)

run_button = st.sidebar.button("Analyze Claim")

# MAIN OUTPUT 
if run_button:
    claim_data = {
        "claim_text": claim_text,
        "amount": amount,
        "history": history
    }

    result = run_agent(claim_data)

    if result.get("fallback"):
        st.warning("⚠️ Running in fallback mode (API limit reached)")

    if "error" in result:
        st.error(result)
    else:
        st.success("✅ Analysis Complete")

        col1, col2, col3 = st.columns(3)

        # METRICS 
        with col1:
            st.metric("Risk Score", result["risk_score"])

        with col2:
            st.metric("Confidence", result["confidence_score"])

        with col3:
            st.metric("Fraud Suspicion", result["fraud_suspicion"])

        st.divider()

        # DETAILS 
        st.subheader("📊 Claim Analysis")

        st.write(f"**Claim Type:** {result['claim_type']}")
        st.write(f"**Risk Level:** {result['risk_level']}")
        st.write(f"**Recommended Action:** {result['recommended_action']}")

        st.divider()

        # RISK FACTORS 
        st.subheader("⚠️ Key Risk Factors")

        if result["key_risk_factors"]:
            for factor in result["key_risk_factors"]:
                st.write(f"- {factor}")
        else:
            st.write("No major risk factors")

        st.divider()

        # EXPLANATION 
        st.subheader("🧾 Fraud Explanation")
        st.info(result["fraud_explanation"])

        st.subheader("🧠 AI Reasoning")
        st.write(result["reasoning"])