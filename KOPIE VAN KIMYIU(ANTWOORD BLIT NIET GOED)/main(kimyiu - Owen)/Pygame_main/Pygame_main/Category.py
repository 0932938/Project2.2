import pygame , time, random, basic, Sportvraag, Entertainmentvraag, Historyvraag, Techonology
pygame.init()

basic.screen
basic.clock
FIRST_DICE = 0
already_rolled = False
Catergory_selected = False 
bg = pygame.image.load("bb.jpg")
cpup = pygame.image.load("Blanco_Frame.png")  
Open_vraag = pygame.image.load('Openvraag.png')
Meerkeu_vraag = pygame.image.load('Meerkeuze.png')

# picking a rondom type of Question
def roll_a_dice():
    typeQ = ["open"] * 0 + ["meerkeuze"] * 100
    result = random.choice(typeQ)
    return result

# determines which first dice is used
def display_first(first):

    if (first == "open"):
        basic.screen.blit(Open_vraag,(0,0))
        produce_large_text("Klik Doorgaan", 575,250)
        produce_small_text("Type vraag", 615,152) 
        basic.button("Doorgaan", 423,520,458,32, basic.yellow, basic.gold, Select_Catagory)
        pygame.display.flip()
    elif (first == "meerkeuze"):
        basic.screen.blit(Meerkeu_vraag,(0,0))
        produce_large_text("Klik Doorgaan", 575,250)
        produce_small_text("Type vraag", 615,152) 
        basic.button("Doorgaan", 423,520,458,32,basic.yellow,basic.gold, Select_Catagory)
        pygame.display.flip()
       
# messages on screen
def produce_large_text(text, x, y):
    our_font = pygame.font.SysFont("Arial black", 20)
    #render the text now
    produce_text = our_font.render(text, 1, basic.black)
    basic.screen.blit(produce_text, (x, y))

def produce_small_text(text, x, y):
    our_font = pygame.font.SysFont("Arial black", 15)
    #render the text now
    produce_text = our_font.render(text, 1, basic.black)
    basic.screen.blit(produce_text, (x, y))

# our roll will display message with our roll converted to text form, alongside
def before_roll():
    blank_popup = pygame.image.load('empty_popup.png')
    basic.screen.blit(blank_popup,(0,0))
    produce_large_text("Druk op 'Rol' om te dobbelen", 505,280)
    produce_small_text("Type vraag", 615,152)
    basic.button("roll", 372,357,560,83,(139,131,134),(75,75,75), rollfunc)

#function to make the dice roll        
def rollfunc(): 
    global FIRST_DICE, already_rolled
    FIRST_DICE = roll_a_dice()
    roll_occur = True
       
#type of question roll function
def typeQroll():
    global already_rolled, roll_occur
    roll_occur = False
    while already_rolled == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                already_rolled = True

        basic.screen.fill(basic.white)
        basic.screen.blit(bg, (0, 0)) 
        before_roll()
        display_first(FIRST_DICE)
        roll_occur = False
        already_rolled = False 
        pygame.display.flip()

 
#catagory selection function
def Select_Catagory():
    global Catergory_selected
    while Catergory_selected == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Catergory_selected = True
        basic.screen.blit(cpup, (0 ,0))
        produce_large_text("Kies een categorie", 555,250)
        produce_small_text("Categorie", 620,152)  
        basic.button("Entertainment", 402,300,180,70, basic.yellow, basic.gold, Entertain_vragen)
        basic.button("Geschiedenis", 730, 300,180,70, basic.d_blue, basic.blue, History_vragen)
        basic.button("Sport", 730,390,180,70, basic.green, basic.lime, Sport_vragen)
        basic.button("Techologie", 402,390,180,70, basic.d_red, basic.red, Tech_vragen)
        pygame.display.flip()

def Sport_vragen():
    Sportvraag.Sport_weergave = False
    while Sportvraag.Sport_gekozen == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Sportvraag.Sport_gekozen = True 
        basic.screen.fill(basic.white)
        basic.screen.blit(bg, (0, 0)) 
        Sportvraag.Sportdisplay()

def Entertain_vragen():
    Entertainmentvraag.Ent_weergave = False
    while Entertainmentvraag.Ent_gekozen == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Entertainmentvraag.Ent_gekozen = True 
        basic.screen.fill(basic.white)
        basic.screen.blit(bg, (0, 0)) 
        Entertainmentvraag.Entdisplay()
        pygame.display.flip()

def History_vragen():
    Historyvraag.hist_weergave = False
    while Historyvraag.hist_gekozen == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Historyvraag.hist_gekozen = True 
        basic.screen.fill(basic.white)
        basic.screen.blit(bg, (0, 0)) 
        Historyvraag.histdisplay()
        pygame.display.flip()

def Tech_vragen():
    Techonology.tech_weergave = False
    while Techonology.tech_gekozen == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Techonology.tech_gekozen = True 
        basic.screen.fill(basic.white)
        basic.screen.blit(bg, (0, 0)) 
        Techonology.techdisplay()
        pygame.display.flip()