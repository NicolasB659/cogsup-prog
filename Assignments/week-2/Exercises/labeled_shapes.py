from expyriment import design, control, stimuli
from expyriment.misc.geometry import vertices_triangle
from expyriment.misc.geometry import vertices_regular_polygon


control.set_develop_mode()

exp = design.Experiment(name = "2 Squares")
control.initialize(exp)


fixation = stimuli.FixCross()

hexagon_points = vertices_regular_polygon(n_edges=6, length=25)
hexagon = stimuli.Shape(vertex_list=hexagon_points, colour=(255, 255, 0), position=(100, 0)) 




triangle_points = vertices_triangle(angle=60, length1=50, length2=50)
triangle = stimuli.Shape(vertex_list=triangle_points, colour= (157, 0, 255), position=(-100, 0))
triangle.rotate(180)





# Créer la ligne noire pour le triangle 
line_triangle = stimuli.Line(start_point=(-99, 20),
                    end_point=(-99, 70),
                    line_width=3,
                    colour=(255, 255, 255))

# Créer la ligne noire pour l'hexagone 
line_hexagon = stimuli.Line(start_point=(100, 20),
                    end_point=(100, 70),
                    line_width=3,
                    colour=(255, 255, 255))

texte_triangle = stimuli.TextLine(
    text="Triangle",                  # Le texte à afficher
    position=(-99, 90),                  # Centré sur l'écran
    text_size=20,                    # Taille de police 
    text_bold=True,                  # Texte en gras
    text_colour=(255, 255, 255)          # Couleur du texte (ici blanc)
)

texte_hexagon = stimuli.TextLine(
    text="Hexagon",                
    position=(100, 90),                  
    text_size=20,                    
    text_bold=True,                 
    text_colour=(255, 255, 255)          
)




control.start(subject_id=1)

fixation.present(clear=False, update=True)
hexagon.present(clear=True, update=False)
triangle.present(clear=False, update=False)
line_triangle.present(clear=False, update=False)
line_hexagon.present(clear=False, update=False)
texte_triangle.present(clear=False, update=False)
texte_hexagon.present(clear=False, update=True)


exp.keyboard.wait()

control.end()