import numpy as np
import random
from constants import *


def get_fidelity(C):
    """Piecewise linear fidelity function

    Args:
        C: the int to the concentration level

    Returns:
        int: the total fidelity rate
    """
    if C >= C_SAT:
        return F_MIN + DELTA_F
    return F_MIN + (DELTA_F * C / C_SAT)


class Ant:
    def __init__(self, x, y):
        self.x, self.y = x, y

        # Ant direction is set for the Ant moving set for random
        self.direction = random.randint(0, 7)

    def move(self, grid):
        """Piecewise linear fidelity function

        Args:
            grid: the

        Returns:
            int: the total fidelity rate
        """
        C = grid[self.x, self.y]

        # Probability of for ant following the path based on the paper is phi/256
        ant_following = random.randint(0, 255) < get_fidelity(C)

        if ant_following:
            # FORK ALGORITHM IMPLEMENTATION
            dx, dy = DIRECTIONS[self.direction]  # Set of directions
            nx, ny = self.x + dx, self.y + dy  # Values set for location on the set grid

            # First check is to see if the ants can move straight ahead
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and grid[nx, ny] > 0:
                pass
            else:
                # Second check is to see if the ants can move within the set branches
                left_dir = (self.direction - 1) % 8
                right_dir = (self.direction + 1) % 8

                l_val = self._get_val(grid, left_dir)
                r_val = self._get_val(grid, right_dir)

                if l_val > r_val:
                    self.direction = left_dir
                elif r_val > l_val:
                    self.direction = right_dir
                else:
                    self.explore()
        else:
            self.explore()

        # Updating the ant position within time with respect to direction and location
        dx, dy = DIRECTIONS[self.direction]
        self.x += dx
        self.y += dy

        # Absorbing boundary
        return 0 <= self.x < GRID_SIZE and 0 <= self.y < GRID_SIZE

    def _get_val(self, grid, direction):
        """Piecewise linear fidelity function

        Args:
            grid:

        Returns:
            int: the total fidelity rate
        """
        dx, dy = DIRECTIONS[direction]
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            return grid[nx, ny]
        return -1

    def explore(self):
        """Turning kernel logic from the paper."""
        r = random.random()
        cum = 0
        for n, prob in enumerate(TURN_KERNEL, 1):
            cum += prob
            if r <= cum:
                turn = n if random.random() < 0.5 else -n
                self.direction = (self.direction + turn) % 8
                break


class AntWorld:
    def __init__(self):
        self.grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=float)
        self.ants = []
        self.nest = (GRID_SIZE // 2, GRID_SIZE // 2)

    def step(self):
        # Spawn new ants (Matches the Ant.__init__ signature)
        if len(self.ants) < MAX_ANTS:
            for _ in range(ANTS_PER_STEP):
                self.ants.append(Ant(*self.nest))

        survivors = []
        for ant in self.ants:
            if ant.move(self.grid):
                self.grid[ant.x, ant.y] += TAU_DEPOSIT
                survivors.append(ant)
        self.ants = survivors

        # Linear Evaporation
        self.grid = np.maximum(0, self.grid - EVAP_RATE_LINEAR)
