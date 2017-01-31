import pygame, random, time, basic, Category
from array import array
    
pygame.init()
Dice_resize = (120,120)
Medal_resize = (200,50)
avatar_resize = (120,150)
bg = pygame.image.load("Blanco_FrameB.png")
basic.screen
basic.clock

#avatars
ava_one = pygame.image.load('avatar1_standing.png')
#ava_oneL = pygame.image.load('avatar1_left.png')
#ava_oneR = pygame.image.load('avatar1_right.png')
ava_two = pygame.image.load('avatar2_standing.png')
#ava_twoL = pygame.image.load('avatar2_left.png')
#ava_twoR = pygame.image.load('avatar2_right.png')
ava_three = pygame.image.load('avatar3_standing.png')
#ava_threeL = pygame.image.load('avatar3_left.png')
#ava_threeR = pygame.image.load('avatar3_right.png')
ava_four = pygame.image.load('avatar4_standing.png')
#ava_fourL = pygame.image.load('avatar4_left.png')
#ava_fourR = pygame.image.load('avatar4_right.png')

#avatars resize
ava_one = pygame.transform.scale(ava_one, avatar_resize)
#ava_oneL = pygame.transform.scale(ava_oneL, avatar_resize)
#ava_oneR = pygame.transform.scale(ava_oneR, avatar_resize)
ava_two = pygame.transform.scale(ava_two, avatar_resize)
#ava_twoL = pygame.transform.scale(ava_twoL, avatar_resize)
#ava_twoR = pygame.transform.scale(ava_twoR, avatar_resize)
ava_three = pygame.transform.scale(ava_three, avatar_resize)
#ava_threeL = pygame.transform.scale(ava_threeL, avatar_resize)
#ava_threeR = pygame.transform.scale(ava_threeR, avatar_resize)
ava_four = pygame.transform.scale(ava_four, avatar_resize)
#ava_fourL = pygame.transform.scale(ava_fourL, avatar_resize)
#ava_fourR = pygame.transform.scale(ava_fourR, avatar_resize)

#animation
#Ani_one = [ava_oneL, ava_oneR]
#Ani_two = [ava_twoL, ava_twoR]
#Ani_three = [ava_threeL, ava_threeR]
#Ani_four = [ava_fourL, ava_fourR]

#dices
dobbelImg1 = pygame.image.load('DObelsteen 1.png')
dobbelImg2 = pygame.image.load('DObelsteen 2.png')
dobbelImg3 = pygame.image.load('DObelsteen 3.png')
dobbelImg4 = pygame.image.load('DObelsteen 4.png')
dobbelImg5 = pygame.image.load('DObelsteen 5.png')
dobbelImg6 = pygame.image.load('DObelsteen 6.png')

#resize dice
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
def animation_one():
    playerone = random.choice(Ani_one)
    basic.screen.blit(playerone, (200,300))
    return playerone

def animation_two():
    playertwo = random.choice(Ani_two)
    basic.screen.blit(playertwo, (200,300))
    return playertwo

def animation_three():
    playerthree = random.choice(Ani_three)
    basic.screen.blit(playerthree, (200,300))
    return playerthree

def animation_four():
    playerfour = random.choice(Ani_four)
    basic.screen.blit(playerfour)
    return playerfour


def updatetime():
    pygame.display.update()
    pygame.time.delay(1000)

#dobbelsteen
def dobbelsteen(x,y):
    basic.screen.blit(dobbelNiks,(x,y))
def dobbel1(x,y):
    basic.screen.blit(dobbelImg1,(x,y))
    aantal_ogen = 1
def dobbel2(x,y):
    basic.screen.blit(dobbelImg2,(x,y))
    aantal_ogen = 2
def dobbel3(x,y):
    basic.screen.blit(dobbelImg3,(x,y))
    aantal_ogen = 3
def dobbel4(x,y):
    basic.screen.blit(dobbelImg4,(x,y))
    aantal_ogen = 4
def dobbel5(x,y):
    basic.screen.blit(dobbelImg5,(x,y))
    aantal_ogen = 5
def dobbel6(x,y):
    basic.screen.blit(dobbelImg6,(x,y))
    aantal_ogen = 6

#medal display
def Medals():
    basic.screen.blit(Medal_speler_1,(155, 620))
    basic.screen.blit(ava_one,(200, 300))
    basic.screen.blit(Medal_speler_2,(415, 620))
    basic.screen.blit(ava_two,(465, 300))
    basic.screen.blit(Medal_speler_3,(665, 620))
    basic.screen.blit(ava_three,(715, 300))
    basic.screen.blit(Medal_speler_4,(915, 620))
    basic.screen.blit(ava_four,(965, 300))

def MedalGold1():
    basic.screen.blit(MedalGold_speler_1,(155, 620))
def MedalGold2():
    basic.screen.blit(MedalGold_speler_2,(415, 620))
def MedalGold3():
    basic.screen.blit(MedalGold_speler_3,(665, 620))
def MedalGold4():
    basic.screen.blit(MedalGold_speler_4,(915, 620))

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
    basic.screen.blit(bg,(0,0)) 
    a = random.choice(playerturn)
    print (a)
    playerturn.remove(a)
    beginroll_uitkomst(a,200,50)

    b = random.choice(playerturn)
    print (b)
    playerturn.remove(b)
    beginroll_uitkomst(b,465,50)

    c = random.choice(playerturn)
    print (c)
    playerturn.remove(c)
    beginroll_uitkomst(c,715,50)

    d = random.choice(playerturn)
    print (d)
    playerturn.remove(d)
    beginroll_uitkomst(d,965,50)

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
        basic.button("Continue",  570,500,150,50, basic.dark_red,basic.red,Category.typeQroll)
        pygame.display.update()
        basic.clock.tick(15)  

def Start_game():
    basic.button("Roll for players", 500,400,280,50,basic.red,  basic.red2, beginroll)

def beginroll_unpause():
    global beginroll_pause
    beginroll_pause = False

#main game loop
def pregame_roll():
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame() 
            basic.screen.blit(bg,(0,0))       
            Start_game()

        pygame.display.update()
        basic.clock.tick(60)
