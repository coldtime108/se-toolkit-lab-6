#!/usr/bin/env python3
"""
Simple CLI agent that calls an LLM and returns a JSON response.
Usage: uv run agent.py "Your question"
"""

import os
import sys
import json
import httpx
from dotenv import load_dotenv

# Load environment variables from .env.agent.secret
load_dotenv('.env.agent.secret')

LLM_API_KEY = os.getenv('LLM_API_KEY')
LLM_API_BASE = os.getenv('LLM_API_BASE', 'https://openrouter.ai/api/v1')
LLM_MODEL = os.getenv('LLM_MODEL', 'google/gemini-3-flash-preview')

def main():
    if len(sys.argv) < 2:
        print("Error: No question provided. Usage: agent.py \"Your question\"", file=sys.stderr)
        sys.exit(1)

    question = sys.argv[1]

    payload = {
        "model": LLM_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LLM_API_KEY}"
    }

    try:
        with httpx.Client(timeout=60.0) as client:
            response = client.post(
                f"{LLM_API_BASE}/chat/completions",
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            data = response.json()
    except Exception as e:
        print(f"Error calling LLM API: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        answer = data['choices'][0]['message']['content']
    except (KeyError, IndexError) as e:
        print(f"Error parsing LLM response: {e}", file=sys.stderr)
        sys.exit(1)

    result = {"answer": answer, "tool_calls": []}
    print(json.dumps(result))

if __name__ == "__main__":
    main()
