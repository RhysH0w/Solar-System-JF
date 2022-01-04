# importing and initiating the program
import pygame
import sys
from Planet import *

pygame.init()
pygame.font.init()

# defining the colours
black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 145, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
grey = (220, 220, 220)
light_blue = (28, 222, 229)

screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Solar System")
icon = pygame.image.load("Solar.jpg")
pygame.display.set_icon(icon)

Mercury = planetstats(screen, 20, "Mercury", 200, grey, 100)
Venus = planetstats(screen, 40, "Venus", 200, red, 100)
Earth = planetstats(screen, 60, "Earth", 200, light_blue, 100)
Mars = planetstats(screen, 80, "Mars", 200, orange, 100)
Jupiter = planetstats(screen, 120, "Jupiter", 200, grey, 100)

# screen boundaries/title/icon

# clock for defining the fps
clock = pygame.time.Clock()


def menu():
    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

        # registers mouse position
        mouseposition = pygame.mouse.get_pos()

        pygame.draw.rect(screen, red, [80, 255, 175, 60], 2)
        pygame.draw.rect(screen, blue, [500, 255, 150, 60], 2)

        # if event.type == pygame.MOUSEBUTTONDOWN and 80 < mouseposition[0] < 250 and 255 < mouseposition[1] < 300:
        # solarsubmenu()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseposition()[0] >= 150 and mouseposition()[1] >= 230:
                if mouseposition()[0] <= 250 and mouseposition()[1] <= 280:
                    solarsubmenu()

                    # changes colour of bg/drawing rectangles
        screen.fill(black)
        pygame.draw.rect(screen, red, [80, 255, 175, 60], 2)
        pygame.draw.rect(screen, blue, [500, 255, 150, 60], 2)
        # setting different fonts and adding them to the screen surface
        headingfont = pygame.font.SysFont("comicsans", 25, True, False)
        heading = headingfont.render("Solar System Main Menu!", True, white)
        screen.blit(heading, [50, 50])

        button1font = pygame.font.SysFont("comicsans", 25, True, False)
        buttontxt = button1font.render("Solar System", True, red)
        screen.blit(buttontxt, [89, 280])

        button2font = pygame.font.SysFont("comicsans", 25, True, False)
        button2txt = button2font.render("Instructions", True, blue)
        screen.blit(button2txt, [505, 270])

        menuimage = pygame.image.load("planets.jpg")
        screen.blit(pygame.transform.scale(menuimage, (300, 300)), (380, -50))

        pygame.display.update()


def solarsubmenu():
    screen.fill(black)

    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        mouseposition = pygame.mouse.get_pos()

        headingfont2 = pygame.font.SysFont("Calibri", 25, True, False)
        heading2 = headingfont2.render("The Solar System", True, red)
        screen.blit(heading2, [30, 30])
        submenubuttonfont = pygame.font.SysFont("comicsans", 25, True, False)
        submenubuttontxt = submenubuttonfont.render("Return", True, blue)
        screen.blit(submenubuttontxt, [15, 400])

        pygame.draw.rect(screen, blue, [10, 380, 70, 60], 2)

        pygame.draw.circle(screen, orange, [500, 250], 50)
        pygame.draw.circle(screen, white, [500, 250], 70, 2)
        pygame.draw.circle(screen, white, [500, 250], 90, 2)
        pygame.draw.circle(screen, white, [500, 250], 110, 2)
        pygame.draw.circle(screen, white, [500, 250], 130, 2)
        pygame.draw.circle(screen, white, [500, 250], 170, 2)
        pygame.draw.circle(screen, white, [500, 250], 240, 2)
        pygame.draw.circle(screen, white, [500, 250], 310, 2)
        pygame.draw.circle(screen, white, [500, 250], 310, 2)

        planetboi.planetstats(Mercury)
        planetboi.planetstats(Venus)
        planetboi.planetstats(Earth)
        planetboi.planetstats(Mars)
        planetboi.planetstats(Jupiter)
        planetboi.planetstats(Neptune)

        pygame.display.update()


def instructionsubmenu():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    mouseposition = pygame.mouse.get_pos()


solarsubmenu()



