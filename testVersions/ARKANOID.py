import pygame 
import random
import math
pygame.init()

#basic
W, H = 1200, 800
FPS = 60

#some settings
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (100, 100, 100)
main_menu_bg = (0,0,0)
overlay_surface = pygame.Surface((W, H), pygame.SRCALPHA)
overlay_surface.fill((50, 50, 50, 0)) 
DARK_GRAY = (50, 50, 50)


#paddle base
paddleW = 120
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


#Ball base
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#sound
collision_sound = pygame.mixer.Sound('ackanoid/catch.mp3')

#detecting the collision
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


block_list = []
color_list = []

rows = 1
columns = 7

# Calculate the starting x-coordinate to center the blocks
start_x = (W - (columns * 100 + (columns - 1) * 20)) // 2

for j in range(rows):
    for i in range(columns):
        block = pygame.Rect(start_x + (100 + 20) * i, 50 + 70 * j, 100, 50)
        color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        block_list.append(block)
        color_list.append(color)



#game over screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#win screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

initial_paddle_width = paddleW
shrink_rate = 3

last_time = pygame.time.get_ticks()

#game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = True
            elif event.key == pygame.K_m:
                paused = True
#game screen
        screen.fill(bg)

        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - last_time) / 1000  # Convert milliseconds to seconds
        last_time = current_time


        ballSpeed += elapsed_time * 0.1
    

    #drawing the blocks
        for color, block in enumerate (block_list):
            pygame.draw.rect(screen, color_list[color], block)
            #draw star in the center of yellow blocks
            if color_list[color] == (255, 255, 0):
                draw_star(screen, (0, 0, 0), block.center)

    #drawing the paddle
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    #drawing the ball
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)


    #ball movement
        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy

    #collision left and right borders 
        if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
            dx = -dx
    #collision the top border
        if ball.centery < ballRadius + 50: 
            dy = -dy
    #collision with paddle
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)

    #collision with blocks
        hitIndex = ball.collidelist(block_list)

        if hitIndex != -1:
            hitRect = block_list[hitIndex]
            hitColor = color_list[hitIndex]
            if hitColor != DARK_GRAY:
                block_list.pop(hitIndex)
                color_list.pop(hitIndex)
                dx, dy = detect_collision(dx, dy, ball, hitRect)
                game_score += 1
                collision_sound.play()
            #check if the hit block is gold (yellow)
                if hitColor == (255, 255, 0):
                #increase paddle width
                    paddleW += 40
                    paddle.width = int(paddleW)
            else:
                dx, dy = detect_collision(dx, dy, ball, hitRect)
        
    #game score text
        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)

        game_score_text_win = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))

#main and pause menu screens
    else:
        key = pygame.key.get_pressed()
        #pause menu
        if key[pygame.K_p]:
            screen.blit(overlay_surface, (0,0))
            font = pygame.font.SysFont('comicsansms', 40)
            pause_text = font.render("Pause Menu", True, (0, 255, 255))
            PauseRect = pause_text.get_rect()
            PauseRect.center = (W // 2, H // 2 - 100)
            screen.blit(pause_text, PauseRect)

            continue_text = font.render("Continue (Press C)", True, (255, 255, 255))
            continueRect = continue_text.get_rect()
            continueRect.center = (W // 2, H // 2 - 20)
            screen.blit(continue_text, continueRect)

            new_game_text = font.render("New Game (Press N)", True, (255, 255, 255))
            newGameRect = new_game_text.get_rect()
            newGameRect.center = (W // 2, H // 2 + 30)
            screen.blit(new_game_text, newGameRect)

            help_text = font.render("Help (Press H)", True, (255, 255, 255))
            helpTextRect = help_text.get_rect()
            helpTextRect.center = (W // 2, H // 2 + 80)
            screen.blit(help_text, helpTextRect)

            exit_text = font.render("Exit (Press ESC)", True, (255, 255, 255))
            exitRect = exit_text.get_rect()
            exitRect.center = (W // 2, H // 2 + 130)
            screen.blit(exit_text, exitRect)

        #main menu
        elif key[pygame.K_m]:
            screen.fill(main_menu_bg)
            font = pygame.font.SysFont('comicsansms', 40)
            pause_text = font.render("Main menu", True, (0, 255, 255))
            PauseRect = pause_text.get_rect()
            PauseRect.center = (W // 2, H // 2 - 100)
            screen.blit(pause_text, PauseRect)

            continue_text = font.render("Continue (Press C)", True, (255, 255, 255))
            continueRect = continue_text.get_rect()
            continueRect.center = (W // 2, H // 2 - 20)
            screen.blit(continue_text, continueRect)

            new_game_text = font.render("New Game (Press N)", True, (255, 255, 255))
            newGameRect = new_game_text.get_rect()
            newGameRect.center = (W // 2, H // 2 + 30)
            screen.blit(new_game_text, newGameRect)

            exit_text = font.render("Exit (Press ESC)", True, (255, 255, 255))
            exitRect = exit_text.get_rect()
            exitRect.center = (W // 2, H // 2 + 80)
            screen.blit(exit_text, exitRect)


 
    #Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
        screen.blit(game_score_text, game_score_rect)
    elif not len(block_list) - 8:
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)
        screen.blit(game_score_text_win, game_score_rect)
    
    #paddle control and setting keys
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed
    if key[pygame.K_n]:
        paused = False
        reset_game()
    if key[pygame.K_c]:
        paused = False
    if key[pygame.K_ESCAPE]:
        done = True
    if key[pygame.K_h]:
        paddleW = 200
        ballSpeed = 3
        paused = False
    
    #screen update
    pygame.display.flip()
    clock.tick(FPS)