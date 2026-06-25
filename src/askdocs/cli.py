import typer
import os

from dotenv import load_dotenv
from askdocs.providers import get_provider
from askdocs.loader import retrieve, build_prompt
from typing_extensions import Annotated


def main(
    prompt: str,
    provider: Annotated[
        str, typer.Option("--provider", help="LLM provider to use (azure | anthropic)")
    ],
):
    sorted_chunks = list(retrieve(prompt, os.getenv("FILE_PATH") or ""))
    full_prompt = build_prompt(prompt, sorted_chunks)

    api_provider = get_provider(provider)
    for chunk in api_provider.ask(full_prompt):
        print(chunk, end="", flush=True)


def cli():
    load_dotenv()
    typer.run(main)
