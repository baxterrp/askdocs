import os
from typing import Iterator
import anthropic


class AnthropicLLMProvider:
    def __init__(self):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if api_key is None:
            raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
        self._client = anthropic.Anthropic(api_key=api_key)
        self._model = os.getenv("ANTHROPIC_MODEL") or "claude-haiku-4-5-20251001"
        self._tokens_max = int(os.getenv("ANTHROPIC_TOKENS_MAX") or 1024)

    def ask(self, prompt: str) -> Iterator[str]:
        response = self._client.messages.create(
            model=self._model,
            max_tokens=self._tokens_max,
            messages=[{"role": "user", "content": prompt}],
        )

        block = response.content[0]
        if block.type == "text":
            yield f" Anthropic's response: {block.text}"

        yield "No text response found."
