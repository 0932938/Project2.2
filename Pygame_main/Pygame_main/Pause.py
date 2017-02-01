import pygame, time, random, basic, Pygame_main

pygame.init

basic.screen
basic.clock
pause = False

def paused():
    global pause
    largeText = pygame.font.SysFont(None,300)
    TextSurf, TextRect = basic.text_objects("Paused", largeText)
    TextRect.center = ((basic.width/2),(basic.height/2 - 50))
    basic.screen.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        basic.button("Continue",  325,500,150,50,basic.dark_red,basic.red,unpause)
        basic.button("Go to menu",485,500,150,50,basic.dark_blue,basic.light_blue,Pygame_main.game_intro)
        basic.button("Instructions",645,500,150,50,basic.dark_green,basic.lime,Pygame_main.instructies)
        basic.button("Quit",      805,500,150,50,basic.d_yellow,basic.yellow2,Pygame_main.quitgame)

        pygame.display.update()
def unpause():
    global pause
    pause = False
    return
    
def pause_pressed():
    global pause
    pause = True
    paused()