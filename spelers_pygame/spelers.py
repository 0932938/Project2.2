import pygame

Black = (0, 0, 0)
White = (255, 255, 255)
Blue = (0, 0, 255)
Red = (255, 0, 0)
Green = (0,255,0)
Yellow = (255,255,0)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

P1Health = 5
P2Health = 5
P3Health = 5
P4Health = 5

bg = pygame.image.load("bb.jpg")
bg = pygame.transform.scale(bg, (800,510))

class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    walls = None


    def __init__(self, x, y):
        super(type(self), self).__init__()

        # self.image=pygame.Surface([20,20])
        # self.image.fill(White)
        self.image = pygame.image.load("8bit.png").convert()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def loop(self, x, y):
        self.rect.x += x
        self.rect.y += y


    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y


class Player_2(pygame.sprite.Sprite):
    walking_x = 0
    walking_y = 0


    # Constructor
    def __init__(self, x, y):
        super(type(self), self).__init__()

        # self.image=pygame.Surface([20,20])
        # self.image.fill(White)
        self.image = pygame.image.load("8bit.png").convert()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def loop(self, x, y):
        self.walking_x = x
        self.walking_y = y


    def update(self):
        self.rect.x += self.walking_x

        self.rect.y += self.walking_y




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

wall_1 = Wall(102, 5, 10, 560)
wall_list.add(wall_1)
wall_1.image.fill(Red)
sprites.add(wall_1)

wall_2 = Wall(154, 5, 3, 560)
wall_list.add(wall_2)
sprites.add(wall_2)

wall_3 = Wall(207, 5, 3, 560)
wall_list.add(wall_3)
wall_3.image.fill(Yellow)
sprites.add(wall_3)

wall_4 = Wall(259, 5, 3, 560)
wall_list.add(wall_4)
wall_4.image.fill(Green)
sprites.add(wall_4)

wall_5 = Wall(312, 5, 3, 560)
wall_list.add(wall_5)
sprites.add(wall_5)

#player1_list = pygame.sprite.Group()
#player2_list = pygame.sprite.Group()

player1 = Player(108, 450)
player1.walls = wall_list

sprites.add(player1)
player1_list.add(player1)

player2 = Player_2(160, 450)
player2.walls = wall_list
player2_list.add(player2)

sprites.add(player2)

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

            if event.key == pygame.K_LEFT:
                player1.loop(-25, 0)
            elif event.key == pygame.K_RIGHT:
                player1.loop(40, 0)
            elif event.key == pygame.K_DOWN:
                player1.loop(0, 5)
            elif event.key == pygame.K_UP:
                player1.loop(0, -5)


            elif event.key == pygame.K_a:
                pass #player2.
            elif event.key == pygame.K_d:
                pass #player2.
            elif event.key == pygame.K_s:
                pass #player2.
            elif event.key == pygame.K_w:
                pass #player2.


    sprites.update()

    screen.blit(bg, (0,0))
    player1health = font.render("Player 1 Health: " + str(P1Health), True, White)

    player2health = font.render("Player 2 Health: " + str(P2Health), True, White)
    screen.blit(player1health, [650, 210])
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