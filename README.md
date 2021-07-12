# ezscript
## Description
A small python script to help manage scripts. It uses a `/home/$USER/bin` directory to store user-written scripts (you can change it if you like, the instruction is in the end of the `Usage` category). It also uses VS Code as a default editor for scripts (you can also change that). 

## Installation
To install the script, you just copy the file `ezscript.py` into any of your `bin` directories. I prefer keeping my personal scripts in the `/home/$USER/bin` directory. To install it like I do, go to your terminal and use these commands: 
```
mkdir ~/bin
wget -O ~/bin/ezscript https://raw.githubusercontent.com/golovingreg/ezscript/master/ezscript.py
chmod 755 ~/bin/ezscript
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

## About 
It's my very first python script that I find helpful, so I'll be glad to hear some friendly advise!
