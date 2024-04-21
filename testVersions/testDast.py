import pygame

def main():
    pygame.init()

    width = 1400
    height = 800
    screen = pygame.display.set_mode((width, height))

    bg = pygame.transform.scale(pygame.image.load("images/kover.png"), (1400, 800))

    # Load images
    imageGirl = pygame.transform.scale(pygame.image.load("images/default.png"), (80, 80))
    upMove = pygame.transform.scale(pygame.image.load("images/up1.png"), (80, 80))
    upMove2 = pygame.transform.scale(pygame.image.load("images/up2.png"), (80, 80))
    upGirl = pygame.transform.scale(pygame.image.load("images/default.png"), (80, 80))

    # Initialize girl sprite
    girl_sprite = pygame.sprite.Sprite()
    girl_sprite.image = imageGirl
    girl_sprite.rect = girl_sprite.image.get_rect()
    girl_sprite.rect.topleft = (300, 300)

    # Movement variables
    move_up = False
    move_down = False
    move_left = False
    move_right = False

    # Movement speed
    speed = 5

    # Toggle variable for image change
    toggle = False

    # Main loop
    run = True
    while run:
        screen.blit(bg, (0, 0))  # Draw background

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                # Handle key presses
                if event.key == pygame.K_UP:
                    move_up = True
                elif event.key == pygame.K_DOWN:
                    move_down = True
                elif event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
            elif event.type == pygame.KEYUP:
                # Handle key releases
                if event.key == pygame.K_UP:
                    move_up = False
                elif event.key == pygame.K_DOWN:
                    move_down = False
                elif event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False

        # Move the girl sprite based on the movement variables
        if move_up:
            girl_sprite.rect.y -= speed
            if girl_sprite.image != upGirl:  # Change image if not already upGirl
                if toggle:
                    girl_sprite.image = upMove
                else:
                    girl_sprite.image = upMove2
                toggle = not toggle
        elif move_down:
            girl_sprite.rect.y += speed
        if move_left:
            girl_sprite.rect.x -= speed
        elif move_right:
            girl_sprite.rect.x += speed
        else:
            if girl_sprite.image != imageGirl:
                girl_sprite.image = imageGirl

        # Draw the girl sprite
        screen.blit(girl_sprite.image, girl_sprite.rect.topleft)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
