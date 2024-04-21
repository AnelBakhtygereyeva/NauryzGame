import pygame

def main():
    pygame.init()

    width = 1400
    height = 800
    screen = pygame.display.set_mode((width, height))
    fps = 60
    clock = pygame.time.Clock()


    frames = [pygame.image.load(f"images/frame{i}.png") for i in range(1, 3)]
    background = pygame.transform.scale(pygame.image.load("images/blurbg.png"), (1400, 900))
    pygame.mixer.Sound("sounds/end.mp3").play()



    #to control frame switching
    currentFrameIndex = 0
    lastSwitchTime = pygame.time.get_ticks()  #time after last switch
    switchInterval = 500  #switch every 0.5 seconds

    #main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        #current time
        now = pygame.time.get_ticks()

        #switch frames every 0.5 seconds
        if now - lastSwitchTime >= switchInterval:
            currentFrameIndex = (currentFrameIndex + 1) % len(frames)
            lastSwitchTime = now


        screen.blit(background, (0,0)) #background

        currentFrame = frames[currentFrameIndex]
        screen.blit(currentFrame, (0, 0)) #draw the frame
        pygame.display.flip()

        clock.tick(fps)