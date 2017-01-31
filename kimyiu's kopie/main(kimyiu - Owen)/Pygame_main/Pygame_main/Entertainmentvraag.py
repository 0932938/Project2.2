import pygame, time, random, basic

pygame.init()
basic.screen
basic.clock

Ent_vraag = 0
Ent_weergave = False
Ent_gekozen = False
empy_frame = pygame.image.load("Blanco_Frame.png")  
correct = pygame.image.load('Correct.png')
incorrect = pygame.image.load('Incorrect.png')
#Dit zijn alle afbeeldingen van de vragen
# entertainmentvragen afbeeldingen
ev1 = pygame.image.load('entertainmentvragen 1.jpg')
ev2 = pygame.image.load('entertainmentvragen 2.jpg')
ev3 = pygame.image.load('entertainmentvragen 3.jpg')
ev4 = pygame.image.load('entertainmentvragen 4.jpg')
ev5 = pygame.image.load('entertainmentvragen 5.jpg')
ev6 = pygame.image.load('entertainmentvragen 6.jpg')
ev7 = pygame.image.load('entertainmentvragen 7.jpg')
ev8 = pygame.image.load('entertainmentvragen 8.jpg')
ev9 = pygame.image.load('entertainmentvragen 9.jpg')
ev10 = pygame.image.load('entertainmentvragen 10.jpg')
ev11 = pygame.image.load('entertainmentvragen 11.jpg')
ev12 = pygame.image.load('entertainmentvragen 12.jpg')
ev13 = pygame.image.load('entertainmentvragen 13.jpg')
ev14 = pygame.image.load('entertainmentvragen 14.jpg')
ev15 = pygame.image.load('entertainmentvragen 15.jpg')


def random_Ent(): 
    Entvragen = [1,2,6,7,8,9,10,11,12,13, 15]
    Sresult = random.choice(Entvragen)
    return Sresult


def antwoordcorrect():
    basic.screen.blit(correct,(0,0))
    
def antwoordincorrect():
    basic.screen.blit(incorrect, (0,0))


def display_Ent(Ent):
    if(Ent == 1): 
        basic.screen.blit(ev1, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(Ent == 2): 
        basic.screen.blit(ev2, (330,170))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(Ent == 3): 
        basic.screen.blit(ev3, (0,0))
        pygame.display.flip()
    elif(Ent == 4): 
        basic.screen.blit(ev4, (0,0))
        pygame.display.flip()
    elif(Ent == 5): 
        basic.screen.blit(ev5, (0,0))
        pygame.display.flip()
    elif(Ent == 6): 
        basic.screen.blit(ev6, (0,0))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(Ent == 7): 
        basic.screen.blit(ev7, (0,0))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onuist
        pygame.display.flip()
    elif(Ent == 8): 
        basic.screen.blit(ev8, (0,0))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(Ent == 9): 
        basic.screen.blit(ev9, (0,0))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordcorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(Ent == 10): 
        basic.screen.blit(ev10, (0,0))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onuist
        pygame.display.flip()
    elif(Ent == 11): 
        basic.screen.blit(ev11, (0,0))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onuist
        pygame.display.flip()
    elif(Ent == 12): 
        basic.screen.blit(ev12, (0,0))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(Ent == 13): 
        basic.screen.blit(ev13, (0,0))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()
    elif(Ent == 14): 
        basic.screen.blit(ev14, (0,0))

        pygame.display.flip()
    elif(Ent == 15): 
        basic.screen.blit(ev15, (0,0))
        basic.button("A", 950,200,80,83,(139,131,134),(75,75,75), antwoordincorrect) #correct !!!
        basic.button("B", 950,315,80,83,(139,131,134),(75,75,75), antwoordcorrect) # onjuist
        basic.button("C", 950,430,80,83,(139,131,134),(75,75,75), antwoordincorrect) # onuist
        pygame.display.flip()

def before_display():
    basic.screen.blit(empy_frame,(0,0))
    basic.button("show vragen", 372,357,560,83,(139,131,134),(75,75,75), displayfunc)
    

def displayfunc():
    global Ent_vraag, Ent_weergave 
    Ent_vraag = random_Ent()
    Ent_weergave = True

def Entdisplay():
    global Ent_gekozen, Ent_weergave
    Ent_weergave = False
    while Ent_gekozen == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Ent_gekozen = True 
        before_display()
        display_Ent(Ent_vraag)
        pygame.display.flip()

