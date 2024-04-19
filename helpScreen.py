import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

def main():
    global screen
    pygame.init()
    
    #basic
    W, H = 1400, 800
    FPS = 60
    #some settings
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        screen.fill((255,255,255))

        backButton = pygame.transform.scale(pygame.image.load("images/unpbback.png"), (220, 110))
        backRect = backButton.get_rect()
        backRect.center = (W // 2, H // 2 - 20)
        screen.blit(backButton, backRect)

        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backRect.collidepoint(event.pos):
                    backButton = pygame.transform.scale(pygame.image.load("images/pbback.png"), (220, 110))
                    backRect = backButton.get_rect()
                    backRect.center = (W // 2, H // 2 - 13)
                    screen.blit(backButton, backRect)
            elif event.type == pygame.MOUSEBUTTONUP:
                if backRect.collidepoint(event.pos):
                    import screen
                    screen.main()
                    
        pygame.display.update()
        clock.tick(FPS)
main()