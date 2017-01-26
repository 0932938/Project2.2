import pygame, time, random, basic
from array import array

pygame.init()
basic.screen
basic.clock

#images
#dices
dobbelImg1 = pygame.image.load('DObelsteen 1.png')
dobbelImg2 = pygame.image.load('DObelsteen 2.png')
dobbelImg3 = pygame.image.load('DObelsteen 3.png')
dobbelImg4 = pygame.image.load('DObelsteen 4.png')
dobbelImg5 = pygame.image.load('DObelsteen 5.png')
dobbelImg6 = pygame.image.load('DObelsteen 6.png')

#resize dice
dobbelNiks = pygame.transform.scale(dobbelNiks, Dice_resize)
dobbelImg1 = pygame.transform.scale(dobbelImg1, Dice_resize)
dobbelImg2 = pygame.transform.scale(dobbelImg2, Dice_resize)
dobbelImg3 = pygame.transform.scale(dobbelImg3, Dice_resize)
dobbelImg4 = pygame.transform.scale(dobbelImg4, Dice_resize)
dobbelImg5 = pygame.transform.scale(dobbelImg5, Dice_resize)
dobbelImg6 = pygame.transform.scale(dobbelImg6, Dice_resize)

#medals
Medal_speler_1 = pygame.image.load('Medal Speler 1.png')
Medal_speler_2 = pygame.image.load('Medal Speler 2.png')
Medal_speler_3 = pygame.image.load('Medal Speler 3.png')
Medal_speler_4 = pygame.image.load('Medal Speler 4.png')

MedalGold_speler_1 = pygame.image.load('Medal First Speler 1.png')
MedalGold_speler_2 = pygame.image.load('Medal First Speler 2.png')
MedalGold_speler_3 = pygame.image.load('Medal First Speler 3.png')
MedalGold_speler_4 = pygame.image.load('Medal First Speler 4.png')

#resize medals
Medal_speler_1 = pygame.transform.scale(Medal_speler_1, Medal_resize)
Medal_speler_2 = pygame.transform.scale(Medal_speler_2, Medal_resize)
Medal_speler_3 = pygame.transform.scale(Medal_speler_3, Medal_resize)
Medal_speler_4 = pygame.transform.scale(Medal_speler_4, Medal_resize)

MedalGold_speler_1 = pygame.transform.scale(MedalGold_speler_1, Medal_resize)
MedalGold_speler_2 = pygame.transform.scale(MedalGold_speler_2, Medal_resize)
MedalGold_speler_3 = pygame.transform.scale(MedalGold_speler_3, Medal_resize)
MedalGold_speler_4 = pygame.transform.scale(MedalGold_speler_4, Medal_resize)

#players
playerturn = ['1','2','3','4','5','6']