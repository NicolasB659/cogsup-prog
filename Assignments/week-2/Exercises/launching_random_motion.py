from expyriment import design, control, stimuli
import math
import random 

control.set_develop_mode()

exp = design.Experiment(name="2 Squares - Circle")
control.initialize(exp)

RADIUS = 300
displacement_x = 0

fixation = stimuli.FixCross()

def causality(speed_vert, stop_distance, delay_ms):

    square_vert.present(clear=True, update=False)
    square_red.present(clear=False, update=True)

    step_size_rouge = 10  # Toujours vers la droite puisque carré rouge est à droite

    # Le carré vert avance vers le rouge
    while True:
        dx = square_red.position[0] - square_vert.position[0]
        dy = square_red.position[1] - square_vert.position[1]
        distance = math.hypot(dx, dy)

        if distance <= stop_distance:
            break

        dir_x = dx / distance
        dir_y = dy / distance
        step_x = dir_x * speed_vert
        step_y = dir_y * speed_vert

        square_vert.move((step_x, step_y))
        square_vert.present(clear=True, update=False)
        square_red.present(clear=False, update=True)

    exp.clock.wait(delay_ms)

    # Le carré rouge avance horizontalement vers la droite (limite 500 px)
    while square_red.position[0] < 500:
        square_red.move((step_size_rouge, 0))
        square_vert.present(clear=True, update=False)
        square_red.present(clear=False, update=True)

    return


parametres = [
    (10, 50, 0),
    (10, 50, 50),
    (10, 65, 0),
    (10, 50, 0)
]

control.start(subject_id=1)

for speed_vert, stop_dist, delay in parametres:
    # Angle entre -pi/2 et pi/2 pour être sur la moitié droite du cercle
    angle = random.uniform(-math.pi/2, math.pi/2)
    x_red = math.cos(angle) * RADIUS
    y_red = math.sin(angle) * RADIUS

    fixation.present(clear=True)
    exp.clock.wait(500)

    square_vert = stimuli.Rectangle((50, 50), (0, 128, 0), position=(0, 0))
    square_red = stimuli.Rectangle((50, 50), (250, 0, 0), position=(x_red, y_red))

    causality(speed_vert, stop_dist, delay)

exp.keyboard.wait()
control.end()
