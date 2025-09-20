from expyriment import design, control, stimuli
control.set_develop_mode()

exp = design.Experiment(name = "2 Squares - Function")
control.initialize(exp)

fixation = stimuli.FixCross()
square_vert = stimuli.Rectangle((50, 50), (0,128,0), position=(-100, 0))
square_red = stimuli.Rectangle((50, 50), (250,0,0), position=(100, 0))

control.start(subject_id=1) 

fixation.present(clear=False, update=True)
displacement_x = 0


def causality(x, y, z):

    
    square_vert.present(clear=True, update=False)
    square_red.present(clear=False, update=False)
    step_size_vert = x # Speed differenciation of Green and red squares / Seems to not really influence the causality 
    step_size_rouge = 10
    
    while abs(square_red.position[0] - square_vert.position[0]) > y and square_red.position[0] <= 100: 
        square_vert.move((step_size_vert, 0))
        square_vert.present(clear=True, update=False)
        square_red.present(clear=False, update=True)

    exp.clock.wait(z)

    while square_vert.position[0] >= displacement_x and square_red.position[0]<500:
        square_red.move((step_size_rouge, 0))
        square_vert.present(clear=True, update=False)
        square_red.present(clear=False, update=True)
        
    return


parametres = [
    (10, 50, 0),
    (10, 50, 50),
    (10, 65, 0),
    (30, 50, 0)
]

# Appel en boucle
for x, y, z in parametres:
    fixation = stimuli.FixCross()
    square_vert = stimuli.Rectangle((50, 50), (0,128,0), position=(-100, 0))
    square_red = stimuli.Rectangle((50, 50), (250,0,0), position=(100, 0))
    causality(x, y, z)



exp.keyboard.wait()

control.end()