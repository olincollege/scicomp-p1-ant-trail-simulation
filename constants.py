import numpy as np

# WINDOW & GRID
GRID_SIZE = 220
CELL_SIZE = 3
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE
FPS = 60

# POPULATION & PHEROMONE
ANTS_PER_STEP = 1
MAX_ANTS = 500
TAU_DEPOSIT = 8.0
EVAP_RATE_LINEAR = 1.0  # Linear decay as per paper Rule 3

# FIDELITY f(C)
F_MIN = 247  # flow
DELTA_F = 0  # Rise to max 247
C_SAT = 12  # Saturation concentration

# TURNING KERNEL B_n
# Probabilities for turning [0, 45, 90, 135] degrees
TURN_KERNEL = [0.360, 0.047, 0.008, 0.004]

# MOORE NEIGHBORHOOD
DIRECTIONS = [
    (1, 0),  # E
    (1, 1),  # SE
    (0, 1),  # S
    (-1, 1),  # SW
    (-1, 0),  # W
    (-1, -1),  # NW
    (0, -1),  # N
    (1, -1),  # NE
]

# COLORS FOR SIMULATION
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
