# ClaimSense — Insurance Claims Triage System

An intelligent system that analyzes insurance claims using advanced reasoning and rule-based logic to classify risk, detect fraud signals, and recommend actions.

## Overview

ClaimSense simulates how modern insurance systems triage claims:

* Understands claim context through natural language processing
* Calculates risk using deterministic rules
* Re-evaluates low-confidence decisions through iterative analysis
* Generates explainable outputs for transparency
* Provides an interactive user interface via Streamlit

## Features

### Intelligent Analysis Engine

Uses Google Gemini API to:
* Classify claim type
* Detect fraud signals
* Extract key risk factors

### Rule-Based Risk Engine

* Combines structured logic with language model output
* Ensures reliability and control
* Generates a final risk score (0–100)

### Iterative Re-Evaluation

* Automatically reprocesses claims if confidence is low
* Improves decision quality without manual intervention

### Explainable Decision-Making

Separates outputs into:
* **Key Risk Factors** — raw signals identified
* **Fraud Explanation** — reasoning behind decisions

Makes outputs interpretable and actionable for claims adjusters.

### Fault-Tolerant Design

* Handles API failures (quota limits, downtime)
* Uses fallback responses to ensure system continuity

### Interactive Dashboard

Built with Streamlit:
* Input claim details
* View risk metrics and scores
* Understand reasoning visually

## Project Structure

```
ClaimSense/
│
├── app.py              # Streamlit UI
├── main.py             # CLI runner
│
├── agent.py            # Core agent logic
├── llm_engine.py       # Gemini API + fallback
├── rules.py            # Risk scoring logic
├── prompts.py          # Prompt templates
│
├── .env                # API key
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone <your-repo-link>
cd claimsense
pip install -r requirements.txt
```

## Setup API Key

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

## Usage

### Streamlit Interface

```bash
streamlit run app.py
```

### CLI Demo

```bash
python main.py
```

## How It Works

### 1. Input
User provides:
* Claim description
* Claim amount
* User history

### 2. Language Model Reasoning
Gemini analyzes:
* Claim type
* Risk level
* Fraud suspicion
* Key risk factors

### 3. Rule Engine
Custom logic calculates:
* Risk score (0–100)

### 4. Iterative Loop
If confidence is low:
* System re-evaluates claim
* Improves final output

### 5. Final Output

```json
{
  "risk_score": 78,
  "confidence_score": 72,
  "fraud_suspicion": "Yes",
  "recommended_action": "Manual Review",
  "fraud_explanation": "..."
}
```

## Limitations

* Depends on external API (rate limits may apply)
* Model outputs may vary slightly between runs
* Rule engine is simplified and can be extended

## Future Improvements

* Add claim history database
* Implement multi-agent reasoning architecture
* Enhanced dashboard analytics
* File upload support (PDF claims)
* Deployment with REST API backend

## Key Technical Highlights

* Hybrid system combining language models with rule-based logic
* Iterative workflows with re-evaluation loops
* Robust error handling for API failures and rate limits
* Explainable decision-making for regulatory compliance
* End-to-end product implementation

## Author

**Ritesh**  
Aspiring AI/ML Engineer | Data Science Enthusiast

## Contributing

If you found this project useful, consider giving it a star and connecting on LinkedIn!
