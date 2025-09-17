from expyriment import design, control, stimuli
control.set_develop_mode()

exp = design.Experiment(name = "2 Squares")
control.initialize(exp)

fixation = stimuli.FixCross()
square_vert = stimuli.Rectangle((50, 50), (0,128,0))
square_red = stimuli.Rectangle((50, 50), (0,0,225))

control.start(subject_id=1)

square_vert.present(clear=True, update=False)
square_red.present(clear=False, update=False)
fixation.present(clear=False, update=True)

exp.keyboard.wait()

control.end()