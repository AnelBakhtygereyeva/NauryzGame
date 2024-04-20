# kyz.py

import pygame
from pygame.locals import *

def main():
    # Initialize Pygame
    pygame.init()

    FPS = 70
    Clock = pygame.time.Clock()
    W = 1400
    H = 800
    boy_x = 100  # Initial X position of the boy
    girl_x = 100  # Initial X position of the girl
    image_toggle = False  # Toggle for switching images
    girl_image_toggle = False  # Toggle for switching girl's images
    auto_move_counter = 0  # Counter for automating girl's movement

    catch_sound = pygame.mixer.Sound("racer/catch.mp3")

    # Set up the display
    DISPLAYSURF = pygame.display.set_mode((W, H))

    # Load images for boy
    imBoyDefault = pygame.transform.scale(pygame.image.load("images/boy.png"), (400, 350))
    imBoyMoved = pygame.transform.scale(pygame.image.load("images/boyMove.png"), (400, 350))

    # Load images for girl
    imGirlDefault = pygame.transform.scale(pygame.image.load("images/girl.png"), (400, 350))
    imGirlMoved = pygame.transform.scale(pygame.image.load("images/girlMove.png"), (400, 350))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_RIGHT:
                    # Check if moving right will exceed the 1200 pixels width border for the boy
                    if boy_x + 17 < 1200:
                        boy_x += 17
                        image_toggle = not image_toggle
                    else:
                        # Change the screen to green for 1 second
                        DISPLAYSURF.fill((0, 255, 0))  # Fill the screen with green
                        pygame.display.update()  # Update the display to show the new color
                        pygame.time.delay(1000)  # Wait for 1 second

                        import lvl1
                        lvl1.main2()
                    

        # Automate girl's movement and image toggle
        auto_move_counter += 1
        if auto_move_counter % 8 == 0:  # Change girl's position and image every 60 frames (~1 second at 60 FPS)
            if girl_x + 20 <= 1150:  # Move girl to the right
                girl_x += 20  # Reset girl's position if it exceeds the right border
                girl_image_toggle = not girl_image_toggle

        background = pygame.transform.scale(pygame.image.load("images/tree/frame1.png"), (1400, 800))
        DISPLAYSURF.blit(background, (0,0))

        # Choose the image based on the toggle state for the boy
        if image_toggle:
            imBoy = imBoyMoved
        else:
            imBoy = imBoyDefault

        # Choose the image based on the toggle state for the girl
        if girl_image_toggle:
            imGirl = imGirlMoved
        else:
            imGirl = imGirlDefault

        girlRect = imGirl.get_rect()
        girlRect.center = (girl_x, 500)  # Position the girl a bit above the boy
        DISPLAYSURF.blit(imGirl, girlRect)

        boyRect = imBoy.get_rect()
        boyRect.center = (boy_x, 650)
        DISPLAYSURF.blit(imBoy, boyRect)



        pygame.display.update()
        Clock.tick(FPS)