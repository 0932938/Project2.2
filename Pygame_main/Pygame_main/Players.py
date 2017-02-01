import pygame, random, basic, sys, Pause, Pregame, pygame.mixer,database, time, Pygame_main, Category

Black = basic.black
White = basic.white
Blue = basic.blue
Red = basic.red
Green = basic.green
Yellow = basic.yellow

Gold = basic.gold

Dice_resize = (200,200)

changeL = -28.5
changeR = 29
changeU = -42.5

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

pijltoetsen = pygame.image.load("pijltoetsen.png")

def dobbelsteen(x,y):
    screen.blit(dobbelNiks,(x,y))
def dobbel1(x,y):
    screen.blit(dobbelImg1,(x,y))
def dobbel2(x,y):
    screen.blit(dobbelImg2,(x,y))
def dobbel3(x,y):
    screen.blit(dobbelImg3,(x,y))
def dobbel4(x,y):
    screen.blit(dobbelImg4,(x,y))
def dobbel5(x,y):
    screen.blit(dobbelImg5,(x,y))
def dobbel6(x,y):
    screen.blit(dobbelImg6,(x,y))

pygame.init()
pygame.display.set_caption("EUROMAST")
basic.screen
bg = pygame.image.load("eurimast.jpg")

player_one = pygame.image.load("avatar1_standing.png")
player_one = pygame.transform.scale(player_one, (25,34))
player_two = pygame.image.load("avatar2_standing.png")
player_two = pygame.transform.scale(player_two, (25,34))
player_three = pygame.image.load("avatar3_standing.png")
player_three = pygame.transform.scale(player_three, (25,34))
player_four = pygame.image.load("avatar4_standing.png")
player_four = pygame.transform.scale(player_four, (25,34))


player1_turn_count = 0
player2_turn_count = 0
player3_turn_count = 0
player4_turn_count = 0

avatar_resize = (42,50)

#een classe voor spelers aanmaken
class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0

    def __init__(self, x, y, image, point):
        pygame.sprite.Sprite.__init__(self) #super(type(self), self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.point = point

    def loop(self, x, y):
        self.rect.x += x
        self.rect.y += y


    def update(self):
        #move up and down
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        
        if not (0 < self.rect.y < 700):
            player1.rect.x = 243
            player1.rect.y = 660
        # if not (0 < player2.rect.y < 450):
            player2.rect.x = 273
            player2.rect.y = 660

            player3.rect.x = 183
            player3.rect.y = 660

            player4.rect.x = 213
            player4.rect.y = 660

        if self.rect.y <= 2:
            self.rect.y = 2

#spelers botsen tegen elkaar
def collide(player_turn):
#p1 & p2
    if player1.rect.colliderect(player2):
        if player_turn == 1:
            player2.rect.y += 42.5
        elif player_turn == 2:
            player1.rect.y += 42.5
#p1 & p3
    elif player1.rect.colliderect(player3):
        if player_turn == 1:
            player3.rect.y += 42.5
        elif player_turn == 3:
            player1.rect.y += 42.5
#p1 &p4           
    elif player1.rect.colliderect(player4):
        if player_turn == 1:
            player4.rect.y += 42.5
        elif player_turn == 4:
            player1.rect.y += 42.5
          
#p2 &p3           
    elif player2.rect.colliderect(player3):
        if player_turn == 2:
            player3.rect.y += 42.5
        elif player_turn == 3:
            player2.rect.y += 42.5

#p2 &p4
    elif player2.rect.colliderect(player4):
        if player_turn == 2:
            player4.rect.y += 42.5
        elif player_turn == 4:
            player2.rect.y += 42.5

#p3 &p4
    elif player3.rect.colliderect(player4):
        if player_turn == 3:
            player4.rect.y += 42.5
        elif player_turn == 4:
            player3.rect.y += 42.5

#verticale lijnen (walls) waarop de poppetjes bewegen           
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.image.fill(Blue)

