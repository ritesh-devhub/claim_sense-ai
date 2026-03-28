from agent import run_agent

if __name__ == "__main__":
    claim = {
  "claim_text": "Accident occurred, all documents perfectly available, no discrepancies.",
  "amount": 150000,
  "history": "No claims ever"
}
    result = run_agent(claim)

    print("\n=== CLAIM RESULT ===")
    for key, value in result.items():
        print(f"{key}: {value}")