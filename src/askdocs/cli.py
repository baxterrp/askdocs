import typer

def main(message: str):
    typer.echo(f"Hello, World! Message: {message}")

def cli():
    typer.run(main)