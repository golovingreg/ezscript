# ezscript
## Description
A small python script to help manage scripts. It uses a `/home/$USER/bin` directory to store user-written scripts (you can change it you like). It also uses VS Code as an editor (you can also change that). 

## Installation


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
It's my very first useful python script, so I hope to see some friendly advise!
