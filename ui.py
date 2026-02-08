import pygame
from constants import *


class UI:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 16)

        # Adding in the image of the ant into the simulation
        try:
            # Statement will try to load in the image and then scale it down to make it fit into the cell
            self.ant_img = pygame.image.load("assets/ant.png").convert_alpha()
            self.ant_img = pygame.transform.scale(
                self.ant_img, (CELL_SIZE * 3, CELL_SIZE * 3)  # setting up image size
            )
        except:
            # Make a print out statement if the image cannot be found and will draw out circles instead
            print(
                "Your ant image cannot be found, reseting to the default option of drawing out circles."
            )
            self.ant_img = None  # no reason to set up the image size

    def render(self, screen, world, step):
        """
        Used for the UI screen to make sure the screen and the ants show up as intended

        Args:
            screen:an int used to set up the display that can be updated
            world: argument used to draw the trails and render out the ants
            step: int to display the timestep on the screen

        Returns:
            None no return statement at the end of this function
        """
        screen.fill(BLACK)

        # --- RENDER TRAILS (High Contrast for Fig 3) ---
        # Instead of iterating through every pixel with a loop (slow),
        # we find where pheromones exist and draw them.
        trail_indices = np.argwhere(world.grid > 1.0)
        for x, y in trail_indices:
            val = world.grid[x, y]
            # Map concentration to brightness (yellow)
            brightness = min(255, int(val * 15))
            pygame.draw.rect(
                screen,
                (brightness, brightness, 0),
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )

        # --- RENDER ANTS ---
        for ant in world.ants:
            if self.ant_img:
                angle = -ant.direction * 45
                rotated_ant = pygame.transform.rotate(self.ant_img, angle)
                rect = rotated_ant.get_rect(
                    center=(ant.x * CELL_SIZE, ant.y * CELL_SIZE)
                )
                screen.blit(rotated_ant, rect)
            else:
                pygame.draw.circle(
                    screen, WHITE, (ant.x * CELL_SIZE, ant.y * CELL_SIZE), 1
                )

        txt = self.font.render(
            f"Step: {step} | Ants: {len(world.ants)}", True, (200, 200, 200)
        )
        screen.blit(txt, (10, 10))
