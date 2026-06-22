from dotenv import load_dotenv
import typer
from askdocs.providers import get_provider

from typing_extensions import Annotated


def main(
    prompt: str,
    provider: Annotated[
        str, typer.Option("--provider", help="LLM provider to use (azure | anthropic)")
    ],
):
    api_provider = get_provider(provider)
    response = api_provider.ask(prompt)
    typer.echo(response)


def cli():
    load_dotenv()
    typer.run(main)
