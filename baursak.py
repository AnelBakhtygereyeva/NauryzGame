import pygame

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Red Ball!")

white = (255,255,255)
red = (255, 0, 0)

radius = 25
x = width // 2
y = height // 2

run = True
while run:
    screen.fill(white)
    pygame.draw.circle(screen, red, (x,y),radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y = max(y - 20, radius)
            elif event.key == pygame.K_DOWN:
                y = min(y + 20, height - radius)
            elif event.key == pygame.K_LEFT:
                x = max(x - 20, radius)
            elif event.key == pygame.K_RIGHT:
                x = min(x + 20, width - radius)
    pygame.display.update()
