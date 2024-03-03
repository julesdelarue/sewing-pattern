S = path([Move(57, 13), # Haut droite du S
          Vert(28), # Vertical -> y = +28
          Quadratic(52, 25, 46, 24),
          Quadratic(41, 23, 36, 23),
          Quadratic(29, 23, 26, 25),
          #Quadratic(23, 26, 23, 30),
          #Quadratic(23, 33, 25, 35),
          #Quadratic(27, 36, 33, 37),
          #Line(40, 39),
          #Quadratic(52, 41, 57, 46),
          #Quadratic(62, 51, 62, 60),
          #Quadratic(62, 71, 55, 77),
          #Quadratic(48, 82, 34, 82),
          #Quadratic(27, 82, 21, 81),
          #Quadratic(14, 80, 7, 77),
          #Vert(62),
          #Quadratic(14, 66, 20, 68),
          #Quadratic(26, 69, 32, 69),
          #Quadratic(38, 69, 41, 67),
          #Quadratic(44, 65, 44, 62),
          #Quadratic(44, 58, 42, 57),
          #Quadratic(40, 55, 34, 53),
          #Line(27, 52),
          #Quadratic(16, 50, 11, 45),
          #Quadratic(7, 40, 7, 31),
          #Quadratic(7, 21, 13, 15),
          #Quadratic(20, 10, 33, 10),
          #Quadratic(39, 10, 45, 11),
          #Quadratic(51, 12, 57, 13),
          ZoneClose()],
         fill='#decd87' #, stroke_width=5
         )
         
#for obj in all_shapes():
#    obj.rotate_path(-22)
    #obj._inkscape_obj.path.set_
    #print(obj._inkscape_obj.path )

## From https://github.com/spakin/SimpInkScr/blob/65f68c2584154965957875181544fba16e3d51f8/examples/animation.py#L36
scripting_path = path([Move(1152, 336), # 1er point
                       Curve(784, 64, 432, 0, 197, 145), 
                       # Coord 784, 64 pour le point de contrôle du point précédent
                       # 432, 0 pour le point de controle du point suivant
                       #  197, 145 le point suivant
                       Curve(-176, 368, 171, 471, 353, 471)],
                      fill='none')