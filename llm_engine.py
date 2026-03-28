import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ServerError, ClientError

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_claim(prompt):

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