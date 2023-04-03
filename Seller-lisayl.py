#Ander Varuskin IS22

import pygame #Impordib pygame

pygame.init() #Käivitab pygame


Screen = pygame.display.set_mode([640,480]) #Ekraani loomine
pygame.display.set_caption("Ander Varuskin - YL2") #Ekraanile nime andmine
Screen.fill([117, 172, 235]) #Täidab ekraani sisestatud värviga.


bg = pygame.image.load("taust.jpg") #Tausta lisamine
Screen.blit(bg,[0,0]) #Pildi asukoht

seller = pygame.image.load("seller.png") #Müüja lisamine ekraanile
seller = pygame.transform.scale(seller, [250,300]) #Müüja laiuse ja pikkuse muutmine
Screen.blit(seller, [10,120]) #Selleri asukohta  paigaldamine

jutumull = pygame.image.load("jutumull.png") #Jutumulli lisamine ekraanile
jutumull = pygame.transform.scale(jutumull, [200,150]) #jutumulli laiuse ja pikkuse muutmine
Screen.blit(jutumull, [140,80]) #jutumulli asukoha paigaldamine

font = pygame.font.Font(pygame.font.match_font("arial"),20)
text = font.render("Tervist, olen Ander", True, [255,255,255])

text_width = text.get_rect().width #muutuja (tekstikasti suurus)
text_height = text.get_rect().height #muutuja
Screen.blit(text, [250-text_width/2,120-text_height/2]) #teksti paigutamine ekraanil

logo = pygame.image.load("TULEVIK 2050.png") #sisestab ekraanile logo
logo = pygame.transform.scale(logo, [350,65]) #määrab logo pikkuse ja laiuse
Screen.blit(logo, [0,2]) #määrab logo asukoha

kook = pygame.image.load("kook.png") #lisab koogi
kook = pygame.transform.scale(kook, [100,60]) #määrab koogi pikkuse ja laiuse
Screen.blit(kook, [320,230]) #määrab koogi asukoha

mook = pygame.image.load("M66k.png") #lisab mõõga
mook = pygame.transform.scale(mook, [115,200]) #määrab mõõga pikkuse ja laiuse
Screen.blit(mook, [530,130]) #määrab mõõga asukoha


pygame.display.flip() #uuendab ekraani

#Loopi loomine
running = True


while running:


    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False