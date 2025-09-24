from expyriment import design, control, stimuli
from expyriment.misc.geometry import vertices_regular_polygon
import expyriment.misc.constants 

control.set_develop_mode()

exp = design.Experiment(name="Kanizsa-square", background_colour = (128, 128, 128))
control.initialize(exp)


width, height = exp.screen.size



x_square_size = width*0.25
radius_size = width*0.05



x1 = (x_square_size / 2)
y1 = (x_square_size / 2) 


square_points1 = vertices_regular_polygon(n_edges= 4, length= min(x_square_size, x_square_size))
square_1 = stimuli.Shape(vertex_list=square_points1, colour= (128,128,128), position=(0,0))

circle1 = stimuli.Circle(radius=radius_size, position=(x1,y1), colour=(0,0,0))

circle2 = stimuli.Circle(radius=radius_size, position=(-x1,-y1), colour=(255,255,255))

circle3 = stimuli.Circle(radius=radius_size, position=(-x1,y1), colour=(0,0,0))
circle4 = stimuli.Circle(radius=radius_size, position=(x1,-y1), colour=(255,255,255))


control.start(subject_id=1)

circle1.present(clear=True, update=False)
circle2.present(clear=False, update=False)
circle3.present(clear=False, update=False)
circle4.present(clear=False, update=False)
square_1.present(clear=False, update=True)


exp.keyboard.wait()

control.end()