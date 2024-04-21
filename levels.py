import pygame 
import sys
from pygame.locals import*
import random, time

def main():
    pygame.init()

    W, H = 1400, 800
    FPS = 60
    screen = pygame.display.set_mode((W, H))
    level1 = pygame.transform.scale(pygame.image.load("images/lvl1.png"), (1400, 800))

    clock = pygame.time.Clock()
    pygame.mixer.Sound("sounds/level.mp3").play()

    while True:
        screen.blit(level1, (0,0))

        nextButton = pygame.transform.scale(pygame.image.load("images/unpbnext.png"), (400, 280))
        nextRect = nextButton.get_rect()
        nextRect.center = (1200, 700)
        screen.blit(nextButton, nextRect)

        mainButton = pygame.transform.scale(pygame.image.load("images/unpbmain.png"), (400, 280))
        mainRect = mainButton.get_rect()
        mainRect.center = (200, 700)
        screen.blit(mainButton, mainRect)

        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nextRect.collidepoint(event.pos):
                    nextButton = pygame.transform.scale(pygame.image.load("images/pbnext.png"), (400, 280))
                    nextRect = nextButton.get_rect()
                    nextRect.center = (1200, 707)
                    screen.blit(nextButton, nextRect)
                    pygame.mixer.Sound("sounds/click.mp3").play()
                if mainRect.collidepoint(event.pos):
                    mainButton = pygame.transform.scale(pygame.image.load("images/pbmain.png"), (400, 280))
                    mainRect = mainButton.get_rect()
                    mainRect.center = (200, 707)
                    screen.blit(mainButton, mainRect)
                    pygame.mixer.Sound("sounds/click.mp3").play()
            elif event.type == pygame.MOUSEBUTTONUP:
                if nextRect.collidepoint(event.pos):
                    import kyzkuu
                    kyzkuu.main()
                if mainRect.collidepoint(event.pos):
                    import game
                    game.main()

    

        pygame.display.update()
        clock.tick(60)

def main2():
    pygame.init()

    W, H = 1400, 800
    FPS = 60
    screen = pygame.display.set_mode((W, H))
    level2 = pygame.transform.scale(pygame.image.load("images/lvl2.png"), (1400, 800))

    clock = pygame.time.Clock()
    pygame.mixer.Sound("sounds/level.mp3").play()

    while True:
        screen.blit(level2, (0,0))

        nextButton = pygame.transform.scale(pygame.image.load("images/unpbnext.png"), (400, 280))
        nextRect = nextButton.get_rect()
        nextRect.center = (1200, 700)
        screen.blit(nextButton, nextRect)

        mainButton = pygame.transform.scale(pygame.image.load("images/unpbmain.png"), (400, 280))
        mainRect = mainButton.get_rect()
        mainRect.center = (200, 700)
        screen.blit(mainButton, mainRect)

        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nextRect.collidepoint(event.pos):
                    nextButton = pygame.transform.scale(pygame.image.load("images/pbnext.png"), (400, 280))
                    nextRect = nextButton.get_rect()
                    nextRect.center = (1200, 707)
                    screen.blit(nextButton, nextRect)
                    pygame.mixer.Sound("sounds/click.mp3").play()
                if mainRect.collidepoint(event.pos):
                    mainButton = pygame.transform.scale(pygame.image.load("images/pbmain.png"), (400, 280))
                    mainRect = mainButton.get_rect()
                    mainRect.center = (200, 707)
                    screen.blit(mainButton, mainRect)
                    pygame.mixer.Sound("sounds/click.mp3").play()
            elif event.type == pygame.MOUSEBUTTONUP:
                if nextRect.collidepoint(event.pos):
                    import asyk
                    asyk.main()
                if mainRect.collidepoint(event.pos):
                    import game
                    game.main()
    

        pygame.display.update()
        clock.tick(60)

def main3():
    pygame.init()

    W, H = 1400, 800
    FPS = 60
    screen = pygame.display.set_mode((W, H))
    level3 = pygame.transform.scale(pygame.image.load("images/lvl3.png"), (1400, 800))

    clock = pygame.time.Clock()
    pygame.mixer.Sound("sounds/level.mp3").play()

    while True:
        screen.blit(level3, (0,0))

        nextButton = pygame.transform.scale(pygame.image.load("images/unpbnext.png"), (400, 280))
        nextRect = nextButton.get_rect()
        nextRect.center = (1200, 700)
        screen.blit(nextButton, nextRect)

        mainButton = pygame.transform.scale(pygame.image.load("images/unpbmain.png"), (400, 280))
        mainRect = mainButton.get_rect()
        mainRect.center = (200, 700)
        screen.blit(mainButton, mainRect)

        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nextRect.collidepoint(event.pos):
                    nextButton = pygame.transform.scale(pygame.image.load("images/pbnext.png"), (400, 280))
                    nextRect = nextButton.get_rect()
                    nextRect.center = (1200, 707)
                    screen.blit(nextButton, nextRect)
                    pygame.mixer.Sound("sounds/click.mp3").play()
                if mainRect.collidepoint(event.pos):
                    mainButton = pygame.transform.scale(pygame.image.load("images/pbmain.png"), (400, 280))
                    mainRect = mainButton.get_rect()
                    mainRect.center = (200, 707)
                    screen.blit(mainButton, mainRect)
                    pygame.mixer.Sound("sounds/click.mp3").play()
            elif event.type == pygame.MOUSEBUTTONUP:
                if nextRect.collidepoint(event.pos):
                    import dastarkhan
                    dastarkhan.main()
                if mainRect.collidepoint(event.pos):
                    import game
                    game.main()
    

        pygame.display.update()
        clock.tick(60)


