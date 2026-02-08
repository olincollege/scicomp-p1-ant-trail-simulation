import pygame
from constants import *
from ants import AntWorld
from ui import UI


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    world, ui, step = AntWorld(), UI(), 0
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        world.step()
        ui.render(screen, world, step)
        pygame.display.flip()
        step += 1
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
