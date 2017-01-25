import pygame
import time
import random
from array import array
    
pygame.init()
 
###global variable

#colores
display_width = 1280
display_height = 720
 
black = (0,0,0)
white = (255,255,255)

dark_red    = (150,0,0)
red         = (200,0,0)
light_red   = (255,0,0)

dark_blue   = (0,0,200)
blue        = (0,50,255)
light_blue  = (0,100,255)

dark_green   = (0,150,0)
green        = (0,200,0)
light_green  = (0,255,0)

dark_yellow   = (150,150,0)
yellow        = (255,255,0)
light_yellow  = (255,255,100)

Dice_resize = (200,200)
Medal_resize = (200,50)

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

#images
#dices
dobbelNiks = pygame.image.load('DObelsteen niks.png')
dobbelImg1 = pygame.image.load('DObelsteen 1.png')
dobbelImg2 = pygame.image.load('DObelsteen 2.png')
dobbelImg3 = pygame.image.load('DObelsteen 3.png')
dobbelImg4 = pygame.image.load('DObelsteen 4.png')
dobbelImg5 = pygame.image.load('DObelsteen 5.png')
dobbelImg6 = pygame.image.load('DObelsteen 6.png')

#resize dice
dobbelNiks = pygame.transform.scale(dobbelNiks, Dice_resize)
dobbelImg1 = pygame.transform.scale(dobbelImg1, Dice_resize)
dobbelImg2 = pygame.transform.scale(dobbelImg2, Dice_resize)
dobbelImg3 = pygame.transform.scale(dobbelImg3, Dice_resize)
dobbelImg4 = pygame.transform.scale(dobbelImg4, Dice_resize)
dobbelImg5 = pygame.transform.scale(dobbelImg5, Dice_resize)
dobbelImg6 = pygame.transform.scale(dobbelImg6, Dice_resize)

#medals
Medal_speler_1 = pygame.image.load('Medal Speler 1.png')
Medal_speler_2 = pygame.image.load('Medal Speler 2.png')
Medal_speler_3 = pygame.image.load('Medal Speler 3.png')
Medal_speler_4 = pygame.image.load('Medal Speler 4.png')

MedalGold_speler_1 = pygame.image.load('Medal First Speler 1.png')
MedalGold_speler_2 = pygame.image.load('Medal First Speler 2.png')
MedalGold_speler_3 = pygame.image.load('Medal First Speler 3.png')
MedalGold_speler_4 = pygame.image.load('Medal First Speler 4.png')

#resize medals
Medal_speler_1 = pygame.transform.scale(Medal_speler_1, Medal_resize)
Medal_speler_2 = pygame.transform.scale(Medal_speler_2, Medal_resize)
Medal_speler_3 = pygame.transform.scale(Medal_speler_3, Medal_resize)
Medal_speler_4 = pygame.transform.scale(Medal_speler_4, Medal_resize)

MedalGold_speler_1 = pygame.transform.scale(MedalGold_speler_1, Medal_resize)
MedalGold_speler_2 = pygame.transform.scale(MedalGold_speler_2, Medal_resize)
MedalGold_speler_3 = pygame.transform.scale(MedalGold_speler_3, Medal_resize)
MedalGold_speler_4 = pygame.transform.scale(MedalGold_speler_4, Medal_resize)

#players
playerturn = ['1','2','3','4','5','6']

beginroll_pause = True

###definitions

def updatetime():
    pygame.display.update()
    pygame.time.delay(1000)

#dobbelsteen
def dobbelsteen(x,y):
    gameDisplay.blit(dobbelNiks,(x,y))
def dobbel1(x,y):
    gameDisplay.blit(dobbelImg1,(x,y))
    aantal_ogen = 1
def dobbel2(x,y):
    gameDisplay.blit(dobbelImg2,(x,y))
    aantal_ogen = 2
def dobbel3(x,y):
    gameDisplay.blit(dobbelImg3,(x,y))
    aantal_ogen = 3
def dobbel4(x,y):
    gameDisplay.blit(dobbelImg4,(x,y))
    aantal_ogen = 4
