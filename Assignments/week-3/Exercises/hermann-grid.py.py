from expyriment import design, control, stimuli
import expyriment.misc.constants 

control.set_develop_mode()


exp = design.Experiment(name="herman-grid", background_colour= (255,255,255)) #I don't understand because this not change the screen color 


control.initialize(exp)

exp.screen.colour = (255, 255, 255)

width, height = exp.screen.size
x = 100 
y = (height//2) - (x/2)
nb_squares = 8
boucle = nb_squares
line = 20

x_start = -(width//2) + (x/2)
origine = -(width//2) + (x/2)


control.start(subject_id=1)

while boucle > 0:
    for i in range(nb_squares):
       square = stimuli.Rectangle((x, x), (255,255,255), position=(x_start,y))
       square.present(clear=False, update=False) 
       x_start = origine + i*(x+line)

    boucle = boucle - 1
    y = y - (x+line)

exp.screen.update()

exp.keyboard.wait()

control.end()