#kijkt of spelers/poppetjes buiten hun assen gaan
def wall_detection(player_turn):
    if player_turn == 1:
        if player1.rect.x < 183:
            player1.rect.x = 270
        if player1.rect.x > 273:
            player1.rect.x = 183
        if player1.rect.y <= 17:
            player1.rect.y = 15
            winning(1)
    if player_turn == 2:
        if player2.rect.x < 183:
            player2.rect.x = 270
        if player2.rect.x > 273:
            player2.rect.x = 183
        if player2.rect.y <= 17:
            player2.rect.y = 15
            winning(2)
    if player_turn == 3:
        if player3.rect.x < 183:
            player3.rect.x = 270
        if player3.rect.x > 273:
            player3.rect.x = 180
        if player3.rect.y <=  17:
            player3.rect.y = 15
            winning(3)
    if player_turn == 4:
        if player4.rect.x < 183:
            player4.rect.x = 270
        if player4.rect.x > 273:
            player4.rect.x = 183
        if player4.rect.y <=  17:
            player4.rect.y = 15
            winning(4)
    collide(player_turn)

#winnende functie
def winning(player):
    winning_player = player
    victoryscreen = pygame.image.load("victory.jpg")
    playerturn = 0
    if player == 1:
        playerturn = player1.point
        print(player1_turn_count)
    elif player == 2:
        playerturn = player2.point
        print(player3_turn_count)
    elif player == 3:
        playerturn = player3.point
        print(player2_turn_count)
    elif player == 4:
        playerturn = player4.point
        print(player4_turn_count)
    Wsound = pygame.mixer.Sound("winner.wav")
    Wsound.play()
    higherscore = database.highscores("speler" + str(player), playerturn, None, None, None)
    database.highscores.highscores_updaten(higherscore)
    sprites2.draw(basic.screen)
    basic.screen.blit(victoryscreen, (100, 70))

    pygame.display.flip()
    pygame.time.delay(4000)
    Pygame_main.highscores()

#dobbelsteen
def steen(moves):
    time = 1
    while time < 2:
        dobbelsteen(700,400)
        updatetime()
        time+=1
    if moves == 1:
        while time < 4:
            dobbel1(700,400)
            updatetime()

            time+=1
    elif moves == 2: 
        while time < 4:
            dobbel2(700,400)
            updatetime()
            time+=1
    elif moves == 3:
        while time < 4:
            dobbel3(700,400)
            updatetime()
            time+=1

def updatetime():
    pygame.display.update()
    pygame.time.delay(750)
# spelers rechts boven op het speelbord
def Medals():
    ava_one = pygame.transform.scale(Pregame.ava_one, avatar_resize)
    ava_two = pygame.transform.scale(Pregame.ava_two, avatar_resize)
    ava_three = pygame.transform.scale(Pregame.ava_three, avatar_resize)
    ava_four = pygame.transform.scale(Pregame.ava_four, avatar_resize)
    basic.screen.blit(Pregame.Medal_speler_1,   (610, 110))
    basic.screen.blit(Pregame.Medal_speler_2,   (810, 110))
    basic.screen.blit(Pregame.Medal_speler_3,   (810, 160))
    basic.screen.blit(Pregame.Medal_speler_4,   (610, 160))
    basic.screen.blit(ava_one,                  (560, 110))
    basic.screen.blit(ava_two,                  (1018, 110))
    basic.screen.blit(ava_three,                (1018, 160))
    basic.screen.blit(ava_four,                 (560, 160))
#rechts boven wie er aan de beurt is
def MedalGold1():
    basic.screen.blit(Pregame.MedalGold_speler_1,(610, 110))
def MedalGold2():
    basic.screen.blit(Pregame.MedalGold_speler_2,(810, 110))
def MedalGold3():
    basic.screen.blit(Pregame.MedalGold_speler_3,(810, 160))
def MedalGold4():
    basic.screen.blit(Pregame.MedalGold_speler_4,(610, 160))

pygame.init()

screen = pygame.display.set_mode([basic.width, basic.height])
pygame.display.set_caption("EUROMAST")
sprites = pygame.sprite.Group()
sprites2 = pygame.sprite.Group()