def dobbel5(x,y):
    gameDisplay.blit(dobbelImg5,(x,y))
    aantal_ogen = 5
def dobbel6(x,y):
    gameDisplay.blit(dobbelImg6,(x,y))
    aantal_ogen = 6

#medal display
def Medals():
    gameDisplay.blit(Medal_speler_1,(50, 260))
    gameDisplay.blit(Medal_speler_2,(270, 260))
    gameDisplay.blit(Medal_speler_3,(490, 260))
    gameDisplay.blit(Medal_speler_4,(710, 260))

def MedalGold1():
    gameDisplay.blit(MedalGold_speler_1,(50, 260))
def MedalGold2():
    gameDisplay.blit(MedalGold_speler_2,(270, 260))
def MedalGold3():
    gameDisplay.blit(MedalGold_speler_3,(490, 260))
def MedalGold4():
    gameDisplay.blit(MedalGold_speler_4,(710, 260))

#uitkomst van de dobbelstenen
def beginroll_uitkomst(z,x,y):
    if z == '1':
        dobbel1(x,y)
    elif z == '2':
        dobbel2(x,y)
    elif z == '3':
        dobbel3(x,y)
    elif z == '4':
        dobbel4(x,y)
    elif z == '5':
        dobbel5(x,y)
    else:
        dobbel6(x,y)

#begin
def beginroll():
    
    a = random.choice(playerturn)
    print (a)
    playerturn.remove(a)
    beginroll_uitkomst(a,50,50)

    b = random.choice(playerturn)
    print (b)
    playerturn.remove(b)
    beginroll_uitkomst(b,270,50)

    c = random.choice(playerturn)
    print (c)
    playerturn.remove(c)
    beginroll_uitkomst(c,490,50)

    d = random.choice(playerturn)
    print (d)
    playerturn.remove(d)
    beginroll_uitkomst(d,710,50)

    Medals()

    playerlist = [a,b,c,d]
    first_player = max(playerlist)
    if first_player == a:
        print("Speler 1 begint")
        MedalGold1()
    elif first_player == b:
        print("Speler 2 begint")
        MedalGold2()
    elif first_player == c:
        print("Speler 3 begint")
        MedalGold3()
    else:
        print("Speler 4 begint")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        MedalGold4()

    while beginroll_pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue",  325,300,150,50,dark_red,light_red,beginroll_unpause)

        pygame.display.update()
        clock.tick(15)  

#verplaatsing richting
def steen():
    time = 0
    while time < 3:
        dobbelsteen(50,50)
        updatetime()
        time+=1
    nummer = random.randint(1, 10)
    if nummer <= 5:
        while time < 7:
            dobbel1(50,50)
            updatetime()
            time+=1
    elif nummer <= 8:
        while time < 7:
            dobbel2(50,50)
            updatetime()
    elif nummer >= 9:
        while time < 7:
            dobbel3(50,50)
            updatetime()
            time+=1

def go_left():
    direction = "left"
    steen()
def go_up():
    direction = "up"
    steen()
def go_right():
    direction = "right" 
    steen()

def lopen():
    button("Left",  480,620,100,50,light_red,red,go_left)
    button("Up",    590,620,100,50,red,dark_red,go_up)
    button("Right", 700,620,100,50,light_red,red,go_right)

def Start_game():
    button("Roll for players", 500,400,280,50,light_red,  red, beginroll)

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

        button("Continue",  325,500,150,50,dark_red,light_red,unpause)
        button("Go to menu",485,500,150,50,dark_blue,light_blue,game_intro)
        button("Instructions",645,500,150,50,dark_green,light_green,instructies)
        button("Quit",      805,500,150,50,dark_yellow,light_yellow,quitgame)

        pygame.display.update()
        clock.tick(15)  

def unpause():
    global pause
    pause = False

def beginroll_unpause():
    global beginroll_pause
    beginroll_pause = False

#main game loop
def game_loop():
    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            gameDisplay.fill(white) 

            Start_game()
            lopen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    paused()


        pygame.display.update()
        clock.tick(60)


#buttons
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont(None, 30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def quitgame():
    pygame.quit()
    quit()

#main game 
game_loop()
pygame.quit()
quit()