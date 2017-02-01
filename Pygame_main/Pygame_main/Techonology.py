import pygame, pygame.mixer, time, random, basic, Pregame, Players

correctsound = pygame.mixer.Sound("claps3.wav")
incorrectsound = pygame.mixer.Sound("missed.wav")
pygame.init()
basic.screen
basic.clock

tech_vraag = 0
tech_weergave = False
tech_gekozen = False
empy_frame = pygame.image.load("Blanco_Frame.png")  
correct = pygame.image.load('Correct.png')
incorrect = pygame.image.load('Incorrect.png')
#Dit zijn alle afbeeldingen van de vragen
tv1 = pygame.image.load('technologievragen 1.jpg')
tv2 = pygame.image.load('technologievragen 2.jpg')
tv3 = pygame.image.load('technologievragen 3.jpg')
tv4 = pygame.image.load('technologievragen 4.jpg')
tv5 = pygame.image.load('technologievragen 5.jpg')
tv6 = pygame.image.load('technologievragen 6.jpg')
tv7 = pygame.image.load('technologievragen 7.jpg')
tv8 = pygame.image.load('technologievragen 8.jpg')
tv9 = pygame.image.load('technologievragen 9.jpg')
tv10 = pygame.image.load('technologievragen 10.jpg')
tv11 = pygame.image.load('technologievragen 11.jpg')
tv12 = pygame.image.load('technologievragen 12.jpg')
tv13 = pygame.image.load('technologievragen 13.jpg')
tv14 = pygame.image.load('technologievragen 14.jpg')
tv15 = pygame.image.load('technologievragen 15.jpg')

techvragen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
def random_tech():

    tech_vraag = random.choice(techvragen)
    return tech_vraag


def antwoordcorrect():
    global tech_vraag
    basic.screen.blit(correct,(1065, 260))
    pygame.display.flip()
    correctsound.play()
    pygame.time.delay(1500)
    techvragen.remove(tech_vraag)
    Players.player_game(1) ## <-  HIER TOEGEVOEDD [VERWIJDER COMMENT]
    pygame.time.delay(3000)


def antwoordincorrect():
    global tech_gekozen
    basic.screen.blit(incorrect, (1065, 260))
    incorrectsound.play()
    pygame.display.flip()
    tech_gekozen = True
    pygame.time.delay(2000)

def display_tech(tech):
    if(tech == 1):
        basic.screen.blit(tv1, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(tech == 2):
        basic.screen.blit(tv2, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onuist
        pygame.display.flip()
    elif(tech == 3):
        basic.screen.blit(tv3, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(tech == 4):
        basic.screen.blit(tv4, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onuist
        pygame.display.flip()
    elif(tech == 5):
        basic.screen.blit(tv5, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(tech == 6):
        basic.screen.blit(tv6, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(tech == 7):
        basic.screen.blit(tv7, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(tech == 8):
        basic.screen.blit(tv8, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(tech == 9):
        basic.screen.blit(tv9, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(tech == 10):
        basic.screen.blit(tv10, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onuist
        pygame.display.flip()
    elif(tech == 11):
        basic.screen.blit(tv11, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(tech == 12):
        basic.screen.blit(tv12, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(tech == 13):
        basic.screen.blit(tv13, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(tech == 14):
        basic.screen.blit(tv14, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(tech == 15):
        basic.screen.blit(tv15, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onuist
        pygame.display.flip()

def before_display():
    basic.screen.blit(empy_frame,(0,0))
    basic.button("show vragen", 372,357,560,83,(139,131,134),(75,75,75), displayfunc)

def displayfunc():
    global tech_vraag, tech_weergave
    tech_vraag = random_tech()
    tech_weergave = True

def techdisplay():
    global tech_gekozen, tech_weergave, tech_vraag
    tech_gekozen = False
    tech_weergave = False
    tech_vraag = random_tech()

    while tech_gekozen == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                tech_gekozen = True
        before_display()
        display_tech(tech_vraag)
        if antwoordcorrect: #<-- HIER TOEGEVOEDD [VERWIJDER COMMENT]
            Players.screen.blit
            Players.player_game
            Players.player_game
        pygame.display.flip()

