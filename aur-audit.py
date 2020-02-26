#!/usr/bin/env python3
# Copyleft (C) Alexandria Pettit 2020

from pathlib import Path
from sys import argv
from os import system

def walk_nonblacklisted(path, dir_blacklist, file_blacklist):
    ''' Recursively walks non-blacklisted directories and files,
    adding each file to a list that is returned once the function is done.

    path:
        Our Path object.

    dir_blacklist:
        A list of directories not to recurse into.

    file_blacklist:
        A list of files not to bother returning
    '''
    files = []
    for child in path.iterdir():
        if child.is_dir():
            if not child.name in dir_blacklist:
                # recursively walk child directory
                files += walk_dir(child, dir_blacklist)
        else:
            if not child.name in file_blacklist:
                files += [str(child)]
    return files

def walk_up_to_existing_dir(path):
    ''' Walks up from our current directory to the first verified existing parent directory.
    For instance, /home/alexandria/work/foo/something.txt will be walked up to
    /home/alexandria/work, if foo does not exist.
    If the directory does exist, it will simply walk up to /home/alexandria/work/foo.
    '''
    path = path.resolve() # make path absolute
    while not path.is_dir():
        path = path.parent # get to existing directory
        # for instance, if our given path is /existing1/existing2/nonexistant/foo.txt,
        # this will give us /existing1/existing2/
    return path

def main():
    ''' Iterates over arguments, ignoring blacklisted files and directories, then passes the list to `bat`. '''
    args = argv[1:]
    # directories we don't need to audit before installing
    dir_blacklist = ['.git']
    # files we don't need to audit before installing
    file_blacklist = ['.gitignore', '.SRCINFO']

    # list of files built up by recursively walking directories
    files = []

    for arg in args: # iterate over all arguments
        path = Path(arg)
        path = walk_up_to_existing_dir(path)
        files += walk_nonblacklisted(path, dir_blacklist, file_blacklist)

    system('bat ' + ' '.join(files))


if __name__ == '__main__':
    main()
