import pygame, pygame.mixer ,sys

pygame.init()

black = (0, 0, 0)
gray = (120, 120, 120)
white = (255, 255, 255)
red = (255, 0, 0)
d_red = (139,0,0)
dark_red = (150,0,0)
red2 = (200,0,0)

d_blue = (30, 114, 225)
blue = (0, 0, 255)
dark_blue   = (0,0,200)
blue2        = (0,50,255)
light_blue  = (0,100,255)

d_red = (139,0,0)
yellow = (227,207,87)
yellow2 = (255,255,0)
light_yellow  = (255,255,100)
d_yellow = (150,150,0)
gold = (255, 215,0)

green = (0,128,0)
lime = (0, 255, 0)
dark_green = (0,150,0)
green2= (0,200,0)

#screen size
width = 1280
height = 720
size = (width,height)

#fonts
antwoordvak_font = pygame.font.SysFont("Arial black",24)


empy_frame = pygame.image.load("Blanco_Frame.png")  
correct = pygame.image.load('Correct.png')
incorrect = pygame.image.load('Incorrect.png')
#screen 
screen = pygame.display.set_mode((size))
pygame.display.set_caption('Beklim de Euromast')
clock = pygame.time.Clock()

#def timer():
#        timerbg = pygame.image.load("timerbg.png")
#        counter = 50
#        text = ""
#        pygame.time.set_timer(pygame.USEREVENT, 1000)
#        font = pygame.font.SysFont('Consolas', 30)

#        while True:
#            for e in pygame.event.get():
#                if e.type == pygame.USEREVENT:
#                    counter -= 1
#                    text = str(counter) if counter > 0 else 'TIMEOUT!'
#                if e.type == pygame.QUIT: break
#            else:
#                screen.blit(timerbg, (610,140))
#                screen.blit(font.render(text, True, (0, 0, 0)), (640, 150))
#                pygame.display.flip()
#                clock.tick(60)


#text for button
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# text on display(large text) 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2),(height/2))
    screen.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 
# buttons to click on
def button(msg,x,y,w,h,ic,ac,action=None):
    Csound = pygame.mixer.Sound("moving cursor.wav")
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            Csound.play()
            pygame.time.delay(1000)
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("Arial black",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)


def button2(msg, x, y, w, h, ic, ac, action=None):
    Csound = pygame.mixer.Sound("moving cursor.wav")
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[1] == 0 and action != None:
            Csound.play()
            pygame.time.delay(1000)
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("Arial black", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)


def tekstvak(msg, x, y, w, h, ac):
    pygame.draw.rect(screen, ac, (x, y, w, h))
    smallText = pygame.font.SysFont("Arial black", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)