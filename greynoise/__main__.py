import click
import click_spinner
import os

from greynoise.client import Greynoise


# Make "-h" work like "--help"
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
GREYNOISE_CONFIG_DIR = '~/.greynoise/'


def get_api_key():
    '''Returns the API key of the current logged-in user.'''
    greynoise_dir = os.path.expanduser(GREYNOISE_CONFIG_DIR)
    keyfile = greynoise_dir + '/api_key'

    # If the file doesn't yet exist let the user know that they need to
    # initialize the greynoise cli
    if not os.path.exists(keyfile):
        raise click.ClickException('Please run "greynoise init <api key>" before using this command')

    # Make sure it is a read-only file
    os.chmod(keyfile, 0o600)

    with open(keyfile, 'r') as fin:
        return fin.read().strip()


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass


@main.command()
@click.argument('key', metavar='<api key>')
def init(key):
    """Initialize the Greynoise command-line"""
    # Create the directory if necessary
    greynoise_dir = os.path.expanduser(GREYNOISE_CONFIG_DIR)
    if not os.path.isdir(greynoise_dir):
        try:
            os.mkdir(greynoise_dir)
        except OSError:
            raise click.ClickException('Unable to create directory to store the Greynoise API key ({})'.format(greynoise_dir))

    # Store the API key in the user's directory
    keyfile = greynoise_dir + '/api_key'
    with open(keyfile, 'w') as fout:
        fout.write(key.strip())
        click.echo(click.style('Successfully initialized', fg='green'))

    os.chmod(keyfile, 0o600)


@main.group()
def noise():
    """Interact with the Noise methods of the Greynoise API"""
    pass


@noise.command('bulk')
def noise_bulk():
    key = get_api_key()

    api = Greynoise(key)

    # Show a spinner to let the user know the tool is working
    with click_spinner.spinner():
        ips = api.noise_bulk()

    for ip in ips:
        click.echo(ip)
