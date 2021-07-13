# ezscript
## Description
A small python script to help manage scripts. It uses a `$HOME/bin` directory to store user-written scripts (you can change it if you like, the instruction is in the end of the `Usage` category). It also uses VS Code as a default editor for scripts (you can also change that). 

## Installation
To install the script, you just copy the file `ezscript.py` into any of your `bin` directories (and rename it to `ezscript` if you like). I prefer keeping my personal scripts in the `$HOME/bin` directory. To install it like I do, go to your terminal and use these commands: 

Create a new directory:
```
mkdir $HOME/bin
```
Add it to your $PATH (change `.zshrc` to your shell config file):
```
echo 'if [ -d "$HOME/bin" ] ; then' >> $HOME/.zshrc
echo '  PATH="$HOME/bin:$PATH"' >> $HOME/.zshrc
echo 'fi' >> $HOME/.zshrc

source $HOME/.zshrc
```
Download the script (either `curl` or `wget`):
```
wget -O $HOME/bin/ezscript https://raw.githubusercontent.com/golovingreg/ezscript/master/ezscript.py
```
or:
```
curl -o $HOME/bin/ezscript https://raw.githubusercontent.com/golovingreg/ezscript/master/ezscript.py
```
Give it necessary permissions:
```
chmod 755 $HOME/bin/ezscript
```

## Usage
To use the program, type `ezscript` into your terminal and pass some options.
******
Available options:
* -o: opens VS Code in your scripts directory
* -n [name]: creates a new script
* -on [name]: creates a new script and opens VS Code
* -t [type]: use after '-n [name]' or '-on [name]' to insert a correct shebang:
  * 'bash' for '#!/bin/bash' 
  * 'zsh' for '#!/bin/zsh' 
  * 'python' for '#!/usr/bin/env python 3' 
******
You can change default script directory on `line 11`.
You can change code editor on `line 40`.
