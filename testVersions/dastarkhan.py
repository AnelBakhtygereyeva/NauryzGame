import pygame
import time


def main():

    class Cube(pygame.sprite.Sprite):
        def __init__(self, image, side_length, side_length2, x, y, group):
            super().__init__()
            self.image = pygame.Surface((side_length, side_length2))
            self.image.set_colorkey((0, 0, 0))  # Set black as transparent color
            if isinstance(image, pygame.Surface):
                self.image.blit(image, (0, 0))
            else:
                # Load the image if it's not a pygame.Surface
                loaded_image = pygame.image.load(image).convert()
                loaded_image.set_colorkey((0, 0, 0))  # Set black as transparent color
                self.image.blit(loaded_image, (0, 0))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.group = group

    class Girl(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.girl_still = pygame.transform.scale(pygame.image.load("images/still.png"), (300, 300))
            self.girl_up1 = pygame.transform.scale(pygame.image.load("images/upMove.png"), (300, 300))
            self.girl_up2 = pygame.transform.scale(pygame.image.load("images/upMove2.png"), (300, 300))
            self.girl_down1 = pygame.transform.scale(pygame.image.load("images/down.png"), (300, 300))
            self.girl_down2 = pygame.transform.scale(pygame.image.load("images/down2.png"), (300, 300))
            self.girl_right1 = pygame.transform.scale(pygame.image.load("images/right.png"), (300, 300))
            self.girl_right2 = pygame.transform.scale(pygame.image.load("images/right2.png"), (300, 300))
            self.girl_left1 = pygame.transform.flip(self.girl_right1, True, False)
            self.girl_left2 = pygame.transform.flip(self.girl_right2, True, False)
            self.image = self.girl_still
            self.rect = pygame.Rect(0, 0, 1, 1)
            self.rect.center = (300, 300)
            self.move_speed = 10
            self.image_counter = 0


    pygame.init()

    width = 1400
    height = 800
    screen = pygame.display.set_mode((width, height))

    bg = pygame.transform.scale(pygame.image.load("images/kover.png"), (1400,800))
    
    red = (255, 0, 0)
    red_surface = pygame.Surface((80, 80))  # Create a surface with the desired dimensions
    red_surface.fill(red)
    green = pygame.transform.scale(pygame.image.load("images/besh.png"), (200, 200))
    blue = (0, 0, 255)
    yellow = (0, 128, 128)
    new = (125, 125, 125)
    gray = pygame.transform.scale(pygame.image.load("images/dastarkhan.png"), (452, 452))
    kids = pygame.transform.scale(pygame.image.load("images/kids.png"), (1400,800))
    kidsRect = kids.get_rect()
    pygame.display.set_caption("Red Cube!")

    white = (255, 255, 255)
    Fps = 60
    Clock = pygame.time.Clock()



    red_cube = Cube(red_surface, 80,80, 300, 300, "red")


    green_cube = Cube(green, 200, 200, 300, 600, "good")
    blue_cube = Cube(gray, 100, 100, 100, 100, "bad")
    dastarkhan = Cube(gray, 450, 450,  width // 2 - 225, height // 2 - 200, "dastarkhan")
    no = Cube(gray, 275, 400,  width // 2 - 150, height // 2 - 170, "dastarkhan")
    no2 = Cube(gray, 390, 265,  width // 2 - 210, height // 2 - 130, "dastarkhan")
    new = Cube(gray, 100,100, 1200, 300, "good")

    all_sprites = pygame.sprite.Group()
    good_sprites = pygame.sprite.Group()
    bad_sprites = pygame.sprite.Group()
    dastarkhan_sprites = pygame.sprite.Group()
    red_sprites = pygame.sprite.Group()

    all_sprites.add(red_cube, green_cube, blue_cube, dastarkhan)

    food = [green_cube, blue_cube, new]

    for i in food:
        if i.group == "good":
            good_sprites.add(i)
        elif i.group == "bad":
            bad_sprites.add(i)


    if dastarkhan.group == "dastarkhan":
        dastarkhan_sprites.add(no)
        dastarkhan_sprites.add(no2)
    if red_cube.group == "red":
        red_sprites.add(red_cube)

    run = True
    while run:
        screen.blit(kids, (0,0))
        screen.blit(no.image, no.rect)
        screen.blit(no2.image, no2.rect)        
        screen.blit(dastarkhan.image, dastarkhan.rect)
        screen.blit(red_cube.image, red_cube.rect)
        screen.blit(green_cube.image, green_cube.rect)
        screen.blit(blue_cube.image, blue_cube.rect)
        screen.blit(new.image, new.rect)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    red_cube.rect.y -= 10
                elif event.key == pygame.K_DOWN:
                    red_cube.rect.y += 10
                elif event.key == pygame.K_LEFT:
                    red_cube.rect.x -= 10
                elif event.key == pygame.K_RIGHT:
                    red_cube.rect.x += 10


        # Collision detection
        if pygame.sprite.spritecollide(red_cube, good_sprites, False):
            for sprite in good_sprites:
                if pygame.sprite.collide_rect(red_cube, sprite):
                    if sprite == green_cube:
                        # Collision with green_cube
                        pygame.mixer.Sound("ackanoid/catch.mp3").play()
                        green_cube.rect.center = (width // 2, height // 2 + 25)
                    elif sprite == new:
                        # Collision with new
                        pygame.mixer.Sound("ackanoid/catch.mp3").play()
                        new.rect.center = (width // 2 - 100, height // 2 - 80)

        if pygame.sprite.spritecollide(red_cube, bad_sprites, False):
            for sprite in bad_sprites:
                if pygame.sprite.collide_rect(red_cube, sprite):
                    if sprite == blue_cube:
                        mini_screen_bad = pygame.Surface((500, 250))  # Create a mini screen surface
                        mini_screen_bad.fill((255, 0, 0))
                        screen.blit(mini_screen_bad, dest=(width // 2 - 250, height // 2 - 125))
                        pygame.display.update()  # Update the display to show the new color
                        pygame.time.delay(1000)
                        blue_cube.image = pygame.Surface((70, 70))
                        blue_cube.rect = blue_cube.image.get_rect(center=(1200, 100))
                        

        if pygame.sprite.spritecollideany(red_cube, dastarkhan_sprites):
            mini_screen = pygame.Surface((500, 250))  # Create a mini screen surface
            mini_screen.fill((128, 0, 128))  # Fill the mini screen with purple color
            red_cube.rect.center = (300, 300)
            screen.blit(mini_screen, dest=(width // 2 - 250, height // 2 - 125))
            pygame.display.update()  # Update the display to show the new color
            pygame.time.delay(1000)
            

        pygame.display.flip()

        Clock.tick(60)
        pygame.display.update()
main()