import pygame, time, random, basic, Pygame_main
from array import array

pygame.init

basic.screen
basic.clock
pause = False

def paused():
    largeText = pygame.font.SysFont(None,300)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2 - 50))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        basic.button("Continue",  325,500,150,50,basic.dark_red,basic.red,unpause)
        basic.button("Go to menu",485,500,150,50,basic.dark_blue,basic.light_blue,Pygame_main.game_intro)
        basic.button("Quit",      805,500,150,50,basic.dark_yellow,basic.yellow2,quitgame)

        pygame.display.update()
        clock.tick(15)  
def unpause():
    global pause
    pause = False
    
def pause_pressed():
    for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause = True
                paused()