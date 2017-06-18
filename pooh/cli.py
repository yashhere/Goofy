import click
import zipfile
import urllib.request
import os
import glob2
from distutils.dir_util import copy_tree
import shutil

data_directory = '.pooh_files/'
datapath = os.path.expanduser('~') + "/" + data_directory


def get_gitignores():
    files_hash = {}
    if not os.path.exists(datapath):
        return files_hash

    datapath_for_search = datapath + '**/*.gitignore'
    for filename in glob2.glob(datapath_for_search):
        if filename.endswith('.gitignore'):
            files_hash[(filename.split('/')[-1]).split('.')
                       [0].lower()] = filename

    return files_hash


@click.group()
def main():
    pass


def list_gitignores():
    return ['ada', 'dada', 'dwad']


@main.command(name='generate')
@click.argument('gitignore', nargs=1, required=True)
@click.pass_context
def generate(ctx, gitignore):
    '''
    generate gitignore files
    '''

    gitignores_to_generate = gitignore.split(',')
    gitignores_to_generate = [string.lower()
                              for string in gitignores_to_generate]
    print(gitignores_to_generate)


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
    zip_ref.extractall('/tmp')
    copy_tree("/tmp/gitignore-master/", datapath)

    # os.remove("/tmp/master.zip")              #Not Needed
    # shutil.rmtree("/tmp/gitignore-master")    #Not Needed
    zip_ref.close()


@main.command(name='ls')
@click.pass_context
def list(ctx):
    '''
    list all gitignore files
    '''
    files = get_gitignores()
    file_name_list = []
    if len(files.keys()):
        for file_name in sorted(files.keys()):
            file_name_list.append(file_name)
        all_gitignores = ', '.join(file_name_list)
        print(all_gitignores)

    else:
        print("Please run pooh ls")
