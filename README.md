<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#project-objectives">Project Objectives</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#capabilities-and-limitations">Capabilities and Limitations</a>
      <ul>
        <li><a href="#capabilities">Capabilities</a></li>
        <li><a href="#limitations">Limitations</a></li>
      </ul>
    </li>
    <li><a href="#scientific-benchmarking">Scientific Benchmarking</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#paper-documentation">Paper Documentation</a></li>
    <li><a href="#test-run">Test Run</a></li>
    <li><a href="#contributors">Contributors </a></li>
  </ol>
</details>

# About the Project 
![Alt text](/assets/ant-trail-walking-colony-black-600nw-2494508395.webp "Ant Trails")

This project comes from Franklin W. Olin College of Engineering's Scientific Computing Spring 2026 class. This is the first project, 
which focuses on agent-based following with ant trail formation. The project follows "Modelling the Formation of Trail Networks by 
Foraging Ants” James Watmough and Leah Edelstein-Keshet. The goal of this project is to to model ant trail formation using a 
cellular automata simulation, that looks similar to Figure 3 in the paper. 

## Project Objectives
* Agent-Based Modeling: Simulating hundreds of individual ants with their local sensing capabilities.
* The Fork Algorithm: Implementation of the extreme forward bias in order to create realistic branching structures.
* Verification: Using unit testing (via Pytest) to validate individual agent behaviors against the source paper's mathematical rules.

# Capabilities and Limitations

## Capabilities
* Discrete Network Formation: Successfully models the transition from random exploration to established foraging trunks.
* Parameter Tuning: Users can adjust fidelity ($\phi$), evaporation rates ($E$), and deposition ($\tau$) within constants.py to observe different network topologies.
* Rule-Based Verification: Includes a robust test suite ensuring that agent movement, pheromone decay, and boundary conditions align with the source material.

## Limitations
* Fixed Environment: Currently only supports a 220x220 grid; larger environments for the grid size may require optimization of the Numpy grid updates.
* Single Nest Logic: The simulation currently models a single source (the nest) and assumes ants move toward an infinite boundary rather than specific food sources.

# Scientific Benchmarking
This implementation is benchmarked against Case I (the Constant Fidelity) and Case II (the Piecewise Linear Fidelity) from the paper.
| Feature Type | Paper Rule | Code Implementation |
|---|---|---|
| Movement | Turning Kernel ($B_n$) | Discrete 8-neighbor direction selection via a probability distribution. |
| Following | Fork Algorithm | Implemented as "Extreme Forward Bias"—ants stay straight if a trail is sensed ahead. |
| Decay | Linear Evaporation | $C_{t+1} = \text{max}(0, C_t - E)$. |
| Boundry | Absorbing | Ants are removed upon reaching the lattice edge. |

# Built With
* Python and its libraries
    * Pygame
    * Numpy
    * Pytest


# Getting Started
Before getting started we need to set up the project to be to run on your machine locally. To get a local copy up and running 
follow these simple example steps.

## Prerequisites
These are the list of Python libraries needed to and how to install it. 
* Pygame
  ```sh
  pip install pygame
  ```
* Numpy
  ```sh
  pip install numpy
  ```

* Pytest
  ```sh
  pip install pytest
  ```

# Paper Documentation
* James Watmough, Leah Edelstein-Keshet,
Modelling the Formation of Trail Networks by Foraging Ants,
Journal of Theoretical Biology,
Volume 176, Issue 3,
1995,
Pages 357-371,
ISSN 0022-5193,
https://doi.org/10.1006/jtbi.1995.0205.
(https://www.sciencedirect.com/science/article/pii/S0022519385702056)
Abstract: This paper studies the role of chemical communication in the formation of trail networks by foraging ants. A cellular automaton model for the motion of the ants is formulated, which assumes that individuals interact according to a simple behavioural algorithm. The ants communicate by depositing trail markers composed of volatile chemicals that serve as attractants for other ants. The ants interact with the network both by following the trails and by extending and reinforcing the trails they follow. By varying the parameters describing these interactions we determine how variations in the behaviour of the individual ants lead to changes in the patterns of trail networks formed by the population. The results indicate that the ability of the group to form trails is inversely related with individual fidelity to trails.

* Please refer to the full paper linked below if you have any further questions or more research insights: 
[Link to the Full Paper](https://www.sciencedirect.com/science/article/abs/pii/S0022519385702056).



# Test Run
In order to run the visualization of the code please run this command on terminal. 
```sh
  python3 main.py
```

In order to test the validity of this code please run this command on terminal. 
```sh
  python3 -m pytest -v test_ants.py
  ```

# Contributors 
Titilayo Oshinowo-  GitHub:@titiooshy
