#!/bin/bash

sudo apt-get install -y inkscape
## Permet d'init le répertoire des extensions d'inkscape
inkscape --version

cd $HOME/.config/inkscape/extensions/ 
git clone https://github.com/spakin/SimpInkScr.git 
pip install Pillow lxml 
export PYTHONPATH="/usr/share/inkscape/extensions:$PYTHONPATH"

