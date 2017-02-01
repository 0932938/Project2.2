import pygame, pygame.mixer, time, random, basic, Pregame, Players

correctsound = pygame.mixer.Sound("claps3.wav")
incorrectsound = pygame.mixer.Sound("missed.wav")
pygame.init()
basic.screen
basic.clock

Sport_vraag = 0
Sport_weergave = False
Sport_gekozen = False
empy_frame = pygame.image.load("Blanco_Frame.png")  
correct = pygame.image.load('Correct.png')
incorrect = pygame.image.load('Incorrect.png')
#Dit zijn alle afbeeldingen van de vragen
#sportvraag afbeeldingen
sv1 = pygame.image.load('sportvragen 1.jpg')
sv2 = pygame.image.load('sportvragen 2.jpg')
sv3 = pygame.image.load('sportvragen 3.jpg')
sv4 = pygame.image.load('sportvragen 4.jpg')
sv5 = pygame.image.load('sportvragen 5.jpg')
sv6 = pygame.image.load('sportvragen 6.jpg')
sv7 = pygame.image.load('sportvragen 7.jpg')
sv8 = pygame.image.load('sportvragen 8.jpg')
sv9 = pygame.image.load('sportvragen 9.jpg')
sv10 = pygame.image.load('sportvragen 10.jpg')
sv11 = pygame.image.load('sportvragen 11.jpg')
sv12 = pygame.image.load('sportvragen 12.jpg')
sv13 = pygame.image.load('sportvragen 13.jpg')
sv14 = pygame.image.load('sportvragen 14.jpg')
sv15 = pygame.image.load('sportvragen 15.jpg')

sportvragen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
def random_sport(): 

    Sport_vraag = random.choice(sportvragen)
    return Sport_vraag



def antwoordcorrect():
    global Sport_vraag
    basic.screen.blit(correct,(1065, 260))
    pygame.display.flip()
    correctsound.play()
    pygame.time.delay(1500)
    sportvragen.remove(Sport_vraag)
    Players.player_game(4) ## <-  HIER TOEGEVOEDD [VERWIJDER COMMENT]
    pygame.time.delay(3000)


def antwoordincorrect():
    global Sport_gekozen
    basic.screen.blit(incorrect, (1065, 260))
    pygame.display.flip()
    Sport_gekozen = True
    incorrectsound.play()
    pygame.time.delay(2000)

def display_sport(sport):
    if(sport == 1):
        basic.screen.blit(sv1, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(sport == 2):
        basic.screen.blit(sv2, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(sport == 3):
        basic.screen.blit(sv3, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(sport == 4):
        basic.screen.blit(sv4, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(sport == 5):
        basic.screen.blit(sv5, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(sport == 6):
        basic.screen.blit(sv6, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onuist
        pygame.display.flip()
    elif(sport == 7):
        basic.screen.blit(sv7, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(sport == 8):
        basic.screen.blit(sv8, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onuist
        pygame.display.flip()
    elif(sport == 9):
        basic.screen.blit(sv9, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(sport == 10):
        basic.screen.blit(sv10, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onuist
        pygame.display.flip()
    elif(sport == 11):
        basic.screen.blit(sv11, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onuist
        pygame.display.flip()
    elif(sport == 12):
        basic.screen.blit(sv12, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onuist
        pygame.display.flip()
    elif(sport == 13):
        basic.screen.blit(sv13, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onuist
        pygame.display.flip()
    elif(sport == 14):
        basic.screen.blit(sv14, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(sport == 15):
        basic.screen.blit(sv15, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()

def before_display():
    basic.screen.blit(empy_frame,(0,0))
    basic.button("show vragen", 372,357,560,83,(139,131,134),(75,75,75), displayfunc)

def displayfunc():
    global Sport_vraag, Sport_weergave
    Sport_vraag = random_tech()
    Sport_weergave = True

def Sportdisplay():
    global Sport_gekozen, Sport_weergave, Sport_vraag
    Sport_gekozen = False
    Sport_weergave = False
    Sport_vraag = random_sport()

    while Sport_gekozen == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Sport_gekozen = True
        before_display()
        display_sport(Sport_vraag)
        if antwoordcorrect: #<-- HIER TOEGEVOEDD [VERWIJDER COMMENT]
            Players.screen.blit
            Players.player_game
            Players.player_game
        pygame.display.flip()

