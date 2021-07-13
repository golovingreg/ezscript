#!/usr/bin/env python3

import os
import sys
import argparse
import subprocess

user = os.environ['USER']
home = os.environ['HOME']

# Change your script directory here
bin_dir = f'{home}/bin'


def create_script(name: str, type='default'):
    initial_dir = os.getcwd()

    os.chdir(bin_dir)
    new_script = open(name, 'w+')

    if type == 'bash':
        new_script.write('#!/bin/bash')
    elif type == 'zsh':
        new_script.write('#!/bin/zsh')
    elif type == 'python':
        new_script.write('#!/usr/bin/env python3')
    else:
        new_script.write('#!')

    new_script.close()
    os.chmod(f'{bin_dir}/{name}', 0o755)

    os.chdir(initial_dir)


def open_editor():
    initial_dir = os.getcwd()

    os.chdir(bin_dir)
    # Change code here if you want to change your default script editor
    subprocess.run(['code', '.'])

    os.chdir(initial_dir)


parser = argparse.ArgumentParser(
    description='''Create a script and make it executable easily! 
    Either run with some arguments to create a script in one line, or pass no arguments to use step-by-step mode.''')

parser.add_argument('-o', action='store_true',
                    help='open your default editor in your scripts directory')
parser.add_argument('-n', metavar='filename',
                    help='create a script with the specified name')
parser.add_argument('-t', metavar='interpreter type',
                    help='''enter 'bash', 'zsh', or 'python' ''')
parser.add_argument('-on', metavar='filename',
                    help='create a script with the specified name and open your editor')

args = vars(parser.parse_args())

if args['on']:
    if args['t'] in ['bash', 'zsh', 'python']:
        create_script(args['on'], args['t'])
    else:
        create_script(args['on'])

    open_editor()

if args['o']:
    open_editor()

if args['n'] != None:
    if args['t'] in ['bash', 'zsh', 'python']:
        create_script(args['n'], args['t'])
    else:
        create_script(args['n'])


if not args['on'] and not args['o'] and args['n'] == None:
    print(
        f'''Hello, {user}! Here's a script that helps you generate and manage scripts.''')
    print('To use the program, type `ezscript` and pass some options.')
    print('******')
    print('Available options:')
    print('-o: opens VS Code in your scripts directory')
    print('-n [name]: creates a new script')
    print('-on [name]: creates a new script and opens VS Code')
    print(
        '''-t [type]: use after '-n [name]' or '-on [name]' to insert a correct shebang:''')
    print('''* 'bash' for '#!/bin/bash' ''')
    print('''* 'zsh' for '#!/bin/zsh' ''')
    print('''* 'python' for '#!/usr/bin/env python 3' ''')
    print('******')
    print('You can also change default settings like script directory (line 11) and default editor (line 40)')
    print('Hope this helps you a little bit!')
