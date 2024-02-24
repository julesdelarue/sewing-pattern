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

python "/home/gitpod/.config/inkscape/extensions/SimpInkScr/simpinkscr/simple_inkscape_scripting.py" --py-source=/workspace/sewing-pattern/jupe_script.py --output=/workspace/sewing-pattern/output.svg /workspace/sewing-pattern/Jupe.svg

https://inkscape.gitlab.io/inkscape/doxygen-extensions/classinkex_1_1elements_1_1__polygons_1_1PathElementBase.html#a548fd3b2e9e3b247a4d67c037a38af86
https://gitlab.com/inkscape/extensions/-/blob/master/inkex/elements/_polygons.py?ref_type=heads

Edit