import pygame

Black = (0, 0, 0)
White = (255, 255, 255)
Blue = (0, 0, 255)
Red = (255, 0, 0)
Green = (0,255,0,)
Yellow = (255,255,0)
Gold = (255,215,0)


SCREEN_WIDTH = 820
SCREEN_HEIGHT = 510

P1Health = 5
P2Health = 5
P3Health = 5
P4Health = 5

bg = pygame.image.load("eurimast.jpg")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH,SCREEN_HEIGHT))


class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0

    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self) #super(type(self), self).__init__()
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def loop(self, x, y):
        self.rect.x += x
        self.rect.y += y


    def update(self):
        #move up and down
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if not (0 < self.rect.y < 480):
            player1.rect.x = 155
            player1.rect.y = 450
        # if not (0 < player2.rect.y < 450):
            player2.rect.x = 184
            player2.rect.y = 450

            player3.rect.x = 95
            player3.rect.y = 450

            player4.rect.x = 125
            player4.rect.y = 450

        #
        # if self.rect.x < 80:
        #     self.rect.x = 184
        # if self.rect.x > 190:
        #     self.rect.x = 95



class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.image.fill(Blue)

def wall_detection(player_turn):
    if player_turn == 1:
        if player1.rect.x < 80:
            player1.rect.x = 184
        if player1.rect.x > 190:
            player1.rect.x = 95
    if player_turn == 2:
        if player2.rect.x < 80:
            player2.rect.x = 184
        if player2.rect.x > 190:
            player2.rect.x = 95
    if player_turn == 3:
        if player3.rect.x < 80:
            player3.rect.x = 184
        if player3.rect.x > 190:
            player3.rect.x = 95
    if player_turn == 4:
        if player4.rect.x < 80:
            player4.rect.x = 184
        if player4.rect.x > 190:
            player4.rect.x = 95

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("EUROMAST")
sprites = pygame.sprite.Group()

wall_list = pygame.sprite.Group()

wall_1 = Wall(100, 4, 10, 560,)
wall_list.add(wall_1)
wall_1.image.fill(Blue)
sprites.add(wall_1)

wall_2 = Wall(130,4, 10, 560)
wall_list.add(wall_2)
wall_1.image.fill(Red)
sprites.add(wall_2)

wall_3 = Wall(160, 4, 10, 560)
wall_list.add(wall_3)
wall_3.image.fill(Yellow)
sprites.add(wall_3)

wall_4 = Wall(190, 4, 10, 560)
wall_list.add(wall_4)
wall_4.image.fill(Green)
sprites.add(wall_4)

wall_5 = Wall(220, 4, 10, 560)
wall_list.add(wall_5)
wall_5.image.fill(Red)
sprites.add(wall_5)
                                # (x,y)
pygame.draw.line(bg, Blue, (0, 450), (300, 450))
pygame.draw.line(bg, Blue, (0, 422), (300, 422))
pygame.draw.line(bg, Blue, (0, 394), (300, 394))

pygame.draw.line(bg, Blue, (0, 366), (300, 366))
pygame.draw.line(bg, Blue, (0, 338), (300, 338))
pygame.draw.line(bg, Blue, (0, 310), (300, 310))

pygame.draw.line(bg, Blue, (0, 282), (300, 282))
pygame.draw.line(bg, Blue, (0, 254), (300, 254))
pygame.draw.line(bg, Blue, (0, 226), (300, 226))

pygame.draw.line(bg, Blue, (0, 198), (300, 198))
pygame.draw.line(bg, Blue, (0, 170), (300, 170))
pygame.draw.line(bg, Blue, (0, 142), (300, 142))

pygame.draw.line(bg, Blue, (0, 114), (300, 114))
pygame.draw.line(bg, Blue, (0, 86), (300, 86))
pygame.draw.line(bg, Blue, (0, 58), (300, 58))

pygame.draw.line(bg, Gold, (0, 30), (300, 30),3)
pygame.draw.line(bg, Gold, (0, 2), (300, 2),3)



# cord = pygame.rect.get_pos()
# def collide(self, player1,player2):
#     if player1.rect.y[cord] == player2.rect.y[cord] and player2.rect.x[cord] == player2.rect.x[cord] :
#         player2.rect.y -= 13
#         player2.rect.x -= 13

player1_list = pygame.sprite.Group()
player2_list = pygame.sprite.Group()

player1 = Player(150, 450, "avatar1_standingv1.png") #gele pop

player1_list.add(player1)
sprites.add(player1)

player2 = Player(185, 450, "avatar2_standingv1.png") #groene pop
sprites.add(player2)

player3 = Player(210, 450, "avatar3_standingv1.png") #rode pop
sprites.add(player3)

player4 = Player(240, 450, "avatar4_standingv1.png") #blauwe pop
sprites.add(player4)

font = pygame.font.SysFont('Arial', 18, False, False)

text2 = font.render("Game Over. Player 2 Wins !", True, White)
text2_rect = text2.get_rect()
text2_x = screen.get_width() / 2 - text2_rect.width / 2
text2_y = screen.get_height() / 2 - text2_rect.height / 2

text1 = font.render("Game Over. Player 1 Wins !", True, White)
text1_rect = text1.get_rect()
text1_x = screen.get_width() / 2 - text1_rect.width / 2
text1_y = screen.get_height() / 2 - text1_rect.height / 2

