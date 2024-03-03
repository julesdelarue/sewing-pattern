# sewing-pattern

## Lancement

Initalisation des dépendances

```shell
./prepare_inkscape.sh
```


Application du script d'exemple à une image SVG vierge :

```shell
python "/home/gitpod/.config/inkscape/extensions/SimpInkScr/simpinkscr/simple_inkscape_scripting.py" \
    --py-source=/workspace/sewing-pattern/example_script.py \
    --output=/workspace/sewing-pattern/output_blank_square.svg /workspace/sewing-pattern/Blank_square.svg
```

cf. https://github.com/spakin/SimpInkScr/wiki/Running pour la documentation de lancement


```shell
python "/home/gitpod/.config/inkscape/extensions/SimpInkScr/simpinkscr/simple_inkscape_scripting.py" \
    --py-source=/workspace/sewing-pattern/jupe_script.py \
    --output=/workspace/sewing-pattern/output_jupe.svg /workspace/sewing-pattern/Jupe.svg
```

### Liens utiles

Exemples
https://github.com/spakin/SimpInkScr/blob/master/examples/README.md

Référence inkex
https://gitlab.com/inkscape/extensions/-/blob/master/inkex/elements/_polygons.py?ref_type=heads
https://inkscape.gitlab.io/inkscape/doxygen-extensions/classinkex_1_1elements_1_1__polygons_1_1PathElementBase.html#a548fd3b2e9e3b247a4d67c037a38af86
