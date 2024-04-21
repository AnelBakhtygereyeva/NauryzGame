import pygame
from pygame.locals import *


def main():
    class Girl(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.girl_still = pygame.transform.scale(pygame.image.load("images/default.png"), (300, 300))
            self.girl_up1 = pygame.transform.scale(pygame.image.load("images/up1.png"), (300, 300))
            self.girl_up2 = pygame.transform.scale(pygame.image.load("images/up2.png"), (300, 300))
            self.girl_down1 = pygame.transform.scale(pygame.image.load("images/down1.png"), (300, 300))
            self.girl_down2 = pygame.transform.scale(pygame.image.load("images/down2.png"), (300, 300))
            self.girl_right1 = pygame.transform.scale(pygame.image.load("images/right1.png"), (300, 300))
            self.girl_right2 = pygame.transform.scale(pygame.image.load("images/right2.png"), (300, 300))
            self.girl_left1 = pygame.transform.flip(self.girl_right1, True, False)
            self.girl_left2 = pygame.transform.flip(self.girl_right2, True, False)
            self.image = self.girl_still
            self.rect = pygame.Rect(0, 0, 1, 1)
            self.rect.center = (300, 300)
            self.move_speed = 10
            self.image_counter = 0

        def update(self):
            pass

    class Cube(pygame.sprite.Sprite):
        def __init__(self, image, side_length, side_length2, x, y, group):
            super().__init__()
            self.image = pygame.Surface((side_length, side_length2))
            self.image.set_colorkey((0, 0, 0))
            if isinstance(image, pygame.Surface):
                self.image.blit(image, (0, 0))
            else:
                loaded_image = pygame.image.load(image)
                loaded_image.set_colorkey((0, 0, 0))
                self.image.blit(loaded_image, (0, 0))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.group = group




    pygame.init()

    fps = 60
    clock = pygame.time.Clock()
    width = 1400
    height = 800

    screen = pygame.display.set_mode((width, height))


    background = pygame.transform.scale(pygame.image.load("images/koverBesh.png"), (width, height))
    besh = pygame.transform.scale(pygame.image.load("images/besh.png"), (200, 200))
    dast = pygame.transform.scale(pygame.image.load("images/dastarkhan.png"), (452, 452))
    test1 = (0, 0, 255)
    test2 = (125, 125, 125)

    red = (255, 0, 0)
    red_surface = pygame.Surface((80, 80))
    red_surface.fill(red)
    blue = (0, 0, 255)
    blue_surface = pygame.Surface((80, 80))
    blue_surface.fill(blue)

    dastarkhan = pygame.transform.scale(pygame.image.load("images/dastarkhan.png"), (452, 452))

    besh_cube = Cube(besh, 200, 200, 300, 600, "good")
    blue_cube = Cube(besh, 100, 100, 100, 100, "bad")
    dastarkhan = Cube(dast, 450, 450,  width // 2 - 225, height // 2 - 200, "dastarkhan")
    no = Cube(red_surface, 250, 400,  width // 2 - 140, height // 2 - 190, "dastarkhan")
    no2 = Cube(blue_surface, 400, 250,  width // 2 - 210, height // 2 - 130, "dastarkhan")
    new = Cube(besh, 100,100, 1200, 300, "good")

    
    all_sprites = pygame.sprite.Group()
    good_sprites = pygame.sprite.Group()
    bad_sprites = pygame.sprite.Group()
    dastarkhan_sprites = pygame.sprite.Group()
    girl = Girl()

    all_sprites.add(girl, besh_cube, blue_cube, dastarkhan)

    food = [besh_cube, blue_cube, new]

    for i in food:
        if i.group == "good":
            good_sprites.add(i)
        elif i.group == "bad":
            bad_sprites.add(i)

    if dastarkhan.group == "dastarkhan":
        dastarkhan_sprites.add(no)
        dastarkhan_sprites.add(no2)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    girl.rect.y -= girl.move_speed
                    if girl.image_counter % 2 == 0:
                        girl.image = girl.girl_up1
                    else:
                        girl.image = girl.girl_up2
                    girl.image_counter += 1
                elif event.key == K_DOWN:
                    girl.rect.y += girl.move_speed
                    if girl.image_counter % 2 == 0:
                        girl.image = girl.girl_down1
                    else:
                        girl.image = girl.girl_down2
                    girl.image_counter += 1
                elif event.key == K_RIGHT:
                    girl.rect.x += girl.move_speed
                    if girl.image_counter % 2 == 0:
                        girl.image = girl.girl_right1
                    else:
                        girl.image = girl.girl_right2
                    girl.image_counter += 1
                elif event.key == K_LEFT:
                    girl.rect.x -= girl.move_speed
                    if girl.image_counter % 2 == 0:
                        girl.image = girl.girl_left1
                    else:
                        girl.image = girl.girl_left2
                    girl.image_counter += 1

        all_sprites.update()

        screen.blit(background, (0, 0))
        
       
        screen.blit(no.image, no.rect)
        screen.blit(no2.image, no2.rect)
        screen.blit(besh_cube.image, besh_cube.rect)
        screen.blit(blue_cube.image, blue_cube.rect)
        screen.blit(new.image, new.rect)
        screen.blit(girl.image, girl.rect)
        screen.blit(dastarkhan.image, dastarkhan.rect)


        if pygame.sprite.spritecollide(girl, good_sprites, False):
            for sprite in good_sprites:
                if sprite == besh_cube:
                    pygame.mixer.Sound("ackanoid/catch.mp3").play()
                    besh.rect.center = (width // 2, height // 2 + 25)
                elif sprite == new:
                    pygame.mixer.Sound("ackanoid/catch.mp3").play()
                    new.rect.center = (width // 2 - 100, height // 2 - 80)

        if pygame.sprite.spritecollide(girl, bad_sprites, False):
            for sprite in bad_sprites:
                if pygame.sprite.collide_rect(girl, sprite):
                    if sprite == blue_cube:
                        mini_screen_bad = pygame.Surface((500, 250))
                        mini_screen_bad.fill((255, 0, 0))
                        screen.blit(mini_screen_bad, dest=(width // 2 - 250, height // 2 - 125))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        blue_cube.image = pygame.Surface((70, 70))
                        blue_cube.rect = blue_cube.image.get_rect(center=(1200, 100))
                        

        if pygame.sprite.spritecollideany(girl, dastarkhan_sprites):
            mini_screen = pygame.Surface((500, 250))
            mini_screen.fill((128, 0, 128))
            girl.rect.center = (300, 300)
            screen.blit(mini_screen, dest=(width // 2 - 250, height // 2 - 125))
            pygame.display.update()
            pygame.time.delay(1000)



        pygame.display.flip()
        clock.tick(fps)
        pygame.display.update()

    pygame.quit()
main()