#aanmaken en groeperen van walls
wall_list = pygame.sprite.Group()

wall_1 = Wall(190, 4, 10, 690)
wall_list.add(wall_1)
wall_1.image.fill(Blue)
sprites.add(wall_1)

wall_2 = Wall(220,4, 10, 690)
wall_list.add(wall_2)
wall_1.image.fill(Red)
sprites.add(wall_2)

wall_3 = Wall(250, 4, 10, 690)
wall_list.add(wall_3)
wall_3.image.fill(Yellow)
sprites.add(wall_3)

wall_4 = Wall(280, 4, 10, 690)
wall_list.add(wall_4)
wall_4.image.fill(Green)
sprites.add(wall_4)


#horizontale lijnen voor levels  
pygame.draw.line(bg, Blue, (0, 560), (400, 560),2)
pygame.draw.line(bg, Blue, (0, 525), (400, 525),2)
pygame.draw.line(bg, Blue, (0, 490), (400, 490),2)

pygame.draw.line(bg, Blue, (0, 455), (400, 455),2)
pygame.draw.line(bg, Blue, (0, 420), (400, 420),2)
pygame.draw.line(bg, Blue, (0, 385), (400, 385),2)

pygame.draw.line(bg, Blue, (0, 350), (400, 350),2)
pygame.draw.line(bg, Blue, (0, 315), (400, 315),2)
pygame.draw.line(bg, Blue, (0, 280), (400, 280),2)

pygame.draw.line(bg, Blue, (0, 245), (400, 245),2)
pygame.draw.line(bg, Blue, (0, 210), (400, 210),2)
pygame.draw.line(bg, Blue, (0, 175), (400, 175),2)

pygame.draw.line(bg, Blue, (0, 140), (400, 140),2)
pygame.draw.line(bg, Blue, (0, 105), (400, 105),2)
pygame.draw.line(bg, Blue, (0, 70), (400, 70),2)

pygame.draw.line(bg, Gold, (0, 35), (400, 35),3)
pygame.draw.line(bg, Gold, (0, 0), (400, 0),3)


#speler groeperen
player1_list = pygame.sprite.Group()
player2_list = pygame.sprite.Group()

#aanmaken van 4 spelers
player1 = Player(150, 660, player_one, 0) #gele pop

player1_list.add(player1)
sprites2.add(player1)

player2 = Player(185, 660, player_two, 0) #groene pop
sprites2.add(player2)

player3 = Player(210, 660, player_three, 0) #rode pop
sprites2.add(player3)

player4 = Player(240, 660, player_four, 0) #blauwe pop
sprites2.add(player4)

font = pygame.font.SysFont('Arial', 18, False, False)

clock = pygame.time.Clock()

#player_moves wordt de dobbelsteen worp uitkomst
def dice_roll():
    move_check = random.randint(1, 10)
    if move_check <= 6:
        moves = 1
    elif move_check <= 9:
        moves = 2
    elif move_check <= 10:
        moves = 3
    steen(moves)
    return moves

done = False
gameover = False
#defineerd wie het eerst aan de beurt is
def player_game(first_player_re):
    player_turn = first_player_re
    
    player_main_game(player_turn)
#gaat naar een categorie
def ga_category():
    blit_bg()
    sprites2.update()
    sprites2.draw(basic.screen)
    blit_allbutbg()
    pygame.display.flip()
    pygame.time.delay(1500)
    Category.typeQroll()

#het hele spel
def player_main_game(player_turn):
    global bg
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and gameover == False:
                if event.key == pygame.K_p:
                    Pause.pause_pressed()
                else:
                    player_moves = dice_roll()
#Left key
                    if event.key == pygame.K_LEFT:
#player1
                        if player_turn == 1:
                            player1.point += 1
                            while player_moves > 0:
                                player1.loop(changeL,0)
                                player_moves -= 1
                                wall_detection(player_turn)
                            player_turn = 2
                            ga_category()
