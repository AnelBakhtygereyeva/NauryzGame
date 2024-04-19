import pygame
from pygame.locals import*


def main():
    pygame.init()

    FPS = 60
    Clock = pygame.time.Clock()

    W = 1400
    H = 800
    boy_speed = 2
    girl_speed = 4
    score = 0

    catch_sound = pygame.mixer.Sound("racer/catch.mp3")

    DISPLAYSURF = pygame.display.set_mode((W, H))
    background = pygame.transform.scale(pygame.image.load("images/tree/frame1.png"), (1400, 800))
    
    class Boy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            imageBoy = pygame.image.load("images/boy.png")
            self.image = pygame.transform.scale(imageBoy, (500, 400))
            self.rect = self.image.get_rect()
            self.rect.center = (100, 500)

        def move(self):
            pressed_keys = pygame.key.get_pressed()
            if self.rect.left > 0:
                if pressed_keys[K_LEFT]:
                    self.rect.move_ip(-5, 0)
            if self.rect.right < W + 200:
                if pressed_keys[K_RIGHT]:
                    self.rect.move_ip(5, 0)

    class Girl(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            imageGirl = pygame.image.load("images/girl.png")  # Load the image using pygame
            self.image = pygame.transform.scale(imageGirl, (500, 400))
            self.rect = self.image.get_rect()
            self.rect.center = (200, 600)

        def move(self):
            #imageGirlMove = pygame.image.load("images/girlMove.png")
            self.rect.move_ip(girl_speed, 0)
            #self.image = pygame.transform.scale(imageGirlMove, (200, 100))


    B = Boy()
    G = Girl()

    boy_group = pygame.sprite.Group()
    boy_group.add(B)

    girl_group = pygame.sprite.Group()
    girl_group.add(G)


    all_sprites = pygame.sprite.Group()
    all_sprites.add(B)
    all_sprites.add(G)

    INC_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INC_SPEED, 1000)

    while True:
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                girl_speed += 0.5
            if event.type == pygame.QUIT:
                pygame.quit()

        for sprite in all_sprites:
            sprite.move()
 #       DISPLAYSURF.blit(background, (0,0))

        DISPLAYSURF.blit(background, (0,0))
        all_sprites.update()
        all_sprites.draw(DISPLAYSURF)
            #pygame.display.update()
            #import screen
            #screen.main()

        pygame.display.update()
        Clock.tick(FPS)
main()