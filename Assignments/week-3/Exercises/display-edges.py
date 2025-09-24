from expyriment import design, control, stimuli
from expyriment.misc.geometry import vertices_regular_polygon


control.set_develop_mode()

exp = design.Experiment(name="display-edges")
control.initialize(exp)

width, height = exp.screen.size

x = (width // 2) 
y = (height // 2)

x_size = width*0.05
y_size = height*0.05

x_position = (x - 0.5*x_size)
y_position = (y - 0.5*y_size)

y_positionUP = y_position - 1


square_points1 = vertices_regular_polygon(n_edges= 4, length= min(x_size, y_size))
square_1 = stimuli.Shape(vertex_list=square_points1, colour= (0,0,0), position=(x_position, y_positionUP), debug_contour_colour= (255,0,0))

square_points2 = vertices_regular_polygon(n_edges= 4, length= min(x_size, y_size))
square_2 = stimuli.Shape(vertex_list=square_points2, colour= (0,0,0), position=(-x_position, -y_position), debug_contour_colour= (255,0,0))

square_points3 = vertices_regular_polygon(n_edges= 4, length= min(x_size, y_size))
square_3 = stimuli.Shape(vertex_list=square_points3, colour= (0,0,0), position=(-x_position, y_positionUP), debug_contour_colour= (255,0,0))

square_points4 = vertices_regular_polygon(n_edges= 4, length= min(x_size, y_size))
square_4 = stimuli.Shape(vertex_list=square_points4, colour= (0,0,0), position=(x_position, -y_position), debug_contour_colour= (255,0,0))

control.start(subject_id=1)


square_1.present(clear=True, update=False)
square_2.present(clear=False, update=False)
square_3.present(clear=False, update=False)
square_4.present(clear=False, update=True)

exp.keyboard.wait()

control.end()