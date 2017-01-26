from pygame.locals import *
import pygame, string
import basic

# DE TEXT WORD NIET HERKEND :( morgen verder

class Woord:

    def __init__(self):
        woord = []
        for key in x:
            exec('self.'+key[0]+' = '+key[1])
            woord = woord + (key[0])

class Input:
    def __init__(self, x, y, color):
        #positie, kleur en fonts bepalen
        self.x = x; self.y = y
        self.font = basic.antwoordvak_font
        self.color = color
        # de user krijgt te zien waar het antwoord komt
        self.antwoordstring = 'Antwoord: '
        # De value staat voor wat je in hebt getypt
        self.value = ''


    def draw(self, scherm):
        # zorgen dat tekst op het scherm komt
        text = self.font.render(self.antwoordstring+self.value, 0, self.color)
        basic.screen.blit(text, (self.x, self.y))

    def update(self, events):
        # Hiermee check ik de keyboard input van de speler en sla deze op in de value van de class
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE: self.value = self.value[:-1]
                elif event.key == K_SPACE: self.value += ' '
                elif event.key == K_a: self.value += 'A'
                elif event.key == K_b: self.value += 'B'
                elif event.key == K_c: self.value += 'C'
                elif event.key == K_d: self.value += 'D'
                elif event.key == K_e: self.value += 'E'
                elif event.key == K_f: self.value += 'F'
                elif event.key == K_g: self.value += 'G'
                elif event.key == K_h: self.value += 'H'
                elif event.key == K_i: self.value += 'I'
                elif event.key == K_j: self.value += 'J'
                elif event.key == K_k: self.value += 'K'
                elif event.key == K_l: self.value += 'L'
                elif event.key == K_m: self.value += 'M'
                elif event.key == K_n: self.value += 'N'
                elif event.key == K_o: self.value += 'O'
                elif event.key == K_p: self.value += 'P'
                elif event.key == K_q: self.value += 'Q'
                elif event.key == K_r: self.value += 'R'
                elif event.key == K_s: self.value += 'S'
                elif event.key == K_t: self.value += 'T'
                elif event.key == K_u: self.value += 'U'
                elif event.key == K_v: self.value += 'V'
                elif event.key == K_w: self.value += 'W'
                elif event.key == K_x: self.value += 'X'
                elif event.key == K_y: self.value += 'Y'
                elif event.key == K_z: self.value += 'Z'
                elif event.key == K_0: self.value += '0'
                elif event.key == K_1: self.value += '1'
                elif event.key == K_2: self.value += '2'
                elif event.key == K_3: self.value += '3'
                elif event.key == K_4: self.value += '4'
                elif event.key == K_5: self.value += '5'
                elif event.key == K_6: self.value += '6'
                elif event.key == K_7: self.value += '7'
                elif event.key == K_8: self.value += '8'
                elif event.key == K_9: self.value += '9'
                elif event.key == K_RETURN: return

# self.value += chr(even.key)
