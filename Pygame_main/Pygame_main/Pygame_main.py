import pygame,sys, math, time, random, basic, Category

pygame.init()
basic.screen

# To quitgame 
def quitgame():
    pygame.quit()
    quit()

#main menu what players see 
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                Intro = False

        bg = pygame.image.load("euromast_wallpaper_v2.jpg")   
        basic.screen.fill(basic.white)
        basic.screen.blit(bg, (0, 0)) 
        largeText = pygame.font.SysFont("calibri",115)
        basic.button("Play",1050,150,150,50,basic.d_blue,(140,140,140),Category.typeQroll)
        basic.button("Instructie",1050,250,150,50,basic.d_blue,(140,140,140),instructies)
        basic.button("High Score",1050,350,150,50,basic.d_blue,(140,140,140),None)
        basic.button("Quit",1050,450,150,50,basic.d_blue,(140,140,140),quitgame)
        pygame.display.update()
        basic.clock.tick(15)

#insturction page
def instructies():
    pygame.display.set_caption("Instruction Screen")
    done = False
    display_instructions = True
    instruction_page = 1

    # LOOP INSTRUCTIEPAGINA
    while not done and display_instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT]:
                instruction_page += 1
                if instruction_page == 4:
                    instruction_page = 1
            elif key[pygame.K_LEFT]:
                instruction_page -= 1
                if instruction_page == 0:
                    instruction_page = 3

        if instruction_page == 1:
            # Draw instructions, page 1
            instruc1 = pygame.image.load("instructiepagina1.jpg")
            instruc1 = pygame.transform.scale(instruc1, (basic.size))
            basic.screen.blit(instruc1,(0,0))

        if instruction_page == 2:
            # Draw instructions, page 1
            instruc2 = pygame.image.load("instructiepagina2.jpg")
            instruc2 = pygame.transform.scale(instruc2, (basic.size)) 
            basic.screen.blit(instruc2,(0,0))

        if instruction_page == 3:
            # Draw instructions, page 1
            instruc3 = pygame.image.load("instructiepagina3.jpg")
            instruc3 = pygame.transform.scale(instruc3, (basic.size))
            basic.screen.blit(instruc3,(0,0))        

        basic.button("<",940,40,50,50,basic.d_blue,(80,80,80),None)
        basic.button(">",1170,40,50,50,basic.d_blue,(80,80,80), None)
        basic.button("Back To menu",1000,40,160,50,basic.d_blue,(80,80,80),game_intro)
        pygame.display.update()
     
game_intro()
pygame.quit()
quit()