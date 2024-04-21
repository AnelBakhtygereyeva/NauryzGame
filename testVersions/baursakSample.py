import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Falling Items Game")

# Colors
WHITE = (255, 255, 255)

# Player
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10

# Falling items
item_width = 30
item_height = 30
items = []
item_speed = 5

def create_item():
    x = random.randint(0, screen_width - item_width)
    y = 0
    items.append([x, y])

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += 5

    # Create falling items
    if random.random() < 0.02:
        create_item()

    # Move and draw falling items
    for item in items:
        item[1] += item_speed
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(item[0], item[1], item_width, item_height))

    # Draw player
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(player_x, player_y, player_width, player_height))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()