clock = pygame.time.Clock()

player_turn = 1
#player_moves wordt de dobbelsteen worp uitkomst
player_moves = 2

done = False
gameover = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and gameover == False:
            #player1.key.get_focused()
            if event.key == pygame.K_LEFT:
                if player_turn == 1:
                    while player_moves > 0:
                        player1.loop(-28.5, 0)
                        player_moves -= 1
                        wall_detection(player_turn)
                    player_turn = 2
                    player_moves = 2
                elif player_turn == 2:
                    while player_moves > 0:
                        player2.loop(-28.5, 0)
                        player_moves -= 1
                        wall_detection(player_turn)
                    player_turn = 3
                    player_moves = 2
                elif player_turn == 3:
                    while player_moves > 0:
                        player3.loop(-28.5, 0)
                        player_moves -= 1
                        wall_detection(player_turn)
                    player_turn = 4
                    player_moves = 2
                elif player_turn == 4:
                    while player_moves > 0:
                        player4.loop(-28.5, 0)
                        player_moves -= 1
                        wall_detection(player_turn)
                    player_turn = 1
                    player_moves = 2
                print(player1.rect.x, "<x,y>" ,player1.rect.y)
            elif event.key == pygame.K_RIGHT:
                if player_turn == 1:
                    while player_moves > 0:
                        player1.loop(29, 0)
                        player_moves -= 1
                        wall_detection(player_turn)
                    player_turn = 2
                    player_moves = 2
                elif player_turn == 2:
                    while player_moves > 0:
                        player2.loop(29, 0)
                        player_moves -= 1
                        wall_detection(player_turn)
                    player_turn = 3
                    player_moves = 2
                elif player_turn == 3:
                    while player_moves > 0:
                        player3.loop(29, 0)
                        player_moves -= 1
                        wall_detection(player_turn)
                    player_turn = 4
                    player_moves = 2
                elif player_turn == 4:
                    while player_moves > 0:
                        player4.loop(29, 0)
                        player_moves -= 1
                        wall_detection(player_turn)
                    player_turn = 1
                    player_moves = 2

                # if player_turn == 1:
                #     while player_moves > 0:
                #         player1.loop(29, 0)
                #         player_moves -= 1
                #         wall_detection(player_turn)
                #     player_turn = 2
                #     player_moves = 2
                # elif player_turn == 2:
                #     while player_moves > 0:
                #         player2.loop(29, 0)
                #         player_moves -= 1
                #         if player2.rect.x < 80:
                #             player2.rect.x = 210
                #     player_turn = 3
                #     player_moves = 2
                # elif player_turn == 3:
                #     while player_moves > 0:
                #         player3.loop(29, 0)
                #         player_moves -= 1
                #         if player3.rect.x < 80:
                #             player3.rect.x = 210
                #     player_turn = 4
                #     player_moves = 2
                # elif player_turn == 4:
                #     while player_moves > 0:
                #         player4.loop(29, 0)
                #         player_moves -= 1
                #         if player4.rect.x < 80:
                #             player4.rect.x = 210
                #     player_turn = 1
                #     player_moves = 2

            # elif event.key == pygame.K_DOWN:
            #     player1.loop(0, 10)
            elif event.key == pygame.K_UP:
                if player_turn == 1:
                    while player_moves > 0:
                        player1.loop(0, -28)
                        player_moves -= 1
                        wall_detection(player_turn)
                    player_turn = 2
                    player_moves = 2
                elif player_turn == 2:
                    while player_moves > 0:
                        player2.loop(0, -28)
                        player_moves -= 1
                        wall_detection(player_turn)
                    player_turn = 3
                    player_moves = 2
                elif player_turn == 3:
                    while player_moves > 0:
                        player3.loop(0, -28)
                        player_moves -= 1
                        wall_detection(player_turn)
                    player_turn = 4
                    player_moves = 2
                elif player_turn == 4:
                    while player_moves > 0:
                        player4.loop(0, -28)
                        player_moves -= 1
                        wall_detection(player_turn)
                    player_turn = 1
                    player_moves = 2
                # if player_turn == 1:
                #     player1.loop(0, -28)
                #     print(player_turn)
                #     # player_moves -= 1
                #     print(player1.rect.x, "<x Player 1 y>", player1.rect.y)
                # elif player_turn == 2:
                #     player2.loop(0, -28)
                #     # player_moves -= 1
                #     print(player2.rect.x, "<x Player 2 y>", player2.rect.y)
                # elif player_turn == 3:
                #     player3.loop(0, -28)
                #     # player_moves -= 1
                #     print(player3.rect.x, "<x Player 3 y>", player3.rect.y)
                #     if player_turn == 3:
                #         player_turn = 1

    sprites.update()

    screen.blit(bg, (0,0))
    player1health = font.render("Player 1 Health: " + str(P1Health), True, White)
    screen.blit(player1health, [650, 210])

    player2health = font.render("Player 2 Health: " + str(P2Health), True, White)
    screen.blit(player2health, [650, 234])
    sprites.draw(screen)

    if (P1Health <= 0):
        screen.blit(text2, [text2_x, text2_y])
        gameover = True
    elif (P2Health <= 0):
        screen.blit(text1, [text1_x, text1_y])
        gameover = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()