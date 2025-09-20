from expyriment import design, control, stimuli
from expyriment.misc.geometry import vertices_regular_polygon
from expyriment.misc.geometry import vertices_triangle


control.set_develop_mode()

exp = design.Experiment(name="Labeled Shapes Function")
control.initialize(exp)

fixation = stimuli.FixCross()

def create_labeled_polygon(n_sides, side_length, colour, position, label_text):
    # Create polygon points and shape
    polygon_points = vertices_regular_polygon(n_edges=n_sides, length=side_length)
    polygon = stimuli.Shape(vertex_list=polygon_points, colour=colour, position=position)

    # Create label text positioned slightly below the polygon
    label_pos = (position[0], position[1] + side_length + 65)  # 20 pixels below polygon
    label = stimuli.TextLine(text=label_text, position=label_pos, text_size=20, text_bold=True, text_colour=(255,255,255))

    return polygon, label

# Create polygons with labels
hexagon, hex_label = create_labeled_polygon(6, 25, (255, 255, 0), (100, 0), "Hexagon")

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

control.start(subject_id=1)

fixation.present(clear=True, update=True)

# Present all stimuli
hexagon.present(clear=True, update=False)
hex_label.present(clear=False, update=False)
triangle.present(clear=False, update=False)
line_triangle.present(clear=False, update=False)
line_hexagon.present(clear=False, update=False)
texte_triangle.present(clear=False, update=True)



exp.keyboard.wait()
control.end()
