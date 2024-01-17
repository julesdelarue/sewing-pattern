# sewing-pattern

sudo apt-get install inkscape

lancer inkscape juste pour générer la config initiale
inkscape

cd $HOME/.config/inkscape/extensions/
git clone https://github.com/spakin/SimpInkScr.git
pip install Pillow
pip install lxml
export PYTHONPATH="/usr/share/inkscape/extensions:$PYTHONPATH"

Application du script d'exemple à une image SVG vierge :

python "/home/gitpod/.config/inkscape/extensions/SimpInkScr/simpinkscr/simple_inkscape_scripting.py" --py-source=/workspace/sewing-pattern/example_script.py --output=/workspace/sewing-pattern/output.svg /workspace/sewing-pattern/Blank_square.svg

cf. https://github.com/spakin/SimpInkScr/wiki/Running pour la documentation de lancement