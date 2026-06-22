from askdocs.providers.azure_llm_provider import AzureLLMProvider
from askdocs.providers.anthropic_llm_provider import AnthropicLLMProvider
from askdocs.providers.llm_client import LLMProvider


def get_provider(provider: str) -> LLMProvider:
    if provider == "azure":
        return AzureLLMProvider()
    if provider == "anthropic":
        return AnthropicLLMProvider()
    raise ValueError(f"Invalid provider: {provider!r}")
