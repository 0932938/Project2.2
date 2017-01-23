import pygame, pygame.mixer ,sys

pygame.init()

black = (0, 0, 0)
gray = (120, 120, 120)
white = (255, 255, 255)
red = (255, 0, 0)
lime = (0, 255, 0)
blue = (0, 0, 255)
d_red = (139,0,0)
yellow = (227,207,87)
gold = (255, 215,0)
green = (0,128,0)
d_blue = (30, 114, 225)

#screen size
width = 1280
height = 720
size = (width,height)

#screen 
screen = pygame.display.set_mode((size))
pygame.display.set_caption('Beklim de Euromast')
clock = pygame.time.Clock()

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