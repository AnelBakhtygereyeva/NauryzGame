import pygame
from pygame.locals import *

def main():
    pygame.init()

    FPS = 60
    Clock = pygame.time.Clock()
    W = 1400
    H = 800
    boy_x = 100  # position of a boy
    girl_x = 100  # position of a girl
    image_toggle = False  #image toggle for boy
    girl_image_toggle = False  #image toggle for girl
    auto_move_counter = 0  #counter to automate the girl's moves


    #display
    screen = pygame.display.set_mode((W, H))
    background = pygame.transform.scale(pygame.image.load("images/tree/frame1.png"), (1400, 800))
    good = pygame.transform.scale(pygame.image.load("images/good.png"), (1400, 800))
    fail = pygame.transform.scale(pygame.image.load("images/fail.png"), (1400, 800))
    #boy images
    imBoyDefault = pygame.transform.scale(pygame.image.load("images/boy.png"), (400, 350))
    imBoyMoved = pygame.transform.scale(pygame.image.load("images/boyMove.png"), (400, 350))

    #girl images
    imGirlDefault = pygame.transform.scale(pygame.image.load("images/girl.png"), (400, 350))
    imGirlMoved = pygame.transform.scale(pygame.image.load("images/girlMove.png"), (400, 350))

    font = pygame.font.SysFont("comicsanms", 100)
    pygame.mixer.Sound("sounds/go.wav").play()
    pygame.mixer.Sound("sounds/horse.mp3").play()
    horserun = pygame.mixer.Sound("sounds/horserun.mp3")
    horserun.set_volume(0.4)

    for i in range(3, 0, -1):
        screen.blit(background, (0,0)) #background to make it "transparent"
        countdown_text = font.render(str(i), True, (255, 255, 255))  #rendering countdown text with for loop
        text_rect = countdown_text.get_rect(center=(W // 2, H // 2)) #positioning it
        screen.blit(countdown_text, text_rect) #drawing everything
        girlRect = imGirlDefault.get_rect()
        girlRect.center = (girl_x, 500)
        screen.blit(imGirlDefault, girlRect)
        boyRect = imBoyDefault.get_rect()
        boyRect.center = (boy_x, 650)
        screen.blit(imBoyDefault, boyRect)
        
        pygame.display.flip()
        pygame.time.delay(1000)
            
    #start text
    start_text = font.render("Start", True, (0, 255, 0))
    text_rect = start_text.get_rect(center=(W // 2, H // 2))
    screen.blit(start_text, text_rect)
    girlRect = imGirlDefault.get_rect()
    girlRect.center = (girl_x, 500)  # Position the girl a bit above the boy
    screen.blit(imGirlDefault, girlRect)
    boyRect = imBoyDefault.get_rect()
    boyRect.center = (boy_x, 650)
    screen.blit(imBoyDefault, boyRect)
    pygame.display.flip()
    pygame.time.delay(1000)

    horserun.play()
                    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_RIGHT:
                    if boy_x + 23 < 1200: #border
                        boy_x += 23
                        image_toggle = not image_toggle
                    else:
                        pygame.mixer.Sound("sounds/horse.mp3").play()
                        horserun.stop()
                        screen.blit(good, (0,0))
                        pygame.mixer.Sound("sounds/success.wav").play()
                        pygame.display.update()
                        pygame.time.delay(2000)  #wait for 2 second

                        import levels
                        levels.main2()


        #automate girl moves and image toggle
        auto_move_counter += 1
        if auto_move_counter % 8 == 0:  #change girl's position and image every 60 frames "(~1 second at 60 FPS)""
            if girl_x + 18 <= 1150: #border
                girl_x += 18 
                girl_image_toggle = not girl_image_toggle
            else:
                horserun.stop()
                screen.blit(fail, (0,0))
                pygame.mixer.Sound("sounds/fail.mp3").play()
                pygame.display.update()
                pygame.time.delay(2000)

                import levels
                levels.main()



        screen.blit(background, (0,0))

        #for image switching
        if image_toggle:
            imBoy = imBoyMoved
        else:
            imBoy = imBoyDefault

        
        if girl_image_toggle:
            imGirl = imGirlMoved
        else:
            imGirl = imGirlDefault

        girlRect = imGirl.get_rect()
        girlRect.center = (girl_x, 500)
        screen.blit(imGirl, girlRect)

        boyRect = imBoy.get_rect()
        boyRect.center = (boy_x, 650)
        screen.blit(imBoy, boyRect)



        pygame.display.update()
        Clock.tick(FPS)