#Sprite Animation Sheet
#Pygame

#importing image assets

#idle

#running

#dead

#jump

#Walk

#importing Modules/Libraries
import sys
import pygame
from pygame.locals import *
pygame.init()
#DinoRunning Assets
scale=pygame.transform.scale
dr1=scale(pygame.image.load("asset/png/run1.png"),(150,150))
dr2=scale(pygame.image.load("asset/png/run2.png"),(150,150))
dr3=scale(pygame.image.load("asset/png/run3.png"),(150,150))
dr4=scale(pygame.image.load("asset/png/run4.png"),(150,150))
dr5=scale(pygame.image.load("asset/png/run5.png"),(150,150))
dr6=scale(pygame.image.load("asset/png/run6.png"),(150,150))
dr7=scale(pygame.image.load("asset/png/run7.png"),(150,150))
dr8=scale(pygame.image.load("asset/png/run8.png"),(150,150))
dr14=scale(pygame.image.load("asset/png/run2.png"),(150,150))
dr13=scale(pygame.image.load("asset/png/run3.png"),(150,150))
dr12=scale(pygame.image.load("asset/png/run4.png"),(150,150))
dr11=scale(pygame.image.load("asset/png/run5.png"),(150,150))
dr10=scale(pygame.image.load("asset/png/run6.png"),(150,150))
dr9=scale(pygame.image.load("asset/png/run7.png"),(150,150))

#idle
idle8=scale(pygame.image.load("asset/png/idle8.png"),(150,150))
idle7=scale(pygame.image.load("asset/png/idle7.png"),(150,150))
idle6=scale(pygame.image.load("asset/png/idle6.png"),(150,150))
idle5=scale(pygame.image.load("asset/png/idle5.png"),(150,150))
idle4=scale(pygame.image.load("asset/png/idle4.png"),(150,150))
idle3=scale(pygame.image.load("asset/png/idle3.png"),(150,150))
idle2=scale(pygame.image.load("asset/png/idle2.png"),(150,150))
idle1=scale(pygame.image.load("asset/png/idle1.png"),(150,150))
idle9=scale(pygame.image.load("asset/png/idle9.png"),(150,150))
idle10=scale(pygame.image.load("asset/png/idle10.png"),(150,150))
#Background Assets
bg=pygame.image.load("bg/img.png")
bg2=pygame.image.load("bg/img2.png")
bg3=pygame.image.load("bg/img4.png")
bg5=pygame.image.load("bg/img5.png")
bg6=pygame.image.load("bg/img6.png")
bg7=pygame.image.load("bg/img7.png")
dino_idle=[idle1,idle2,idle3,idle4,idle5,idle6,idle7,idle8,idle9,idle10]
surface = pygame.display.set_mode((720, 520))

class ani():
    def idle(x,y):
        bg1=pygame.image.load("bg/img.png")
        button=pygame.image.load("bg/button.png")
        scale=pygame.transform.scale
        bub=scale(pygame.image.load("bg/bub.png"),(180,180))
        button=scale(button,(290,290))
        bg1=scale(bg1,(720,520))
        l=0
        value=0
        while True:
            l+=1
            if True:
                if l==8:
                    l=0
                    value+=1
            if value >= len(dino_idle):
                value=0  
            dinoidle=dino_idle[value]  
            # Framelimiter                
            
            
            surface.blit(dinoidle,(310,90))
            
            pygame.display.flip() 
ani.idle(0,0)