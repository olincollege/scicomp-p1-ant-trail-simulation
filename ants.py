import numpy as np
from constants import *

# 8-direction movement
DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


class Ant:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.following = False


class AntWorld:
    def __init__(self, fidelity=247, deposit=6, evaporation=1):
        self.grid = np.zeros((GRID_SIZE, GRID_SIZE))
        self.ants = []

        self.fidelity = fidelity
        self.deposit = deposit
        self.evaporation = evaporation

        self.nest = GRID_SIZE // 2

    def spawn_ant(self):
        self.ants.append(Ant(self.nest, self.nest, np.random.randint(8)))

    def fidelity_check(self):
        return np.random.randint(256) < self.fidelity

    def step(self):
        self.spawn_ant()

        new_ants = []

        for ant in self.ants:
            # deposit pheromone
            self.grid[ant.x, ant.y] += self.deposit

            if ant.following:
                if not self.fidelity_check():
                    ant.following = False
                    ant.direction = (ant.direction + np.random.choice([-1, 1])) % 8
            else:
                ant.direction = (ant.direction + np.random.choice([-1, 0, 1])) % 8

            dx, dy = DIRECTIONS[ant.direction]
            nx, ny = ant.x + dx, ant.y + dy

            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                ant.x, ant.y = nx, ny

                if self.grid[nx, ny] > 0 and self.fidelity_check():
                    ant.following = True

                new_ants.append(ant)

        self.ants = new_ants

        # evaporation
        self.grid -= self.evaporation
        self.grid[self.grid < 0] = 0