#player2
                        elif player_turn == 2:
                            player2.point += 1
                            while player_moves > 0:
                                player2.loop(changeL,0)
                                player_moves -= 1
                                wall_detection(player_turn)
                            player_turn = 3
                            ga_category()
#player3
                        elif player_turn == 3:
                            player3.point += 1
                            while player_moves > 0:
                                player3.loop(changeL,0)
                                player_moves -= 1
                                wall_detection(player_turn)
                            player_turn = 4
                            ga_category()
#player4
                        elif player_turn == 4:
                            player4.point += 1
                            while player_moves > 0:
                                player4.loop(changeL,0)
                                player_moves -= 1
                                wall_detection(player_turn)
                            player_turn = 1
                            ga_category()
#Right key
                    elif event.key == pygame.K_RIGHT:
#player1
                        if player_turn == 1:
                            player1.point += 1
                            while player_moves > 0:
                                player1.loop(changeR,0)
                                player_moves -= 1
                                wall_detection(player_turn)
                            player_turn = 2
                            ga_category()
#player2
                        elif player_turn == 2:
                            player2.point += 1
                            while player_moves > 0:
                                player2.loop(changeR,0)
                                player_moves -= 1
                                wall_detection(player_turn)
                            player_turn = 3
                            ga_category()
#player3
                        elif player_turn == 3:
                            player3.point += 1
                            while player_moves > 0:
                                player3.loop(changeR,0)
                                player_moves -= 1
                                wall_detection(player_turn)
                            player_turn = 4
                            ga_category()
#player4
                        elif player_turn == 4:
                            player4.point += 1
                            while player_moves > 0:
                                player4.loop(changeR,0)
                                player_moves -= 1
                                wall_detection(player_turn)
                            player_turn = 1
                            ga_category()
#Up key
                    elif event.key == pygame.K_UP:
#player1
                        if player_turn == 1:
                            player1.point += 1
                            while player_moves > 0:
                                player1.loop(0,changeU)
                                player_moves -= 1
                                wall_detection(player_turn)
                            player_turn = 2
                            ga_category()
#player2
                        elif player_turn == 2:
                            player2.point += 1
                            while player_moves > 0:
                                player2.loop(0,changeU)
                                player_moves -= 1
                                wall_detection(player_turn)
                            player_turn = 3
                            ga_category()
#player3
                        elif player_turn == 3:
                            player3.point += 1
                            while player_moves > 0:
                                player3.loop(0,changeU)
                                player_moves -= 1
                                wall_detection(player_turn)
                            player_turn = 4
                            ga_category()
#player4
                        elif player_turn == 4:
                            player4.point += 1
                            while player_moves > 0:
                                player4.loop(0,changeU)
                                player_moves -= 1
                                wall_detection(player_turn)
                            player_turn = 1
                            ga_category()


        sprites.update()
        sprites2.update()
        


        blit_bg()
        sprites.update()


        Medals()
        if player_turn == 1:
            MedalGold1()
        if player_turn == 2:
            MedalGold2()
        if player_turn == 3:
            MedalGold3()
        if player_turn == 4:
            MedalGold4()
        blit_allbutbg()
        pygame.display.flip()
        clock.tick(60)
#tekent de level text
def blit_allbutbg():
    level_1 = font.render("level 1", True, (Black))
    level_5 = font.render("level 5", True, (Black))
    level_10 = font.render("level 10", True, (Black))
    level_15= font.render("level 15", True, (Black))
    finish = font.render("Finish", True, (Yellow))
    sprites.draw(basic.screen)
    sprites2.draw(basic.screen)
    basic.screen.blit(level_1, (30, 660))
    basic.screen.blit(level_5, (30, 485))
    basic.screen.blit(level_10, (30, 270))
    basic.screen.blit(level_15, (30, 55))
    basic.screen.blit(finish, (30, 10))
    basic.screen.blit(pijltoetsen, (1000, 470))
#laat de background zien
def blit_bg():
    global bg
    bg = pygame.transform.scale(bg,(1280,800))
    basic.screen.blit(bg, (0,0)) 
