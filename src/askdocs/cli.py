import typer
import os

from dotenv import load_dotenv
from askdocs.providers import get_provider
from askdocs.loader import load_files
from typing_extensions import Annotated


def main(
    prompt: str,
    provider: Annotated[
        str, typer.Option("--provider", help="LLM provider to use (azure | anthropic)")
    ],
):
    for line in load_files(os.getenv("FILE_PATH") or ""):
        print(line)
        
    api_provider = get_provider(provider)
    for chunk in api_provider.ask(prompt):
        print(chunk, end="", flush=True)


def cli():
    load_dotenv()
    typer.run(main)
