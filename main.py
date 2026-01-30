import pygame
import os
from constants import *
from ants import AntWorld
from screen import Button, Panel, Slider, TextUI

pygame.init()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Ant Trail Formation")
clock = pygame.time.Clock()

# ======================
# LOAD ANT SPRITES
# ======================
ANT_SIZE = 8

ANT_IMG = pygame.image.load(os.path.join("assets", "ant.png")).convert_alpha()

ANT_IMG = pygame.transform.scale(ANT_IMG, (ANT_SIZE, ANT_SIZE))

ANT_SPRITES = [pygame.transform.rotate(ANT_IMG, -i * 45) for i in range(8)]

# ======================
# SIMULATION
# ======================
world = AntWorld()

panel = Panel()
reset_btn = Button("Reset")

fidelity_slider = Slider(Width - 330, 200, 0, 0, 255, 200, 10, max=255)
deposit_slider = Slider(Width - 330, 260, 0, 0, 20, 200, 10, max=20)
evap_slider = Slider(Width - 330, 320, 0, 0, 5, 200, 10, max=5)

running = True

while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    clicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True

    # ======================
    # UI
    # ======================
    panel.Render(screen)
    reset_btn.Render(screen)

    world.fidelity = int(fidelity_slider.Render(screen))
    world.deposit = int(deposit_slider.Render(screen))
    world.evaporation = int(evap_slider.Render(screen))

    TextUI("Fidelity", (Width - 250, 190), WHITE).Render(screen)
    TextUI("Deposit", (Width - 250, 250), WHITE).Render(screen)
    TextUI("Evaporation", (Width - 250, 310), WHITE).Render(screen)

    if reset_btn.state:
        world = AntWorld()

    # ======================
    # UPDATE MODEL
    # ======================
    world.step()

    # ======================
    # DRAW PHEROMONES
    # ======================
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            val = world.grid[x, y]
            if val > 0:
                c = min(255, int(val * 4))
                pygame.draw.rect(
                    screen,
                    (c, c, c),
                    (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                )

    # ======================
    # DRAW ANTS (ON TOP)
    # ======================
    for ant in world.ants:
        screen.blit(
            ANT_SPRITES[ant.direction],
            (ant.x * CELL_SIZE - ANT_SIZE // 2, ant.y * CELL_SIZE - ANT_SIZE // 2),
        )

    pygame.display.flip()

pygame.quit()
