import pygame , time, random, basic, vraagfunc
    
pygame.init()

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
    typeQ = ["open"] * 20 + ["meerkeuze"] * 80
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
    global already_rolled
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
        pygame.display.flip()

 
#catagory selection function
def Select_Catagory():
    global Catergory_selected
    while Catergory_selected == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Catergory_selected = True

        basic.screen.blit(cpup, (0 ,0))
        produce_large_text("Kies een categorie", 555,250)
        produce_small_text("Categorie", 620,152) 
        Ebutton = basic.button("Entertainment", 402,300,180,70, basic.yellow, basic.gold, None)
        Gbutton = basic.button("Geschiedenis", 730, 300,180,70, basic.d_blue, basic.blue, Histo_vragen)
        Sbutton =basic.button("Sport", 730,390,180,70, basic.green, basic.lime, Sport_vragen)
        Tbutton = basic.button("Techologie", 402,390,180,70, basic.d_red, basic.red, None)
        
        pygame.display.flip()

def Sport_vragen():
    gegeven_vraag = False
    while gegeven_vraag == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               gegeven_vraag = True
        vraagfunc.s_vraag()
        Sbutton = basic.button2("Sport", 730,600,180,70, basic.green, basic.lime, Sport_vragen)
        Gbutton = basic.button2("Geschiedenis", 402, 600,180,70, basic.d_blue, basic.blue, Histo_vragen)
        Tbutton = basic.button2("Techologie", 102,390,180,70, basic.d_red, basic.red, typeQroll)
        pygame.display.flip()


def Histo_vragen():
    gegeven_vraag = False
    while gegeven_vraag == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               gegeven_vraag = True
        vraagfunc.h_vraag()
        Sbutton = basic.button2("Sport", 730,600,180,70, basic.green, basic.lime, Sport_vragen)
        Gbutton = basic.button2("Geschiedenis", 402, 600,180,70, basic.d_blue, basic.blue, Histo_vragen)
        Tbutton = basic.button2("Techologie", 102,390,180,70, basic.d_red, basic.red, before_roll)
        pygame.display.flip()
        
def vraagbeantwoord():
    sportvragen.remove(randomvraag)      