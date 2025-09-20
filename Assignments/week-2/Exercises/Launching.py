from expyriment import design, control, stimuli
control.set_develop_mode()

exp = design.Experiment(name = "2 Squares Mov")
control.initialize(exp)

fixation = stimuli.FixCross()
square_vert = stimuli.Rectangle((50, 50), (0,128,0), position=(-100, 0))
square_red = stimuli.Rectangle((50, 50), (250,0,0), position=(100, 0))

control.start(subject_id=1)

square_vert.present(clear=True, update=False)
square_red.present(clear=False, update=False)
fixation.present(clear=False, update=True)

displacement_x = 0
step_size = 10

while abs(square_red.position[0] - square_vert.position[0]) > 50:
    square_vert.move((step_size, 0))
    square_vert.present(clear=True, update=False)
    square_red.present(clear=False, update=True)
 

while square_vert.position[0] >= displacement_x:
    square_red.move((step_size, 0))
    square_vert.present(clear=True, update=False)
    square_red.present(clear=False, update=True)
    

exp.keyboard.wait()

control.end()