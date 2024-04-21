import pygame
from pygame.locals import *
import time

def main():

    class Girl(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.girl_still = pygame.transform.scale(pygame.image.load("images/default.png"), (100, 100))
            self.girl_up1 = pygame.transform.scale(pygame.image.load("images/up1.png"), (100, 100))
            self.girl_up2 = pygame.transform.scale(pygame.image.load("images/up2.png"), (100, 100))
            self.girl_down1 = pygame.transform.scale(pygame.image.load("images/down1.png"), (100, 100))
            self.girl_down2 = pygame.transform.scale(pygame.image.load("images/down2.png"), (100, 100))
            self.girl_right1 = pygame.transform.scale(pygame.image.load("images/right1.png"), (100, 100))
            self.girl_right2 = pygame.transform.scale(pygame.image.load("images/right2.png"), (100, 100))
            self.girl_left1 = pygame.transform.scale(pygame.image.load("images/left1.png"), (100, 100))
            self.girl_left2 = pygame.transform.scale(pygame.image.load("images/left2.png"), (100, 100))
            self.image = self.girl_still
            self.rect = pygame.Rect(0, 0, 80, 80)
            self.rect.center = (300, 300)
            self.move_speed = 10
            self.image_counter = 0


    class Cube(pygame.sprite.Sprite):
        def __init__(self, image, side_length, side_length2, x, y, group):
            super().__init__()
            self.image = pygame.Surface((side_length, side_length2))
            self.image.set_colorkey((0, 0, 0))  # to make transparent in the background
            if isinstance(image, pygame.Surface):
                self.image.blit(image, (0, 0))
            else:
                # loading the image (if it's not a pygame.Surface)
                loaded_image = pygame.image.load(image).convert()
                loaded_image.set_colorkey((0, 0, 0))  # to make background transparent
                self.image.blit(loaded_image, (0, 0))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.group = group

    class Bomb(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(pygame.image.load("images/bomb.png"), (50, 50))
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()


    #initialize pygame and seting up the screen
    pygame.init()
    fps = 60
    clock = pygame.time.Clock()
    width = 1400
    height = 800
    screen = pygame.display.set_mode((width, height))
    count = 0

    #background and images
    background = pygame.transform.scale(pygame.image.load("images/koverBesh.png"), (width, height))
    besh = pygame.transform.scale(pygame.image.load("images/besh.png"), (200, 200))
    dast = pygame.transform.scale(pygame.image.load("images/dastarkhan.png"), (452, 452))
    burgerIm = pygame.transform.scale(pygame.image.load("images/burger.png"), (100, 100))
    baursakIm = pygame.transform.scale(pygame.image.load("images/baursak.png"), (100, 100))
    kozheIm = pygame.transform.scale(pygame.image.load("images/kozhe.png"), (100, 100))
    pizzaIm = pygame.transform.scale(pygame.image.load("images/pizza.png"), (100, 100))
    kurtIm = pygame.transform.scale(pygame.image.load("images/kurt.png"), (100, 100))
    donutIm = pygame.transform.scale(pygame.image.load("images/donut.png"), (100, 100))
    baspa = pygame.transform.scale(pygame.image.load("images/baspa.png"), (500, 250))
    sarkyt = pygame.transform.scale(pygame.image.load("images/sarkyt.png"), (500, 250))
    good = pygame.transform.scale(pygame.image.load("images/good.png"), (1400, 800))
    fail = pygame.transform.scale(pygame.image.load("images/fail.png"), (1400, 800))

    step = pygame.mixer.Sound("sounds/step.mp3")
    step.set_volume(0.4)

    bgSound = pygame.mixer.Sound("sounds/dastBg.mp3")
    bgSound.set_volume(0.4)
    bgSound.play()

    bgPeople = pygame.mixer.Sound("sounds/dastPeople.mp3")
    bgPeople.set_volume(0.6)
    bgPeople.play()
    


    #creating sprites
    girl = Girl()
    besh_cube = Cube(besh, 200, 200, 300, 600, "good")
    burger = Cube(burgerIm, 100, 100, 100, 460, "bad")
    dastarkhan = Cube(dast, 450, 450,  width // 2 - 225, height // 2 - 200, "dastarkhan")
    no = Cube(dast, 250, 400,  width // 2 - 140, height // 2 - 190, "dastarkhan")
    no2 = Cube(dast, 400, 250,  width // 2 - 210, height // 2 - 130, "dastarkhan")
    baursak = Cube(baursakIm, 100, 100, 1100, 300, "good")
    kozhe = Cube(kozheIm, 100, 100, 250, 100, "good")
    pizza = Cube(pizzaIm, 100, 100, 650, 50, "bad")
    kurt = Cube(kurtIm, 100, 100, 1250, 650, "good")
    donut = Cube(donutIm, 100, 100, 1000, 550, "bad")

    bomb_group = pygame.sprite.Group()
    bomb1 = Bomb()
    bomb2 = Bomb()
    bomb3 = Bomb()
    bomb4 = Bomb()
    bomb5 = Bomb()
    bomb6 = Bomb()
    bomb7 = Bomb()

    bomb1.rect.topleft = (650, 650)
    bomb2.rect.topleft = (100, 200)
    bomb3.rect.topleft = (500, 100)
    bomb4.rect.topleft = (400, 450)
    bomb5.rect.topleft = (100, 700)
    bomb6.rect.topleft = (1250, 450)
    bomb7.rect.topleft = (1100, 700)
    bomb_group.add(bomb1, bomb2, bomb3, bomb4, bomb5, bomb6, bomb7)

    #creating sprite groups
    all_sprites = pygame.sprite.Group()
    good_sprites = pygame.sprite.Group()
    bad_sprites = pygame.sprite.Group()
    dastarkhan_sprites = pygame.sprite.Group()

    all_sprites.add(girl, burger, dastarkhan, besh_cube, burger, baursak, kozhe, pizza, kurt, donut, bomb1, bomb2, bomb3, bomb4, bomb5, bomb6, bomb7)

    #to iterate through it (saves time)
    food = [besh_cube, burger, baursak, burger, baursak, kozhe, pizza, kurt, donut]
    for i in food:
        if i.group == "good":
            good_sprites.add(i)
        elif i.group == "bad":
            bad_sprites.add(i)


    if dastarkhan.group == "dastarkhan":
        dastarkhan_sprites.add(no)
        dastarkhan_sprites.add(no2)
    

    #game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP and girl.rect.y >= 0:
                    girl.rect.y -= girl.move_speed
                    girl.image = girl.girl_up1 if girl.image_counter % 2 == 0 else girl.girl_up2
                    girl.image_counter += 1
                    step.play()
                elif event.key == K_DOWN and girl.rect.y <= height - 105:
                    girl.rect.y += girl.move_speed
                    girl.image = girl.girl_down1 if girl.image_counter % 2 == 0 else girl.girl_down2
                    girl.image_counter += 1
                    step.play()
                elif event.key == K_RIGHT and girl.rect.x <= width - 95:
                    girl.rect.x += girl.move_speed
                    girl.image = girl.girl_right1 if girl.image_counter % 2 == 0 else girl.girl_right2
                    girl.image_counter += 1
                    step.play()
                elif event.key == K_LEFT and girl.rect.x >= 0:
                    girl.rect.x -= girl.move_speed
                    girl.image = girl.girl_left1 if girl.image_counter % 2 == 0 else girl.girl_left2
                    girl.image_counter += 1
                    step.play()

        all_sprites.update()

        #drawing/rendering the images
        screen.blit(background, (0, 0))
        screen.blit(no.image, no.rect)
        screen.blit(no2.image, no2.rect)
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect)

        #counting how many good foods are caught
        if count == 7:
            bgSound.stop()
            bgPeople.stop()
            pygame.display.update()
            pygame.time.delay(1500)

            import win
            win.main()


 

        #collision detection and response logic
        if pygame.sprite.spritecollide(girl, good_sprites, False):
            for sprite in good_sprites:
                if pygame.sprite.collide_rect(girl, sprite):
                    if sprite == besh_cube:
                        pygame.mixer.Sound("ackanoid/catch.mp3").play()
                        besh_cube.rect.center = (width // 2, height // 2 + 25)
                        count += 1
                        pygame.mixer.Sound("sounds/food.mp3").play()
                    elif sprite == baursak:
                        pygame.mixer.Sound("ackanoid/catch.mp3").play()
                        baursak.rect.center = (width // 2 + 100, height // 2 - 80)
                        count += 1
                        pygame.mixer.Sound("sounds/food.mp3").play()
                    elif sprite == kurt:
                        pygame.mixer.Sound("ackanoid/catch.mp3").play()
                        kurt.rect.center = (width // 2 - 10, height // 2 + 120)
                        count += 1
                        pygame.mixer.Sound("sounds/food.mp3").play()
                    elif sprite == kozhe:
                        pygame.mixer.Sound("ackanoid/catch.mp3").play()
                        kozhe.rect.center = (width // 2 - 100, height // 2 - 80)
                        count += 1
                        pygame.mixer.Sound("sounds/food.mp3").play()

        if pygame.sprite.spritecollide(girl, bad_sprites, False):
            for sprite in bad_sprites:
                if pygame.sprite.collide_rect(girl, sprite):
                    if sprite == burger:
                        mini_screen_bad = pygame.Surface((500, 250))
                        mini_screen_bad.blit(sarkyt, (0,0))
                        screen.blit(mini_screen_bad, dest=(width // 2 - 250, height // 2 - 125))
                        pygame.display.update()
                        pygame.time.delay(1500)
                        pygame.mixer.Sound("sounds/sarkyt.mp3").play()
                        burger.rect = burger.image.get_rect(center=(1200, 100))
                        count += 1
                        
                    elif sprite == donut:
                        mini_screen_bad = pygame.Surface((500, 250))
                        mini_screen_bad.blit(sarkyt, (0,0))
                        screen.blit(mini_screen_bad, dest=(width // 2 - 250, height // 2 - 125))
                        pygame.display.update()
                        pygame.time.delay(1500)
                        pygame.mixer.Sound("sounds/sarkyt.mp3").play()
                        donut.rect = donut.image.get_rect(center=(1000, 130))
                        count += 1
                        
                    elif sprite == pizza:
                        mini_screen_bad = pygame.Surface((500, 250))
                        mini_screen_bad.blit(sarkyt, (0,0))
                        screen.blit(mini_screen_bad, dest=(width // 2 - 250, height // 2 - 125))
                        pygame.display.update()
                        pygame.time.delay(1500)
                        pygame.mixer.Sound("sounds/sarkyt.mp3").play()
                        pizza.rect = pizza.image.get_rect(center=(1100, 120))
                        count += 1
                        

        if pygame.sprite.spritecollideany(girl, dastarkhan_sprites):
            mini_screen = pygame.Surface((500, 250))
            mini_screen.blit(baspa, (0,0))
            girl.rect.center = (300, 300)
            pygame.mixer.Sound("sounds/no.mp3").play()
            screen.blit(mini_screen, dest=(width // 2 - 250, height // 2 - 125))
            pygame.display.update()
            
            pygame.time.delay(2000)
            


        if pygame.sprite.spritecollideany(girl, bomb_group):
            bgSound.stop()
            bgPeople.stop()
            screen.blit(fail, (0, 0))
            pygame.display.flip()
            pygame.mixer.Sound("sounds/boom.mp3").play()
            pygame.time.delay(1500)  #show the fail screen for 2 seconds
            import levels
            levels.main3()
            

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()