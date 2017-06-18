import click
import zipfile
import urllib.request


@click.group()
def main():
    pass


def list_gitignores():
    return ['ada', 'dada', 'dwad']


@main.command(name='generate')
@click.argument('gitignore', nargs=-1, required=True)
@click.pass_context
def generate(ctx, gitignore):
    ''' 
    generate gitignore files
    '''

    for n in gitignore:
        print(n)


@main.command(name='update')
@click.pass_context
def update(ctx):
    '''
    Update all gitignore files
    '''

    print("updating")
    gitignore_url = "https://github.com/github/gitignore/archive/master.zip"
    zip_path = urllib.request.urlretrieve(gitignore_url, '/tmp/master.zip')

    zip_ref = zipfile.ZipFile('/tmp/master.zip', 'r')
    zip_ref.extractall('/home/yash/.pooh/')
    zip_ref.close()


@main.command(name='ls')
@click.pass_context
def list(ctx):
    '''
    list all gitignore files
    '''

    print("listing")
