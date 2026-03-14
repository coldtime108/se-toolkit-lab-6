# Agent Documentation

## Overview
This agent is a simple CLI tool that sends a user question to an LLM and returns a JSON response with the answer and an empty tool calls array.

## LLM Provider
- **Provider**: OpenRouter
- **Model**: `google/gemini-3-flash-preview` (can be changed in `.env.agent.secret`)
- **API Base**: `https://openrouter.ai/api/v1`

## Setup
1. Copy `.env.agent.example` to `.env.agent.secret` and fill in your OpenRouter API key.
2. Install dependencies: `uv add httpx python-dotenv` and `uv add --dev pytest`.
3. Run the agent: `uv run agent.py "Your question"`

## Output Format
The agent prints a single JSON line to stdout:
```json
{"answer": "The answer", "tool_calls": []}
