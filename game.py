"""
so the code was updated with these features:
-added some new coins(blue(but it looks black) coin with -1 score and black/yellow coin with +2 score)
-every 10 score the speed of the enemy car will increase
"""
import pygame
import sys
from pygame.locals import*
import random, time

score = 0

def main():
    global score
    pygame.init()

    FPS = 60
    Clock = pygame.time.Clock()
    #colors
    blue = (0, 0, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    width = 400
    height = 600
    speed = 5
    enemy_speed = 5
    score = 0
    speed_coin = 4
    score_coin = 0


    #fonts
    font = pygame.font.SysFont("Verdana", 60)
    font_small = pygame.font.SysFont("Verdana", 20)
    game_over = font.render("Game Over", True, black)
    #background image
    background = pygame.image.load("racer/AnimatedStreet.png")
    catch_sound = pygame.mixer.Sound("racer/catch.mp3")
    #creating screen
    DISPLAYSURF = pygame.display.set_mode((width, height))
    DISPLAYSURF.fill(white)
    pygame.display.set_caption(("Racer game!"))
    #classes of objects
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            image_enemy_car = pygame.image.load("racer/Enemy.png")
            self.image = pygame.transform.scale(image_enemy_car, (48,93))
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, width - 40), 0)

        def move(self):
            global score
            self.rect.move_ip(0, enemy_speed)
            if (self.rect.bottom > 600):
                score += 1
                self.rect.top = 0
                self.rect.center = (random.randint(40, width - 40), 0)

    class Coins(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            image_coin = pygame.image.load("racer/coin.png")
            self.image = pygame.transform.scale(image_coin, (40,40))
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, width - 40), 0)

        def move(self):
            self.rect.move_ip(0, speed_coin)
            if (self.rect.bottom > 600):
                self.rect.top = 0
                self.rect.center = (random.randint(40, width - 40), 0)

    class Coins2(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            image_coin = pygame.image.load("racer/bluecoin.svg")
            self.image = pygame.transform.scale(image_coin, (40,40))
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, width - 40), 0)

        def move(self):
            self.rect.move_ip(0, speed_coin)
            if (self.rect.bottom > 600):
                self.rect.top = 0
                self.rect.center = (random.randint(40, width - 40), 0)

    class Coins3(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            image_coin = pygame.image.load("racer/yellowcoin.svg")
            self.image = pygame.transform.scale(image_coin, (40,40))
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, width - 40), 0)

        def move(self):
            self.rect.move_ip(0, speed_coin)
            if (self.rect.bottom > 600):
                self.rect.top = 0
                self.rect.center = (random.randint(40, width - 40), 0)

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("racer/Player.png")
            self.rect = self.image.get_rect()
            self.rect.center = (160,520)

        def move(self):
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0 , 5)
            
            if self.rect.left > 0:
                if pressed_keys[K_LEFT]:
                    self.rect.move_ip(-5, 0)
            if self.rect.right < width:
                if pressed_keys[K_RIGHT]:
                    self.rect.move_ip(5, 0)
    #storing them in variables
    P1 = Player()
    E1 = Enemy()
    C1 = Coins()
    C2 = Coins2()
    C3 = Coins3()
    #adding into the groups
    enemies = pygame.sprite.Group()
    enemies.add(E1)

    coins = pygame.sprite.Group()
    coins.add(C1)

    coins2 = pygame.sprite.Group()
    coins2.add(C2)

    coins3 = pygame.sprite.Group()
    coins3.add(C3)

    player_group = pygame.sprite.Group()
    player_group.add(P1)
    #all objects together
    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)
    all_sprites.add(E1)
    all_sprites.add(C1)
    all_sprites.add(C2)
    all_sprites.add(C3)
    #increasing speed with time
    INC_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INC_SPEED, 1000)

    #main loop
    while True:
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                speed += 0.5
                speed_coin += 0.3

            if score_coin % 10 == 0 and score_coin > 0:
                enemy_speed += 0.5

    #main screen of the gaim
        DISPLAYSURF.blit(background, (0,0))
        scores = font_small.render("score: " + str(score), True, black)
        scores_coin = font_small.render("coins: " + str(score_coin), True, black)
        DISPLAYSURF.blit(scores, (10,10))
        DISPLAYSURF.blit(scores_coin, (width - 110, 10))
    #drawing the objects and moving
        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()
    #check the collision
        #the coin weights 1 score
        if pygame.sprite.spritecollideany(P1, coins):
            catch_sound.play()
            C1.rect.top = 0
            score_coin += 1
            C1.rect.center = (random.randint(40, width - 40), 0)
            DISPLAYSURF.blit(scores_coin, (200,370))
        #the coin weights -1 score
        if pygame.sprite.spritecollideany(P1, coins2):
            catch_sound.play()
            C2.rect.top = 0
            score_coin += -1
            C2.rect.center = (random.randint(40, width - 40), 0)
            DISPLAYSURF.blit(scores_coin, (200,370))
        #the coin weights 3 score
        if pygame.sprite.spritecollideany(P1, coins3):
            catch_sound.play()
            C3.rect.top = 0
            score_coin += 3  
            C3.rect.center = (random.randint(40, width - 40), 0)  
            DISPLAYSURF.blit(scores_coin, (200,370))
              
        

        if pygame.sprite.spritecollideany(P1, enemies):
            sound = pygame.mixer.Sound("racer/crash.wav").play()
            time.sleep(0.5)
    #game over screen
            DISPLAYSURF.fill(red)
            DISPLAYSURF.blit(game_over, (30, 250))
            DISPLAYSURF.blit(scores, (150, 330))    
            DISPLAYSURF.blit(scores_coin, (150,350))

    #end of the game
            pygame.display.update()
            import screen
            screen.main()

        pygame.display.update()
        Clock.tick(FPS)
main()