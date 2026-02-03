import numpy as np

# WINDOW & GRID
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 200
CELL_SIZE = 4  # Maps 200 grid to 800px
FPS = 15

# POPULATION
ANTS_PER_STEP = 1
MAX_ANTS = 500
ANT_SIZE = 8

# PHEROMONE (Paper Variable: t)
# Use 12 for Fig 3a, 7 for Fig 3b, 3 for Fig 3c
TAU_DEPOSIT = 4.0
EVAP_RATE = 1.0  # Linear decay as per paper Rule 3

# FIDELITY f(C) (Paper Scale: 0-255)
F_MIN = 210  # flow
DELTA_F = 37  # Rise to max 247
C_SAT = 20  # Saturation concentration

# BEHAVIOR
BASE_LOSS_PROB = 0.02  # Probability of losing trail randomly

# TURNING KERNEL B_n (Wide Kernel from Fig 1)
# Probabilities for turning [0, 45, 90, 135] degrees
TURN_KERNEL = [0.360, 0.047, 0.008, 0.004]

# MOORE NEIGHBORHOOD
DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
