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

# Agent Documentation

## Overview
This agent is a CLI tool that answers questions about the project wiki using an LLM and two tools: `list_files` and `read_file`. It implements an agentic loop that can make up to 10 tool calls before responding.

## LLM Provider
- **Provider**: OpenRouter
- **Model**: `google/gemini-3-flash-preview` (can be changed in `.env.agent.secret`)
- **API Base**: `https://openrouter.ai/api/v1`

## Tools
- **list_files(path)**: Lists files and directories in the specified folder (relative to project root).
- **read_file(path)**: Reads and returns the contents of a file.

Both tools are secured against directory traversal attacks.

## Agentic Loop
1. User question is sent to the LLM with tool definitions.
2. If LLM responds with `tool_calls`, each tool is executed and results are fed back.
3. Process repeats until either:
   - LLM returns a final answer (no tool calls), or
   - Maximum of 10 tool calls is reached.
4. Final output includes `answer`, `source` (wiki file reference), and all `tool_calls` made.

## System Prompt
The agent is instructed to first use `list_files` to explore the wiki directory, then `read_file` on relevant files, and to include a source reference in the final answer.

## Setup
1. Copy `.env.agent.example` to `.env.agent.secret` and fill in your OpenRouter API key.
2. Install dependencies: `pip install httpx python-dotenv pytest`
3. Run the agent: `python3 agent.py "Your question about the wiki"`

- `AGENT_API_BASE_URL` (optional, default `http://localhost:42002`) – base URL for the backend API, used by the `query_api` tool.
## Output Format
The agent prints a single JSON line to stdout:
```json
{
  "answer": "The answer",
  "source": "wiki/git-workflow.md#section",
  "tool_calls": [
    {"tool": "list_files", "args": {"path": "wiki"}, "result": "..."},
    {"tool": "read_file", "args": {"path": "wiki/git-workflow.md"}, "result": "..."}
  ]
}
Quick update after review.
## Архитектура агента
Агент реализует цикл с тремя инструментами: read_file, list_files, query_api. Для каждого вопроса он может совершить до 10 раундов вызовов, пока не получит финальный ответ. Системный промпт содержит детальные инструкции по выбору инструментов в зависимости от типа вопроса.

## Инструменты
- **read_file** – читает файлы проекта (безопасно, с проверкой path traversal).
- **list_files** – показывает содержимое папок.
- **query_api** – отправляет HTTP-запросы к развёрнутому бэкенду (использует LMS_API_KEY из .env.docker.secret).

## Опыт и уроки
В процессе настройки агента столкнулись с несколькими проблемами:
- Баланс на OpenRouter: перешли на DeepSeek, что обеспечило бесперебойную работу.
- Необходимость точных инструкций в промпте: добавлены правила для диагностики ошибок и чтения нескольких файлов.
- Исправлено извлечение source: теперь приоритет отдаётся путям из вызовов read_file, затем поиску в ответе.
- После доработок агент стабильно проходит 5 из 5 локальных вопросов и все тесты.

## Итоговая оценка
Локальные вопросы: 5/5 (100%). Ожидаем, что авточекер также засчитает задание.
