import pygame
import random

def main():
    pygame.init()

    W, H = 1400, 800
    FPS = 70

    screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    done = False
    bg = (0, 0, 0)

    # Paddle
    paddleW = 150
    paddleH = 25
    paddleSpeed = 20
    paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

    # Asyk (Ball)
    ballRadius = 20
    ballSpeed = 6
    asyk_image = pygame.image.load("asyk.png")  # Update the path to your asyk image
    asyk_image = pygame.transform.scale(asyk_image, (ballRadius * 2, ballRadius * 2))
    ball = pygame.Rect(paddle.centerx - ballRadius, paddle.top - ballRadius * 2, ballRadius * 2, ballRadius * 2)
    shooting = False

    # Game score
    game_score = 0
    game_score_fonts = pygame.font.SysFont('comicsansms', 40)

    # Sound
    collision_sound = pygame.mixer.Sound('catch.mp3')

    # Blocks
    block_list = []
    rows = 1
    columns = 7
    start_x = (W - (columns * 220 + (columns - 1))) // 2
    start_y = 20

    for i in range(columns):
        block = pygame.Rect(start_x + 220 * i, start_y, 200, 50)
        block_list.append(block)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(bg)

        # Paddle Control
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed

        # Shooting Mechanism
        if key[pygame.K_SPACE] and not shooting:
            shooting = True
            dy = -ballSpeed

        if shooting:
            ball.y += dy
            if ball.top <= 0 or ball.colliderect(paddle):
                shooting = False
                ball.x = paddle.centerx - ballRadius
                ball.y = paddle.top - ballRadius * 2

        # Collision with Blocks
        hitIndex = ball.collidelist(block_list)
        if hitIndex != -1:
            block_list.pop(hitIndex)
            shooting = False
            ball.x = paddle.centerx - ballRadius
            ball.y = paddle.top - ballRadius * 2
            game_score += 1
            collision_sound.play()

        # Drawing
        for block in block_list:
            pygame.draw.rect(screen, (123, 123, 123), block)
        pygame.draw.rect(screen, (255, 255, 255), paddle)
        if not shooting:  # Update asyk position with paddle if not shooting
            ball.x = paddle.centerx - ballRadius
        screen.blit(asyk_image, ball)

        # Game Score Display
        game_score_text = game_score_fonts.render(f'Score: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, (50, 20))

        pygame.display.flip()
        clock.tick(FPS)


main()