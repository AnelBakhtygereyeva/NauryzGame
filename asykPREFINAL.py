import pygame 
import random
import math
import time

def main():
    pygame.init()

    W, H = 1400, 800
    FPS = 70

    screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    done = False
    bg = pygame.transform.scale(pygame.image.load("images/kover.png"), (1400, 800))
    transparent_layer = (255,255,255,128)

    #paddle
    paddleW = 150
    paddleH = 25
    paddleSpeed = 20
    paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


    #Ball
    ballRadius = 20
    ballSpeed = 6
    ball_rect = int(ballRadius * 20 ** 0.5)
    ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
    asyk_image = pygame.transform.scale(pygame.image.load("images/asyk2.png"), (150,150))
    dx, dy = 1, -1

    #Game score
    game_score = 0
    game_score_fonts = pygame.font.SysFont('comicsansms', 40)

    #sound
    collision_sound = pygame.mixer.Sound('ackanoid/catch.mp3')

    def detect_collision(dx, dy, ball, rect):
        if dx > 0:
            delta_x = ball.right - rect.left
        else:
            delta_x = rect.right - ball.left
        if dy > 0:
            delta_y = ball.bottom - rect.top
        else:
            delta_y = rect.bottom - ball.top

        if abs(delta_x - delta_y) < 10:
            dx, dy = -dx, -dy
        if delta_x > delta_y:
            dy = -dy
        elif delta_y > delta_x:
            dx = -dx
        return dx, dy


    #block settings initializing
    block_list = []

    rows = 1
    columns = 7

    # Calculate the starting x-coordinate to center the blocks
    start_x = (W - (columns * 215 + (columns - 1))) // 2
    start_y = - 60 # Adjust the starting y-coordinate to position at the top

    for i in range(columns):
        block = pygame.Rect(start_x + (190) * i, start_y, 180, 100)  # Placing blocks at the top
        image = pygame.transform.scale(pygame.image.load("images/asyk.png"), (400, 350))
        block_list.append(block)

    #Game over Screen
    losefont = pygame.font.SysFont('comicsansms', 40)
    losetext = losefont.render('Qaytadan basta :(', True, (255, 255, 255))
    losetextRect = losetext.get_rect()
    losetextRect.center = (W // 2, H // 2)

    #Win Screen
    winfont = pygame.font.SysFont('comicsansms', 40)
    wintext = losefont.render('Zharaysyn', True, (0, 0, 0))
    wintextRect = wintext.get_rect()
    wintextRect.center = (W // 2, H // 2)

    last_time = pygame.time.get_ticks()


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        

        screen.blit(bg, (0,0))      

        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - last_time) / 1000  # Convert milliseconds to seconds
        last_time = current_time

        # Increase ball speed over time
        ballSpeed += elapsed_time * 0.1


        # Update paddle rectangle

        

        #drawing the blocks
        for block in block_list:
            screen.blit(image, block)

        #drawing the paddle
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
        #drawing the ball
        screen.blit(asyk_image, ball)


        #Ball movement
        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy

        #Collision left 
        if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
            dx = -dx
        #Collision top
        if ball.centery < ballRadius + 50: 
            dy = -dy
        #Collision with paddle
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)

        #Collision blocks
        hitIndex = ball.collidelist(block_list)

        if hitIndex != -1:
            hitRect = block_list[hitIndex]
            block_list.pop(hitIndex)  # Remove the hit block from the list
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
            collision_sound.play()

        #Win/lose screens
        if (ball.bottom > H) and (len(block_list) > 0):
            screen.fill((0, 0, 0))
            screen.blit(losetext, losetextRect)
            time.sleep(0.5)
            import screen
        elif not len(block_list):
            screen.fill((255,255, 255))
            screen.blit(wintext, wintextRect)
            time.sleep(0.5)
            import lvl1
            lvl1.main3()
        
        #Paddle Control
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed


        pygame.display.flip()
        clock.tick(FPS)
main()