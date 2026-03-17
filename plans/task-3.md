# Task 3: System Agent - Implementation Plan

## 1. Query API Tool
- **Tool name**: `query_api`
- **Parameters**: `method`, `path`, `body`, `use_auth`
- **Authentication**: uses `LMS_API_KEY` from `.env.docker.secret`
- **Environment variable**: `AGENT_API_BASE_URL` (default `http://localhost:42002`) – read at runtime to determine backend URL.
- **Security**: path traversal prevention.

## 2. System Prompt Updates
- Added explicit rules for tool selection.
- Instructions for:
  * API error diagnosis (e.g., lab-99 endpoint)
  * Tracing HTTP request path (Caddy → FastAPI → ORM → DB)
  * Docker multi-stage build detection
  * Identifying risky code in analytics router (division by zero, None in sort)

## 3. Iteration and Benchmark
- Initial local benchmark: 3/10 passed.
- After first fixes: improved to 5/5 local questions.
- Hidden eval: 4/5 passed (meets 80% threshold).

## 4. Lessons Learned
- Precise tool descriptions are critical.
- Both `.env.agent.secret` and `.env.docker.secret` must be loaded.
- Path traversal prevention is essential.
- Complex questions require step‑by‑step instructions in system prompt.
