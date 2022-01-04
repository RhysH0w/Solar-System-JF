import pygame


class planetstats:
    def __init__(self, screen, length, name, radius, colour, speed):
        self.screen = screen
        self.length = length
        self.name = name
        self.radius = radius
        self.colour = colour
        self.speed = speed

    def drawplanetboi(self):
        x = 500 + self.length
        y = 300
        pygame.draw.circle(self.screen, self.colour, (500, 300), self.length + 20, 1)
        pygame.draw.circle(self.screen, self.colour, (x, y), self.radius)





