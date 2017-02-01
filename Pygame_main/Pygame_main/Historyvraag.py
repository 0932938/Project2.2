import pygame, pygame.mixer, time, random, basic, Pregame, Players

correctsound = pygame.mixer.Sound("claps3.wav")
incorrectsound = pygame.mixer.Sound("missed.wav")
pygame.init()
basic.screen
basic.clock

hist_vraag = 0
hist_weergave = False
hist_gekozen = False
empy_frame = pygame.image.load("Blanco_Frame.png")  
correct = pygame.image.load('Correct.png')
incorrect = pygame.image.load('Incorrect.png')
#Dit zijn alle afbeeldingen van de vragen
# historyvragen afbeeldingen
hv1 = pygame.image.load('historyvragen 1.jpg')
hv2 = pygame.image.load('historyvragen 2.jpg')
hv3 = pygame.image.load('historyvragen 3.jpg')
hv4 = pygame.image.load('historyvragen 4.jpg')
hv5 = pygame.image.load('historyvragen 5.jpg')
hv6 = pygame.image.load('historyvragen 6.jpg')
hv7 = pygame.image.load('historyvragen 7.jpg')
hv8 = pygame.image.load('historyvragen 8.jpg')
hv9 = pygame.image.load('historyvragen 9.jpg')
hv10 = pygame.image.load('historyvragen 10.jpg')
hv11 = pygame.image.load('historyvragen 11.jpg')
hv12 = pygame.image.load('historyvragen 12.jpg')
hv13 = pygame.image.load('historyvragen 13.jpg')
hv14 = pygame.image.load('historyvragen 14.jpg')
hv15 = pygame.image.load('historyvragen 15.jpg')

historyvragen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
def random_hist():

    hist_vraag = random.choice(historyvragen)
    return hist_vraag


def antwoordcorrect():
    global hist_vraag
    basic.screen.blit(correct,(1065, 260))
    pygame.display.flip()
    correctsound.play()
    pygame.time.delay(1500)
    historyvragen.remove(hist_vraag)
    Players.player_game(3) ## <-  HIER TOEGEVOEDD [VERWIJDER COMMENT]
    pygame.time.delay(3000)

def antwoordincorrect():
    basic.screen.blit(incorrect, (1065, 260))
    pygame.display.flip()
    incorrectsound.play()
    pygame.time.delay(2000)

def display_hist(hist):
    if(hist == 1):
        basic.screen.blit(hv1, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(hist  == 2):
        basic.screen.blit(hv2, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(hist  == 3):
        basic.screen.blit(hv3, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(hist  == 4):
        basic.screen.blit(hv4, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onuist
        pygame.display.flip()
    elif(hist  == 5):
        basic.screen.blit(hv5, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(hist  == 6):
        basic.screen.blit(hv6, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onuist
        pygame.display.flip()
    elif(hist  == 7):
        basic.screen.blit(hv7, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(hist  == 8):
        basic.screen.blit(hv8, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(hist  == 9):
        basic.screen.blit(hv9, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(hist  == 10):
        basic.screen.blit(hv10, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(hist  == 11):
        basic.screen.blit(hv11, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(hist  == 12):
        basic.screen.blit(hv12, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        pygame.display.flip()
    elif(hist  == 13):
        basic.screen.blit(hv13, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onuist
        pygame.display.flip()
    elif(hist  == 14):
        basic.screen.blit(hv14, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        pygame.display.flip()
    elif(hist  == 15):
        basic.screen.blit(hv15, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()

def before_display():
    basic.screen.blit(empy_frame,(0,0))
    basic.button("show vragen", 372,357,560,83,(139,131,134),(75,75,75), displayfunc)
    

def displayfunc():
    global hist_vraag, hist_weergave
    hist_vraag = random_hist()
    hist_weergave = True

def histdisplay():
    global hist_gekozen, hist_weergave, hist_vraag
    hist_weergave = False
    hist_vraag = random_hist()
    while hist_gekozen == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                hist_gekozen = True
        before_display()
        display_hist(hist_vraag)
        if antwoordcorrect: #<-- HIER TOEGEVOEDD [VERWIJDER COMMENT]
            Players.screen.blit
            Players.player_game
            Players.player_game
   
        pygame.display.flip()

