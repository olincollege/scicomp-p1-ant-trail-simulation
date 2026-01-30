import pygame
from constants import *


def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)


class Button:
    def __init__(
        self,
        text,
        position=(Width - 230, 600),
        w=100,
        h=50,
        border=10,
        color=(0, 0, 0),
        borderColor=(64, 123, 158),
    ):
        self.text = text
        self.position = position
        self.w = w
        self.h = h
        self.border = border
        self.temp = color
        self.color = color
        self.borderColor = borderColor
        self.font = "freesansbold.ttf"
        self.fontSize = 25
        self.textColor = (255, 255, 255)
        self.state = False
        self.action = None

    def HandleMouse(self, HoverColor=(100, 100, 100)):
        m = pygame.mouse.get_pos()
        self.state = False
        if self.position[0] <= m[0] <= self.position[0] + self.w:
            if self.position[1] <= m[1] <= self.position[1] + self.h:
                self.color = HoverColor
                if pygame.mouse.get_pressed()[0]:
                    self.color = (200, 200, 200)
                    self.state = True
            else:
                self.color = self.temp
        else:
            self.color = self.temp

    def Render(self, screen):
        self.HandleMouse()
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(self.text, True, self.textColor)
        textRect = text.get_rect(
            center=(self.position[0] + self.w // 2, self.position[1] + self.h // 2)
        )

        pygame.draw.rect(
            screen,
            self.borderColor,
            pygame.Rect(
                self.position[0] - self.border // 2,
                self.position[1] - self.border // 2,
                self.w + self.border,
                self.h + self.border,
            ),
        )
        pygame.draw.rect(
            screen,
            self.color,
            pygame.Rect(self.position[0], self.position[1], self.w, self.h),
        )
        screen.blit(text, textRect)


class Panel:
    def __init__(
        self, position=(Width - 350, 100), w=345, h=500, color=(8, 3, 12), alpha=128
    ):
        self.position = position
        self.w = w
        self.h = h
        self.color = color
        self.alpha = alpha

    def Render(self, screen):
        s = pygame.Surface((self.w, self.h))
        s.set_alpha(self.alpha)
        s.fill(self.color)
        screen.blit(s, self.position)


class TextUI:
    def __init__(self, text, position, fontColor):
        self.text = text
        self.position = position
        self.fontColor = fontColor
        self.font = "freesansbold.ttf"
        self.fontSize = 18

    def Render(self, screen):
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(self.text, True, self.fontColor)
        screen.blit(text, text.get_rect(center=self.position))


class Slider:
    def __init__(self, x, y, val, min1, max1, length, h, max=500):
        self.value = val
        self.x = x
        self.y = y
        self.h = h
        self.length = length
        self.max = max
        self.v = 0.4

    def Render(self, screen):
        mx, my = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.x <= mx <= self.x + self.length:
                self.v = (mx - self.x) / self.length

        self.value = int(self.v * self.max)

        pygame.draw.rect(screen, (50, 50, 50), (self.x, self.y, self.length, self.h))
        pygame.draw.rect(
            screen, (200, 200, 200), (self.x, self.y, int(self.v * self.length), self.h)
        )
        pygame.draw.circle(
            screen,
            (130, 213, 151),
            (int(self.x + self.v * self.length), self.y + self.h // 2),
            10,
        )
        return self.value
