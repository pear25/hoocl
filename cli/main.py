import click

@click.command()
def cli():
    """Simple cli greeting"""
    click.echo("Hello from hoocl")

if __name__ == '__main__':
    print("Non import run::")
    cli()