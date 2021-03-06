import click

from leasebot.cli import pass_context
from leasebot.runtime import Runtime
from leasebot.utils import check_valid_voice, check_valid_model
from leasebot.const import (INTERVAL_SEC, INPUT_DEVICE, OUTPUT_CHANNEL,
                             INPUT_CHANNEL, OUTPUT_DEVICE, SAMPLE_RATE,
                             THRESHOLD_DB, NUM_CLASSES_SOUNDS,
                             SEQ_LEN, TEMPERATURE,
                             PENALTY, VOLUME, OSC_ADDRESS, OSC_PORT)


@click.command('start', short_help='Start a live session')
@click.option('--interval',
              default=INTERVAL_SEC,
              help='Interval (in seconds) of analyzing incoming live signal')
@click.option('--input_device',
              default=INPUT_DEVICE,
              help='Index of audio device for incoming signal')
@click.option('--output_device',
              default=OUTPUT_DEVICE,
              help='Index of audio device for outgoing signal')
@click.option('--input_channel',
              default=INPUT_CHANNEL,
              help='Index of channel for incoming signal')
@click.option('--output_channel',
              default=OUTPUT_CHANNEL,
              help='Index of channel for outgoing signal')
@click.option('--samplerate',
              default=SAMPLE_RATE,
              help='Sample rate of audio signals')
@click.option('--threshold',
              default=THRESHOLD_DB,
              help='Ignore audio events under this db value')
@click.option('--num_classes',
              default=NUM_CLASSES_SOUNDS,
              help='Number of k-means classes')
@click.option('--dynamics/--no_dynamics',
              default=False,
              help='Use dynamics (volume) classes')
@click.option('--durations/--no_durations',
              default=False,
              help='Use duration classes (length of sound events)')
@click.option('--seq_len',
              default=SEQ_LEN,
              help='How long is the sequence the model needs to predict')
@click.option('--temperature',
              default=TEMPERATURE,
              help='Softmax reweighting temperature')
@click.option('--penalty',
              default=PENALTY,
              help='Multiple of seq_len to be reached for cutting sequence')
@click.option('--reference',
              default=None,
              help='Use this voice as a reference for PCA and k-means')
@click.option('--volume',
              default=VOLUME,
              type=float,
              help='Volume of the audio output')
@click.option('--osc_address',
              default=OSC_ADDRESS,
              type=str,
              help='Address of OSC server')
@click.option('--osc_port',
              default=OSC_PORT,
              type=int,
              help='Port of OSC server')
@click.argument('voice')
@click.argument('model')
@pass_context
def cli(ctx, voice, model, **kwargs):
    """Start a live session with leasebot."""
    try:
        check_valid_model(model)
    except FileNotFoundError as err:
        ctx.elog('Model "{}" is invalid: {}'.format(model, err))
    else:
        try:
            check_valid_voice(voice)
        except FileNotFoundError as err:
            ctx.elog('Voice "{}" is invalid: {}'.format(voice, err))
        else:
            runtime = Runtime(ctx, voice, model, **kwargs)
            runtime.initialize()
