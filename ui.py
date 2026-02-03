import pygame
from constants import *


class UI:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 18)

    def render(self, screen, step_count, ant_count):
        # Panel Background
        pygame.draw.rect(screen, (30, 30, 30), (WIDTH - 180, 0, 180, 100))

        # Stats
        step_txt = self.font.render(f"Step: {step_count}", True, WHITE)
        ant_txt = self.font.render(f"Ants: {ant_count}", True, WHITE)
        reset_txt = self.font.render("Press 'R' to Reset", True, (200, 200, 200))

        screen.blit(step_txt, (WIDTH - 170, 10))
        screen.blit(ant_txt, (WIDTH - 170, 35))
        screen.blit(reset_txt, (WIDTH - 170, 70))
