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
    fail = pygame.transform.scale(pygame.image.load("images/fail.png"), (1400, 800))
    good = pygame.transform.scale(pygame.image.load("images/good.png"), (1400, 800))
    kids = pygame.mixer.Sound("sounds/asykBg.mp3")
    kids.set_volume(0.6)
    kids.play()

    #paddle
    paddleW = 150
    paddleH = 25
    paddleSpeed = 20
    paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


    #ball as asyk
    ballRadius = 20
    ballSpeed = 6
    ball_rect = int(ballRadius * 20 ** 0.5)
    ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
    asykLying_image = pygame.transform.scale(pygame.image.load("images/asykLying.png"), (400,350))
    asyk_image = pygame.transform.scale(pygame.image.load("images/asyk2.png"), (150,150))
    dx, dy = 1, -1

    #sound
    collision_sound = pygame.mixer.Sound('sounds/asyk.wav')

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


    #block settings
    block_list = []

    rows = 1
    columns = 7

    #starting position
    start_x = (W - (columns * 215 + (columns - 1))) // 2
    start_y = - 60

    for i in range(columns):
        block = pygame.Rect(start_x + (190) * i, start_y, 180, 100)
        asykImage = pygame.transform.scale(pygame.image.load("images/asyk.png"), (400, 350))
        block_list.append((block,asykImage, 0)) 

    block_hits = [0] * len(block_list)

    last_time = pygame.time.get_ticks()


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        

        screen.blit(bg, (0,0))      

        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - last_time) / 1000  #converting milliseconds to seconds
        last_time = current_time

        #increasing speed of the ball with time
        ballSpeed += elapsed_time * 0.1

        #drawing the blocks
        for block, image, hits in block_list:
            screen.blit(image, block)

        #drawing the paddle
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
        #drawing the ball
        screen.blit(asyk_image, ball)


        #ball movement
        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy

        #collision left 
        if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
            dx = -dx
        #collision top
        if ball.centery < ballRadius + 50: 
            dy = -dy
        #collision with paddle
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)

        #collision with blocks
        for i, (block, image, hits) in enumerate(block_list):
            if ball.colliderect(block):
                if hits == 0:
                    block_list[i] = (block, asykLying_image, 1)  #changing image and mark after first hit
                elif hits == 1:
                    block_list.pop(i)  #removing after second hit
                    collision_sound.play()
                    break
                dx, dy = detect_collision(dx, dy, ball, block)
                collision_sound.play()

        if (ball.bottom > H) and (len(block_list) > 0):
            kids.stop()
            screen.blit(fail, (0,0))
            pygame.mixer.Sound("sounds/fail.mp3").play().set_volume(0.5)
            pygame.display.update()
            pygame.time.delay(1500)

            import levels
            levels.main2()


        elif not len(block_list):
            kids.stop()
            screen.blit(good, (0,0))
            pygame.mixer.Sound("sounds/success.wav").play()
            pygame.display.update()
            pygame.time.delay(1500)

            import levels
            levels.main3()
        
        #paddle Control
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed


        pygame.display.flip()
        clock.tick(FPS)
main()