# Adding in  the needed libraries:
import numpy as np

# ---------------------------------------------------
# CONSTANTS & DIRECTION OF THE ANTS:
# ---------------------------------------------------
# Ant Direction~
my_direction = np.array(
    [
        (-1, 0),  # Directing North
        (-1, 1),  # Directing North East
        (0, 1),  # Directing East
        (1, 1),  # Directing South East
        (1, 0),  # Directing South
        (1, -1),  # Directing South West
        (0, -1),  # Directing West
        (-1, -1),  # Directing North West
    ]
)


# Agent Based Graph
class Ant:
    def __init__(
        self,
        grid_size=128,
        deposit_rate=8,
        evaporation_rate=1,
        fidelity=247,
        turning_kernel=(0.36, 0.047, 0.008, 0.004),
        max_steps=1500,
        seed=0,
    ):
        np.random.seed(seed)
