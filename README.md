# askdocs

A typed Python CLI that takes a question, calls a deployed LLM with proper auth, and streams the answer grounded in financial documents. Project 1 of 6 in a regulated-document AI platform — the same skeleton as repostat with one endpoint swap: the GitHub call replaced by an LLM call.

## Usage

```
uv run askdocs "What is a debt-to-income ratio?"
```

```
uv run askdocs "Summarize this loan application" --provider anthropic
```

```
uv run askdocs "What are the CFPB complaint categories?" --json
```

## Auth

Authentication follows the same pattern as repostat — secrets are read from environment variables, never hardcoded.

```
# .env
AZURE_ENDPOINT=https://your-foundry-project.openai.azure.com/
AZURE_DEPLOYMENT=gpt-4o
ANTHROPIC_API_KEY=your_key_here        # only needed with --provider anthropic
```

Azure uses `DefaultAzureCredential` — run `az login` for local development. No raw API keys in Azure.

## Setup

```
uv sync
az login
uv run askdocs --help
```

## Development

```
uv run pytest          # run tests
uv run ruff check src  # lint
uv run pyright src     # type check
```

## Stack

- [azure-ai-inference](https://pypi.org/project/azure-ai-inference/) — Azure model client with streaming
- [azure-identity](https://pypi.org/project/azure-identity/) — `DefaultAzureCredential` for keyless auth
- [anthropic](https://pypi.org/project/anthropic/) — direct Anthropic SDK for multi-provider support
- [typer](https://typer.tiangolo.com/) — type-hint-driven CLI
- [python-dotenv](https://pypi.org/project/python-dotenv/) — `.env` file loading
- [pytest](https://pytest.org/) — testing with mocked model clients

## What this project adds

- Calling an LLM SDK and printing a completion
- `DefaultAzureCredential` instead of a raw API key
- Streaming completions — tokens print as they are generated
- Lazy document chunking with `yield`
- Naive retrieval — keyword overlap used to ground answers in financial documents
- Multi-provider abstraction — `--provider azure` and `--provider anthropic` through the same code path

## Part of a series

| Project | What it adds |
|---------|-------------|
| repostat | Python language fundamentals: CLI, REST, typed models, error handling, secrets, tests |
| **askdocs** | LLM SDK, streaming, naive RAG, multi-provider |
| agentcli | Tool-calling agents, memory, asyncio, MCP |
| ragservice | FastAPI, embeddings, vector + hybrid search, citations, PII handling |
| extractor | Document intelligence, vision, batch processing, structured validation |
| evalkit | Evals, observability, cost tracking, tracing, Docker |
