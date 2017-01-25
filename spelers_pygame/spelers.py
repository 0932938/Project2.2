import pygame

Black = (0, 0, 0)
White = (255, 255, 255)
Blue = (0, 0, 255)
Red = (255, 0, 0)
Green = (0,255,0,)
Yellow = (255,255,0)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

P1Health = 5
P2Health = 5
P3Health = 5
P4Health = 5

bg = pygame.image.load("eurimast.jpg")
bg = pygame.transform.scale(bg, (850,510))

player_turn = 0
#player_moves wordt de dobbelsteen worp uitkomst
player_moves = 2

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
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if not (0 < self.rect.y < 450):
            player1.rect.x = 180
            player1.rect.y = 440
        # if not (0 < player2.rect.y < 450):
            player2.rect.x = 150
            player2.rect.y = 440
        if self.rect.x < 80:
            self.rect.x = 210
        if self.rect.x > 211:
            self.rect.x = 90



class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super(type(self), self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(Blue)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("EUROMAST")
sprites = pygame.sprite.Group()
player1_list = pygame.sprite.Group()
player2_list = pygame.sprite.Group()

wall_list = pygame.sprite.Group()

wall_1 = Wall(100, 5, 10, 560,)
wall_list.add(wall_1)
wall_1.image.fill(Red)
sprites.add(wall_1)

wall_2 = Wall(130, 5, 10, 560)
wall_list.add(wall_2)
sprites.add(wall_2)

wall_3 = Wall(160, 5, 10, 560)
wall_list.add(wall_3)
wall_3.image.fill(Yellow)
sprites.add(wall_3)

wall_4 = Wall(190, 5, 10, 560)
wall_list.add(wall_4)
wall_4.image.fill(Green)
sprites.add(wall_4)

wall_5 = Wall(220, 5, 10, 560)
wall_list.add(wall_5)
wall_5.image.fill(Red)
sprites.add(wall_5)
                                # (x,y)
pygame.draw.line(bg, Black, (0, 390), (300, 390))
pygame.draw.line(bg, Black, (0, 350), (300, 350))
pygame.draw.line(bg, (0, 0, 255), (0, 280), (300, 280))

pygame.draw.line(bg, (0, 0, 255), (0, 390), (300, 390))
pygame.draw.line(bg, (0, 0, 255), (0, 350), (300, 350))
pygame.draw.line(bg, (0, 0, 255), (0, 280), (300, 280))

pygame.draw.line(bg, (0, 0, 255), (0, 50), (300, 50))
pygame.draw.line(bg, (0, 0, 255), (0, 30), (300, 30))
pygame.draw.line(bg, (0, 0, 255), (0, 10), (300, 10))




def collide(self, player1,player2):
    if player1.rect.y+5 == player1.rect.y+5 and player2.rect.x+5 == player2.rect.x+5 :
        player2.rect.y -= 13
        player2.rect.x -= 13

#player1_list = pygame.sprite.Group()
#player2_list = pygame.sprite.Group()

player1 = Player(180, 450, "avatar2_standing.png" )
player1_list.add(player1)
sprites.add(player1)


player2 = Player(155, 450, "avatar1_standing.png")
sprites.add(player2)
player2_list.add(player2)



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
                    player1.loop(-28.5, 0)
                    player2.loop(-28.5, 0)
                print(player1.rect.x)
            elif event.key == pygame.K_RIGHT:
                player1.loop(29, 0)
                player2.loop(29, 0)
                if player_turn == 1:
                    while player_moves > 0:
                        player1.loop(-28.5, 0)
                        player_moves -= 1
                        # if player1.rect.x <80:
                        #     player1.rect.x = 210
                    player_turn = 2
                    player_moves = 2
                elif player_turn == 2:
                    while player_moves > 0:
                        player2.loop(-28.5, 0)
                        player_moves -= 1
                        # if player2.rect.x < 80:
                        #     player2.rect.x = 210
                     # player_turn = 1
                # elif player_turn == 3:
                #     while player_moves > 0:
                #         player3.loop(-28.5, 0)
                #         player_moves -= 1
                #         if player3.rect.x < 80:
                #             player3.rect.x = 210
                #     player_turn = 4
                # elif player_turn == 4:
                #     while player_moves > 0:
                #         player4.loop(-28.5, 0)
                #         player_moves -= 1
                #         if player4.rect.x < 80:
                #             player4.rect.x = 210
                #     player_turn = 1

            # elif event.key == pygame.K_DOWN:
            #     player1.loop(0, 10)
            elif event.key == pygame.K_UP:
                player1.loop(0, -28)
                player2.loop(0, -28)

            # elif event.key == pygame.K_a:
            #     player2.loop(-27, 0)
            # elif event.key == pygame.K_d:
            #     player2.loop(27,0)
            # elif event.key == pygame.K_s:
            #     pass #player2.
            # elif event.key == pygame.K_w:
            #     pass #player2.


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