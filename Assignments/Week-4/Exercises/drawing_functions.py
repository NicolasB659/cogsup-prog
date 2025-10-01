from expyriment import design, control, stimuli
import random


PRELOADED = set()

def load(stims):
   
    for stim in stims:
        stim.preload()
        PRELOADED.add(stim)


def timed_draw(stims):
    
    t0 = control.get_time()
    for i, stim in enumerate(stims):
        stim.present(clear=(i == 0), update=(i == len(stims)-1))
    t1 = control.get_time()
    return t1 - t0


def present_for(stims, t=1000):
   
    if not stims or t <= 0:
        return

    for i, stim in enumerate(stims):
        stim.present(clear=(i == 0), update=(i == len(stims)-1))
    
    exp.clock.wait(t)


""" Test functions """
exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
load([fixation])

n = 20
positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n)]
squares = [stimuli.Rectangle(size=(50, 50), position = pos) for pos in positions]
load(squares)

durations = []

t0 = exp.clock.time
for square in squares:
    if not square.is_preloaded:
        print("Preloading function not implemneted correctly.")
    stims = [fixation, square] 
    present_for(stims, 500)
    t1 = exp.clock.time
    durations.append(t1-t0)
    t0 = t1

print(durations)

control.end()