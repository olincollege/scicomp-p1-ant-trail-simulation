import numpy as np
import random
from constants import *


class Ant:
    def __init__(self, x, y, direction):
        self.x, self.y = x, y
        self.direction = direction
        self.following = False  # State toggle: Is the ant 'locked' onto a trail?


class AntWorld:
    # The 'Environment': A 2D grid storing pheromone intensity
    def __init__(self):
        self.grid = np.zeros((GRID_SIZE, GRID_SIZE))
        self.ants = []
        self.nest = GRID_SIZE // 2

    def get_fidelity(self, C):
        """
        This is used to set up the fideltity function by calculating the probability of an ant successfully following a trail.
        args:

        As concentration (C) increases, the ant becomes 'stickier' (higher fidelity).
        """
        if C < C_SAT:
            return F_MIN + DELTA_F * (C / C_SAT)
        return F_MIN + DELTA_F

    def fork_logic(self, ant):
        """
        THE FORK ALGORITHM This is the 'Line Straightener.' Instead of turning randomly,
        if an ant sees pheromone directly ahead, it stays the course.
        This prevents the trails from looking like zig-zags.
        """
        fwd_idx = ant.direction % 8
        dx, dy = DIRECTIONS[fwd_idx]
        nx, ny = ant.x + dx, ant.y + dy

        # If straight ahead is within bounds and has pheromone, stay straight
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            if self.grid[nx, ny] > 0.5:
                return fwd_idx

        # Otherwise, check Left/Right 45 degrees
        l_idx, r_idx = (ant.direction - 1) % 8, (ant.direction + 1) % 8
        # Simple directional check
        return l_idx if random.random() < 0.5 else r_idx

    def step(self):
        # 1. Spawning
        if len(self.ants) < MAX_ANTS:
            for _ in range(ANTS_PER_STEP):
                self.ants.append(Ant(self.nest, self.nest, random.randint(0, 7)))

        survivors = []
        for ant in self.ants:
            # 2. Rule 2: Deposit Pheromone BEFORE moving
            self.grid[ant.x, ant.y] += TAU_DEPOSIT

            # 3. Direction Decision
            if ant.following:
                # Roll for fidelity: chance to lose the trail
                if random.random() < BASE_LOSS_PROB or random.randint(
                    0, 255
                ) > self.get_fidelity(self.grid[ant.x, ant.y]):
                    ant.following = False
                else:
                    ant.direction = self.fork_logic(ant)

            # If not following (or just lost it), use Turning Kernel
            if not ant.following:
                r, cum = random.random(), 0
                for n, p in enumerate(TURN_KERNEL):
                    cum += p
                    if r <= cum:
                        ant.direction = (ant.direction + random.choice([-n, n])) % 8
                        break

            # 4. Movement & ABSORBING BOUNDARY CHECK (The Fix)
            dx, dy = DIRECTIONS[ant.direction]
            nx, ny = ant.x + dx, ant.y + dy

            # ONLY add to survivors if nx, ny is inside the grid
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                ant.x, ant.y = nx, ny

                # Check for trail discovery
                if not ant.following and self.grid[nx, ny] > 0.5:
                    if random.randint(0, 255) <= self.get_fidelity(self.grid[nx, ny]):
                        ant.following = True

                survivors.append(ant)
            # If out of bounds, ant is NOT appended, effectively deleted.

        self.ants = survivors

        # 5. Rule 3: Linear Evaporation
        self.grid = np.maximum(0, self.grid - EVAP_RATE)
