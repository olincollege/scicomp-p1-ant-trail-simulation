import pygame
import numpy as np
import sys
from constants import *
from ants import AntWorld


def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ant Trail CA: Watmough & Edelstein-Keshet")
    clock = pygame.time.Clock()

    # Initialize Model and UI
    world = AntWorld()
    font = pygame.font.SysFont("Arial", 20)
    step_count = 0

    running = True
    while running:
        # 1. Event Handling (Corrected)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for KEYDOWN first to avoid AttributeError
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    world = AntWorld()
                    step_count = 0
                if event.key == pygame.K_ESCAPE:
                    running = False

        # 2. Update Simulation
        world.step()
        step_count += 1

        # 3. Drawing
        screen.fill(BLACK)

        # Render Pheromones
        # We only look for cells with significant pheromone to speed up rendering
        active_cells = np.argwhere(world.grid > 0.1)
        for x, y in active_cells:
            val = world.grid[x, y]
            # Map concentration to brightness (White trails)
            # Multiplying by 15-20 makes the 'trunk' lines much more visible
            c_val = min(255, int(val * 15))
            pygame.draw.rect(
                screen,
                (c_val, c_val, c_val),
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )

        # Render Ants
        for ant in world.ants:
            # Followers are Red, Explorers are slightly darker Red
            color = (255, 50, 50) if ant.following else (150, 30, 30)
            pygame.draw.circle(
                screen, color, (int(ant.x * CELL_SIZE), int(ant.y * CELL_SIZE)), 2
            )

        # 4. UI Overlay
        # Displaying steps is important because lines take time to emerge
        stats_surf = font.render(
            f"Step: {step_count} | Ants: {len(world.ants)} | [R] Reset",
            True,
            (0, 255, 0),
        )
        screen.blit(stats_surf, (10, 10))

        pygame.display.flip()

        # Lowering FPS (defined in constants) allows you to see the line growth
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
