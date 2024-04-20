import pygame
import time

pygame.init()

width = 1400
height = 800
screen = pygame.display.set_mode((width, height))
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (0, 128, 128)
new = (125, 125, 125)
gray = (128, 128, 128)

pygame.display.set_caption("Red Cube!")

white = (255, 255, 255)
Fps = 60
Clock = pygame.time.Clock()

class Cube(pygame.sprite.Sprite):
    def __init__(self, color, side_length, x, y, group):
        super().__init__()
        self.image = pygame.Surface((side_length, side_length))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.group = group

    def check_border_collision(self, other_cube):
        if self.rect.colliderect(other_cube.rect):
            if self.rect.left < other_cube.rect.left:
                self.rect.right = other_cube.rect.left
            if self.rect.right > other_cube.rect.right:
                self.rect.left = other_cube.rect.right
            if self.rect.top < other_cube.rect.top:
                self.rect.bottom = other_cube.rect.top
            if self.rect.bottom > other_cube.rect.bottom:
                self.rect.top = other_cube.rect.bottom

red_cube = Cube(red, 80, 300, 300, "red")
green_cube = Cube(green, 100, 200, 200, "good")
blue_cube = Cube(blue, 100, 100, 100, "bad")
dastarkhan = Cube(yellow, 450, width // 2 - 225, height // 2 - 200, "dastarkhan")
dastarkhanReal = Cube(gray, 452, width // 2 - 226, height // 2 - 201, "dastarkhan")
new = Cube(new, 100, 1200, 300, "good")

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
    dastarkhan_sprites.add(dastarkhanReal)
if red_cube.group == "red":
    red_sprites.add(red_cube)

run = True
while run:
    screen.fill(white)
    screen.blit(dastarkhanReal.image, dastarkhanReal.rect)
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

    red_cube.check_border_collision(dastarkhan)

    # Collision detection
    if pygame.sprite.spritecollide(red_cube, good_sprites, False):
        for sprite in good_sprites:
            if pygame.sprite.collide_rect(red_cube, sprite):
                if sprite == green_cube:
                    # Collision with green_cube
                    pygame.mixer.Sound("ackanoid/catch.mp3").play()
                    green_cube.rect.center = (width // 2, height // 2)
                elif sprite == new:
                    # Collision with new
                    pygame.mixer.Sound("ackanoid/catch.mp3").play()
                    new.rect.center = (width // 2 - 50, height // 2 - 30)

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
pygame.quit()