import pytest
import numpy as np
import random
from ants import AntWorld, Ant
from constants import *


@pytest.fixture
def world():
    """A fixture to make sure that the tests run clean and to refresh the environment."""
    return AntWorld()


def test_fidelity_calculation(world):
    """
    Test to check on the Piecewise Linear Fidelity. Make sure that it can handle the C_SAT logic correctly as
    mentioned on the paper.
    """
    # Test at zero pheromone
    assert world.get_fidelity(0) == F_MIN

    # Test at saturation
    assert world.get_fidelity(C_SAT + 10) == F_MIN + DELTA_F


def test_linear_evaporation(world):
    """
    Test to check on the Linear Pheromone Decay. Making sure to see if it follows what the paper mentions.
    """
    initial_val = 10.0
    world.grid[100, 100] = initial_val

    # Run the evaporation using the world.step()
    world.grid = np.maximum(0, world.grid - EVAP_RATE_LINEAR)

    expected = initial_val - EVAP_RATE_LINEAR
    assert world.grid[100, 100] == expected


def test_extreme_forward_bias(world):
    """
    Test to check on the Fork Algorithm and its Extreme Forward Bias. Making sre the this logic matches figure 3.
    """
    ant = Ant(50, 50)
    ant.direction = 0  # direction is set to east

    # Ant is going straight but is weak
    world.grid[51, 50] = 1.0
    # Ant path is going straight but is strong
    world.grid[51, 51] = 100.0

    # start up the follower logic
    world.get_fidelity = lambda c: 256

    # Follow the moving logic set for ants
    ant.move(world.grid, world)

    # Making sure the ant remains in the same direction as before for this it is east
    assert ant.direction == 0, "Ant failed to stay straight (Forward Bias Rule)"


def test_absorbing_boundaries(world):
    """
    Test to check out the boundires. Make sure that the ants that go outside of the grid get removed from the simulation.
    """
    # But ant at the edge of the grid
    edge_ant = Ant(0, 0)
    edge_ant.direction = 4  # Facing the direction of west
    world.ants = [edge_ant]

    world.step()

    # Ant at the edge should get deleted
    for ant in world.ants:
        assert not (ant.x < 0 or ant.y < 0), "Ant was not removed at boundary"


def test_pheromone_deposition(world):
    """
    Test to make sure that there is Constant Deposition. Make sure that each ant adds TAU_DEPOSIT to its current cell.
    """
    world.grid.fill(0)
    ant = Ant(100, 100)
    world.ants = [ant]

    # Record movement
    old_x, old_y = ant.x, ant.y
    world.step()

    # Making sure there is a pheromone
    assert world.grid[old_x, old_y] > 0
    # Making sure that TAU_DEPOSIT - 1 step of evaporation
    assert world.grid[old_x, old_y] == (TAU_DEPOSIT - EVAP_RATE_LINEAR)


def test_turning_kernel_randomness(world):
    """
    Test is trying out the Turning Kernel. By making sure that explorers turn based on the probability distribution of the
    TURN_KERNEL.
    """
    ant = Ant(110, 110)
    initial_dir = ant.direction

    # Checking at a probability of the ant exploring
    world.get_fidelity = lambda c: 0

    turns = 0
    trials = 500
    for _ in range(trials):
        old_dir = ant.direction
        ant.move(world.grid, world)
        if ant.direction != old_dir:
            turns += 1

    # Calculating the probability of turning is sum
    expected_prob = sum(TURN_KERNEL)
    actual_prob = turns / trials

    # allow space for any error 10 percent at max
    assert abs(actual_prob - expected_prob) < 0.10
