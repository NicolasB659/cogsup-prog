from expyriment import design, control, stimuli
from expyriment.misc.geometry import vertices_regular_polygon
import expyriment.misc.constants 

control.set_develop_mode()

exp = design.Experiment(name="Kanizsa-rectangle", background_colour = (128, 128, 128))
control.initialize(exp)


width, height = exp.screen.size



x_rectangle_size = width*0.35
y_rectangle_size = height*0.25
radius_size = width*0.05


x1 = (x_rectangle_size / 2)
y1 = (y_rectangle_size / 2) 


rectangle = stimuli.Rectangle((x_rectangle_size, y_rectangle_size), (128,128,128), position=(0, 0))

circle1 = stimuli.Circle(radius=radius_size, position=(x1,y1), colour=(0,0,0))

circle2 = stimuli.Circle(radius=radius_size, position=(-x1,-y1), colour=(255,255,255))

circle3 = stimuli.Circle(radius=radius_size, position=(-x1,y1), colour=(0,0,0))
circle4 = stimuli.Circle(radius=radius_size, position=(x1,-y1), colour=(255,255,255))


control.start(subject_id=1)

circle1.present(clear=True, update=False)
circle2.present(clear=False, update=False)
circle3.present(clear=False, update=False)
circle4.present(clear=False, update=False)
rectangle.present(clear=False, update=True)


exp.keyboard.wait()

control.end()