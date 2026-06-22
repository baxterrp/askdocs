from typing import Protocol


class LLMProvider(Protocol):
    def ask(self, prompt: str) -> str: ...
