import click
from gpt_engineer.main import app


@click.command()
@click.option(
    '--directory',
    '-d',
    prompt='Enter the directory name',
    help='The name of the directory with the main_prompt file. This is where the code for your project will be generated.'
)
def build(directory):
    click.echo(f'Building project in {directory}...')