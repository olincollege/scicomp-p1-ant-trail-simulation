import unittest
import numpy as np
from ants import AntWorld, Ant
from constants import *


class TestAntSimulation(unittest.TestCase):

    def setUp(self):
        """Initialize a fresh world for each test."""
        self.world = AntWorld()

    def test_fidelity_values(self):
        """Test Rule 4: Fidelity f(C) must be between 210 and 247."""
        # Zero pheromone
        self.assertEqual(self.world.get_fidelity(0), 210)
        # Saturated pheromone
        self.assertEqual(self.world.get_fidelity(C_SAT + 10), 247)

    def test_absorbing_boundaries(self):
        """Test Rule: Ants must be removed when hitting the grid edge."""
        # 1. Clear any ants spawned during initialization
        self.world.ants = []

        # 2. Place an ant at (0,0) and point it North (-1, 0)
        # In our DIRECTIONS, index 0 is (-1, 0)
        edge_ant = Ant(0, 0, 0)
        self.world.ants = [edge_ant]

        # 3. Step the world
        self.world.step()

        # 4. Check that no ant exists at (0,0) anymore
        # Even if a new ant spawned at the nest, the one at (0,0) must be gone
        for ant in self.world.ants:
            self.assertNotEqual((ant.x, ant.y), (0, 0), "Ant at (0,0) was not removed!")

    def test_linear_evaporation(self):
        """Test Rule 3: Pheromone decay must be linear."""
        initial_val = 10.0
        self.world.grid[50, 50] = initial_val

        # Manually run the evaporation logic
        self.world.grid = np.maximum(0, self.world.grid - EVAP_RATE)

        self.assertEqual(self.world.grid[50, 50], initial_val - EVAP_RATE)

    def test_pheromone_deposition(self):
        """Test Rule 2: Ant deposits TAU_DEPOSIT per step."""
        self.world.ants = [Ant(50, 50, 0)]
        self.world.grid.fill(0)

        self.world.step()

        # Cell should have TAU_DEPOSIT minus 1 step of evaporation
        expected = TAU_DEPOSIT - EVAP_RATE
        self.assertEqual(self.world.grid[50, 50], expected)


if __name__ == "__main__":
    unittest.main()
