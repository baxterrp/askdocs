import typer
from typing_extensions import Annotated


def main(
    prompt: str,
    provider: Annotated[
        str, typer.Option("--provider", help="LLM provider to use (azure | anthropic)")
    ],
):
    typer.echo(f"Hello, World! Prompt: {prompt}, Provider: {provider}")


def cli():
    typer.run(main)
