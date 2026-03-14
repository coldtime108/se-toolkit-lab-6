# Task 1: Call an LLM from Code - Plan

## LLM Provider and Model
- **Provider**: OpenRouter
- **Model**: `google/gemini-3-flash-preview`
- **API Base**: `https://openrouter.ai/api/v1`
- **Authentication**: API key stored in `.env.agent.secret` as `LLM_API_KEY`

## Agent Structure
The agent will be implemented in `agent.py` and will:
1. Read configuration from `.env.agent.secret` (using `python-dotenv`).
2. Accept a question as a command-line argument.
3. Construct a chat completion request with a minimal system prompt (e.g., "You are a helpful assistant.").
4. Send the request to the LLM API using `httpx` (or `requests`).
5. Parse the response and extract the answer.
6. Output a single JSON line: `{"answer": "...", "tool_calls": []}` to stdout.
7. Print any debug or progress information to stderr.
8. Exit with code 0 on success, non-zero on failure.

## Error Handling
- If the question is missing, print error to stderr and exit with code 1.
- If the API call fails, print error to stderr and exit with code 1.
- If the response is malformed, print error and exit with code 1.

## Testing
- One regression test will be created (e.g., `tests/test_agent.py`) that runs `agent.py` as a subprocess with a simple question, checks that stdout is valid JSON and contains `answer` and `tool_calls` fields.
- The test will be runnable via `pytest`.

## Dependencies
- `python-dotenv` for loading environment variables.
- `httpx` for HTTP requests (or `requests`).
- `pytest` for testing.

## Implementation Steps
1. Create `agent.py` with basic argument parsing.
2. Load environment variables from `.env.agent.secret`.
3. Implement API call to OpenRouter.
4. Process response and output JSON.
5. Write the test.
6. Update `pyproject.toml` with new dependencies.
