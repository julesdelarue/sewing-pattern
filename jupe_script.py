## From https://github.com/spakin/SimpInkScr/blob/65f68c2584154965957875181544fba16e3d51f8/examples/animation.py#L36
H = 32
B = 25
Xorigin = 70
Yorigin = 70

curveYDisplace = H/4
curveXDisplace = 0.6

p1 = path([Move(Xorigin,Yorigin), # 1er point
                       Vert(Yorigin+1),
                       Vert(Yorigin+1+H),
                       Horz(Xorigin + B),
                       #Line(Xorigin-4+B, Yorigin),
                       Curve(
                        Xorigin+B-curveXDisplace, Yorigin+H-curveYDisplace, 
                        Xorigin+B-4+1.6, Yorigin+curveYDisplace, 
                        Xorigin+B-4,Yorigin
                       ),
                       Line(Xorigin,Yorigin)
                       #Horz(164.45-134.90),
                       #Curve(784, 64, 432, 0, 197, 145), 
                       # Coord 784, 64 pour le point de contrôle du point précédent
                       # 432, 0 pour le point de controle du point suivant
                       #  197, 145 le point suivant
                      # Curve(-176, 368, 171, 471, 353, 471)
                      ],
                      fill='none')


H = 20
B = 25
Xorigin = 100
Yorigin = 70
curveYDisplace = H/4
curveXDisplace = 0.6

p2 = path([Move(Xorigin,Yorigin), # 1er point
                       Vert(Yorigin+1),
                       Vert(Yorigin+1+H),
                       Horz(Xorigin + B),
                       Curve(
                        Xorigin+B-curveXDisplace, Yorigin+H-curveYDisplace, 
                        Xorigin+B-4+1.6, Yorigin+curveYDisplace, 
                        Xorigin+B-4,Yorigin
                       ),
                       Line(Xorigin,Yorigin)
                      ],
                      fill='none')

H = 32
B = 20
Xorigin = 130
Yorigin = 70
curveYDisplace = H/4
curveXDisplace = 0.6

p3 = path([Move(Xorigin,Yorigin), # 1er point
                       Vert(Yorigin+1),
                       Vert(Yorigin+1+H),
                       Horz(Xorigin + B),
                       Curve(
                        Xorigin+B-curveXDisplace, Yorigin+H-curveYDisplace, 
                        Xorigin+B-4+1.6, Yorigin+curveYDisplace, 
                        Xorigin+B-4,Yorigin
                       ),
                       Line(Xorigin,Yorigin)
                      ],
                      fill='none')