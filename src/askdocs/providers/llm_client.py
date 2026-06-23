from typing import Iterator, Protocol


class LLMProvider(Protocol):
    def ask(self, prompt: str) -> Iterator[str]: ...
