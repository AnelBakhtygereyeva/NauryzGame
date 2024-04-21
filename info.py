import pygame 
import sys
from pygame.locals import*
import random, time

def main():
    pygame.init()

    W, H = 1400, 800
    FPS = 60
    screen = pygame.display.set_mode((W, H))
    info = pygame.transform.scale(pygame.image.load("images/infoScreen.png"), (1400, 800))
    main_menu_bg = pygame.transform.scale(pygame.image.load("images/blurbg.png"), (1400, 900))

    clock = pygame.time.Clock()
    sound = pygame.mixer.Sound("sounds/info.mp3")
    sound.set_volume(0.3)
    sound.play()

    while True:
        screen.blit(main_menu_bg, (0,0))
        screen.blit(info, dest = (0, 40))

        mainButton = pygame.transform.scale(pygame.image.load("images/unpbmain.png"), (400, 280))
        mainRect = mainButton.get_rect()
        mainRect.center = (200, 730)
        screen.blit(mainButton, mainRect)

        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mainRect.collidepoint(event.pos):
                    mainButton = pygame.transform.scale(pygame.image.load("images/pbmain.png"), (400, 280))
                    mainRect = mainButton.get_rect()
                    mainRect.center = (200, 737)
                    screen.blit(mainButton, mainRect)
                    pygame.mixer.Sound("sounds/click.mp3").play()
            elif event.type == pygame.MOUSEBUTTONUP:
                if mainRect.collidepoint(event.pos):
                    sound.stop()
                    import game
                    game.main()
    

        pygame.display.update()
        clock.tick(60)