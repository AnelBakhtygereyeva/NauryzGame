import pygame 
import sys
from pygame.locals import*
import random, time

def main():
    pygame.init()

    #basic
    W, H = 1400, 800
    FPS = 60
    #some settings
    screen = pygame.display.set_mode((W, H))
    level1 = pygame.transform.scale(pygame.image.load("images/levels.png"), (3500, 600))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        screen.fill((255,255,255))
        screen.blit(level1, (0,150))

        backButton = pygame.transform.scale(pygame.image.load("images/unpbback.png"), (220, 110))
        backRect = backButton.get_rect()
        backRect.center = (1200, 700)
        screen.blit(backButton, backRect)

        playButton = pygame.transform.scale(pygame.image.load("images/unpbplay.png"), (220, 110))
        playRect = playButton.get_rect()
        playRect.center = (200, 700)
        screen.blit(playButton, playRect)

        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backRect.collidepoint(event.pos):
                    backButton = pygame.transform.scale(pygame.image.load("images/pbback.png"), (220, 110))
                    backRect = backButton.get_rect()
                    backRect.center = (1200, 707)
                    screen.blit(backButton, backRect)
                if playRect.collidepoint(event.pos):
                    playButton = pygame.transform.scale(pygame.image.load("images/pbplay.png"), (220, 110))
                    playRect = playButton.get_rect()
                    playRect.center = (200, 707)
                    screen.blit(playButton, playRect)
            elif event.type == pygame.MOUSEBUTTONUP:
                if backRect.collidepoint(event.pos):
                    import kyz
                    kyz.main()
                if playRect.collidepoint(event.pos):
                    import screen
                    screen.main()
    

        pygame.display.flip()
        clock.tick(60)

def main2():
    pygame.init()

    #basic
    W, H = 1400, 800
    FPS = 60
    #some settings
    screen = pygame.display.set_mode((W, H))
    level1 = pygame.transform.scale(pygame.image.load("images/levels.png"), (3500, 600))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        screen.fill((255,255,255))
        screen.blit(level1, (0,150))

        backButton = pygame.transform.scale(pygame.image.load("images/unpbback.png"), (220, 110))
        backRect = backButton.get_rect()
        backRect.center = (1200, 700)
        screen.blit(backButton, backRect)

        playButton = pygame.transform.scale(pygame.image.load("images/unpbplay.png"), (220, 110))
        playRect = playButton.get_rect()
        playRect.center = (200, 700)
        screen.blit(playButton, playRect)

        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backRect.collidepoint(event.pos):
                    backButton = pygame.transform.scale(pygame.image.load("images/pbback.png"), (220, 110))
                    backRect = backButton.get_rect()
                    backRect.center = (1200, 707)
                    screen.blit(backButton, backRect)
                if playRect.collidepoint(event.pos):
                    playButton = pygame.transform.scale(pygame.image.load("images/pbplay.png"), (220, 110))
                    playRect = playButton.get_rect()
                    playRect.center = (200, 707)
                    screen.blit(playButton, playRect)
            elif event.type == pygame.MOUSEBUTTONUP:
                if backRect.collidepoint(event.pos):
                    import asykPREFINAL
                    asykPREFINAL.main()
                if playRect.collidepoint(event.pos):
                    import screen
                    screen.main()
    

        pygame.display.flip()
        clock.tick(60)

def main3():
    pygame.init()

    #basic
    W, H = 1400, 800
    FPS = 60
    #some settings
    screen = pygame.display.set_mode((W, H))
    level1 = pygame.transform.scale(pygame.image.load("images/levels.png"), (3500, 600))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        screen.fill((255,255,255))
        screen.blit(level1, (0,150))

        backButton = pygame.transform.scale(pygame.image.load("images/unpbback.png"), (220, 110))
        backRect = backButton.get_rect()
        backRect.center = (1200, 700)
        screen.blit(backButton, backRect)

        playButton = pygame.transform.scale(pygame.image.load("images/unpbplay.png"), (220, 110))
        playRect = playButton.get_rect()
        playRect.center = (200, 700)
        screen.blit(playButton, playRect)

        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backRect.collidepoint(event.pos):
                    backButton = pygame.transform.scale(pygame.image.load("images/pbback.png"), (220, 110))
                    backRect = backButton.get_rect()
                    backRect.center = (1200, 707)
                    screen.blit(backButton, backRect)
                if playRect.collidepoint(event.pos):
                    playButton = pygame.transform.scale(pygame.image.load("images/pbplay.png"), (220, 110))
                    playRect = playButton.get_rect()
                    playRect.center = (200, 707)
                    screen.blit(playButton, playRect)
            elif event.type == pygame.MOUSEBUTTONUP:
                if backRect.collidepoint(event.pos):
                    import screen
                    screen.main()
                if playRect.collidepoint(event.pos):
                    import screen
                    screen.main()
    

        pygame.display.flip()
        clock.tick(60)


