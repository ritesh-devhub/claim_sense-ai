import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ServerError, ClientError
import streamlit as st


def get_client():
    api_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        return None 

    return genai.Client(api_key=api_key)


def analyze_claim(prompt):
    client = get_client()

    if client is None:
        return fallback_response()

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
                response_mime_type="application/json"
            )
        )
        return json.loads(response.text)
    
    except (ServerError, ClientError) as e:
        print(f"⚠️ Gemini API Error: {e}")

        return fallback_response()
    
    except Exception as e:
        print(f"⚠️ Unexpected Error: {e}")

        return fallback_response()


def fallback_response():
    return {
        "claim_type": "Auto Insurance",
        "risk_level": "Medium",
        "fraud_suspicion": "No",
        "confidence_score": 60,
        "key_risk_factors": ["Fallback mode"],
        "reasoning": "Mock response due to API limit",
        "fallback": True
    }
