from typing import Iterator


class AzureLLMProvider:
    def ask(self, prompt: str) -> Iterator[str]:
        yield f" Asking Azure: {prompt}"
