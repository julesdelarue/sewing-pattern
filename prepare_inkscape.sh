#!/bin/bash

sudo apt-get install -y inkscape
## Permet d'init le répertoire des extensions d'inkscape
inkscape --version

cd $HOME/.config/inkscape/extensions/ 
git clone https://github.com/spakin/SimpInkScr.git 

#Pour inkex
sudo apt install libgirepository1.0-dev 

pip install Pillow lxml inkex
export PYTHONPATH="/usr/share/inkscape/extensions:$PYTHONPATH"

