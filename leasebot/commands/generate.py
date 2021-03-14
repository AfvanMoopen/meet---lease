import click

from leasebot.cli import pass_context
from leasebot.const import THRESHOLD_DB, BLOCK_SEC
from leasebot.generate import generate_voice


@click.command('generate', short_help='Generate voice based on .wav file')
@click.option('--threshold',
              default=THRESHOLD_DB,
              help='Ignore audio events under this dB value')
@click.option('--block_sec',
              default=BLOCK_SEC,
              help='Slice the audio file in this length (sec)')
@click.argument('file', type=click.Path(exists=True))
@click.argument('name')
@pass_context
def cli(ctx, file, name, **kwargs):
    generate_voice(ctx, file, name,
                   db_threshold=kwargs.get('threshold'),
                   block=kwargs.get('block_sec'))
