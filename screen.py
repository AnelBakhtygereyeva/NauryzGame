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
    main_menu_bg = pygame.transform.scale(pygame.image.load("images/blurbg.png"), (1400, 900))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                


        screen.blit(main_menu_bg, (0,0))

        imgTheme = pygame.transform.scale(pygame.image.load("images/nauryz.png"), (660, 220))
        imgThemeRect = imgTheme.get_rect()
        imgThemeRect.center = (W // 2, H // 2 - 160)
        screen.blit(imgTheme, imgThemeRect)

        playButton = pygame.transform.scale(pygame.image.load("images/unpbplay.png"), (220, 110))
        playRect = playButton.get_rect()
        playRect.center = (W // 2, H // 2 - 20)
        screen.blit(playButton, playRect)

        helpButton = pygame.transform.scale(pygame.image.load("images/unpbhelp.png"), (220, 110))
        helpRect = helpButton.get_rect()
        helpRect.center = (W // 2, H // 2 + 70)
        screen.blit(helpButton, helpRect)
        
        exitButton = pygame.transform.scale(pygame.image.load("images/unpbexit.png"), (220, 110))
        exitRect = exitButton.get_rect()
        exitRect.center = (W // 2, H // 2 + 180)
        screen.blit(exitButton, exitRect)

        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playRect.collidepoint(event.pos):
                    playButton = pygame.transform.scale(pygame.image.load("images/pbplay.png"), (220, 110))
                    playRect = playButton.get_rect()
                    playRect.center = (W // 2, H // 2 - 13)
                    screen.blit(playButton, playRect)
                if helpRect.collidepoint(event.pos):
                    helpButton = pygame.transform.scale(pygame.image.load("images/pbhelp.png"), (220, 110))
                    helpRect = playButton.get_rect()
                    helpRect.center = (W // 2, H // 2 + 77)
                    screen.blit(helpButton, helpRect)
                if exitRect.collidepoint(event.pos):
                    exitButton = pygame.transform.scale(pygame.image.load("images/pbexit.png"), (220, 110))
                    exitRect = exitButton.get_rect()
                    exitRect.center = (W // 2, H // 2 + 187)
                    screen.blit(exitButton, exitRect)
            elif event.type == pygame.MOUSEBUTTONUP:
                if playRect.collidepoint(event.pos):
                    import lvl1
                    lvl1.main()
                if helpRect.collidepoint(event.pos):
                    import lvl1
                    lvl1.main2()
                if exitRect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(60)
main()