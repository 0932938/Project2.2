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

red = (150,0,0)
light_red = (200,0,0)
bright_red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

#images
dobbelNiks = pygame.image.load('DObelsteen niks.png')
dobbelImg1 = pygame.image.load('DObelsteen 1.png')
dobbelImg2 = pygame.image.load('DObelsteen 2.png')
dobbelImg3 = pygame.image.load('DObelsteen 3.png')
dobbelImg4 = pygame.image.load('DObelsteen 4.png')
dobbelImg5 = pygame.image.load('DObelsteen 5.png')
dobbelImg6 = pygame.image.load('DObelsteen 6.png')

#players
playerturn = ['1','2','3','4','5','6']

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

#begin
def beginroll():
    a = random.choice(playerturn)
    print (a)
    playerturn.remove(a)

    b = random.choice(playerturn)
    print (b)
    playerturn.remove(b)

    c = random.choice(playerturn)
    print (c)
    playerturn.remove(c)

    d = random.choice(playerturn)
    print (d)
    playerturn.remove(d)

    playerlist = [a,b,c,d]
    first_player = max(playerlist)
    if first_player == a:
        print("Speler 1 begint")
    elif first_player == b:
        print("Speler 2 begint")
    elif first_player == c:
        print("Speler 3 begint")
    else:
        print("Speler 4 begint")
    quitgame()

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
    beginroll()
def go_right():
    direction = "right" 
    steen()

def lopen():
    button("Left",  480,620,100,50,bright_red,  light_red, go_left)
    button("Up",    590,620,100,50,light_red,   red,       go_up)
    button("Right", 700,620,100,50,bright_red,  light_red, go_right)


#main game loop
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
 
    x_change = 0
 
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        x += x_change
        gameDisplay.fill(white) 

        lopen()
 
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

    smallText = pygame.font.SysFont(None, 40)
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