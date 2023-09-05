#PROJECT 1.0
#importing Modules/Libraries
import sys
import pygame
import random
from pygame.locals import *
pygame.init()

#Assets
#Run 1
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

#Idle 2
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

#Jump 3
jump1=scale(pygame.image.load("asset/png/jump1.png"),(150,150))
jump2=scale(pygame.image.load("asset/png/jump2.png"),(150,150))
jump3=scale(pygame.image.load("asset/png/jump3.png"),(150,150))
jump4=scale(pygame.image.load("asset/png/jump4.png"),(150,150))
jump5=scale(pygame.image.load("asset/png/jump5.png"),(150,150))
jump6=scale(pygame.image.load("asset/png/jump6.png"),(150,150))
jump7=scale(pygame.image.load("asset/png/jump7.png"),(150,150))
jump8=scale(pygame.image.load("asset/png/jump8.png"),(150,150))
jump9=scale(pygame.image.load("asset/png/jump9.png"),(150,150))
jump10=scale(pygame.image.load("asset/png/jump10.png"),(150,150))
jump11=scale(pygame.image.load("asset/png/jump11.png"),(150,150))
jump12=scale(pygame.image.load("asset/png/jump12.png"),(150,150))
#Walk 4
walk1=scale(pygame.image.load("asset/png/walk1.png"),(150,150))
walk2=scale(pygame.image.load("asset/png/walk2.png"),(150,150))
walk3=scale(pygame.image.load("asset/png/walk3.png"),(150,150))
walk4=scale(pygame.image.load("asset/png/walk4.png"),(150,150))
walk5=scale(pygame.image.load("asset/png/walk5.png"),(150,150))
walk6=scale(pygame.image.load("asset/png/walk6.png"),(150,150))
walk7=scale(pygame.image.load("asset/png/walk7.png"),(150,150))
walk8=scale(pygame.image.load("asset/png/walk8.png"),(150,150))
walk9=scale(pygame.image.load("asset/png/walk9.png"),(150,150))
walk10=scale(pygame.image.load("asset/png/walk10.png"),(150,150))

#Dead 5
dead1=scale(pygame.image.load("asset/png/dead1.png"),(150,150))
dead2=scale(pygame.image.load("asset/png/dead2.png"),(150,150))
dead3=scale(pygame.image.load("asset/png/dead3.png"),(150,150))
dead4=scale(pygame.image.load("asset/png/dead4.png"),(150,150))
dead5=scale(pygame.image.load("asset/png/dead5.png"),(150,150))
dead6=scale(pygame.image.load("asset/png/dead6.png"),(150,150))
dead7=scale(pygame.image.load("asset/png/dead7.png"),(150,150))
dead8=scale(pygame.image.load("asset/png/dead8.png"),(150,150))
idle9=scale(pygame.image.load("asset/png/idle9.png"),(150,150))
idle10=scale(pygame.image.load("asset/png/idle10.png"),(150,150))

#Tiles
t1=scale(pygame.image.load("tiles/png/Tiles/1.png"),(60,60))
t2=scale(pygame.image.load("tiles/png/Tiles/2.png"),(60,60))
t3=scale(pygame.image.load("tiles/png/Tiles/3.png"),(60,60))

#Objects
stone=scale(pygame.image.load("bg/stone.png"),(80,80))
mr1=scale(pygame.image.load("bg/mr1.png"),(70,70))
mr2=scale(pygame.image.load("bg/mr2.png"),(70,70))


#Background Assets
bg=pygame.image.load("bg/img.png")
bg2=pygame.image.load("bg/img2.png")
bg3=pygame.image.load("bg/img4.png")
bg5=pygame.image.load("bg/img5.png")
bg6=pygame.image.load("bg/img6.png")
bg7=pygame.image.load("bg/img7.png")

#Setup Display Resolution(width,Height)
surface = pygame.display.set_mode((720, 520))

#Setup Fonts Style and Colors
myfont = pygame.font.SysFont("cambria", 20)
label = myfont.render("Loading...", 1, (255, 255, 255))
label2 = myfont.render("WelcomeScreen", 1, (255, 255, 255))
label3 = myfont.render("High Score :", 1, (255, 100    ,0))
label4 = myfont.render("GameOverScreen", 1, (255, 255, 255))
label5 = myfont.render("AboutScreen", 1, (255, 255, 255))
Load=myfont.render("Loading...",1,(0,255,0))
clock = pygame.time.Clock()

#sprite Animation List
dino_sprite=[dr1,dr2,dr3,dr4,dr5,dr6,dr7,dr8]
dino_idle=[idle1,idle2,idle3,idle4,idle5,idle6,idle7,idle8,idle9,idle10]
dino_walk=[walk1,walk2,walk3,walk4,walk5,walk6,walk7,walk8,walk9,walk10]
dino_dead=[dead1,dead2,dead3,dead4,dead5,dead6,dead7,dead8]
dino_jump=[jump1,jump2,jump3,jump4,jump5,jump6,jump7,jump8,jump9,jump10]
#values
value=0

#Loading Screen Function
def WelcomeScreen():
    x=2
    bgwx=0
    bgwx2=720
    bg2=pygame.image.load("bg/img2.png")
    
    scale=pygame.transform.scale
    bgw=scale(bg2,(720,520))
    while True:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
        # Framelimiter
        bgwx-=1
        bgwx2-=1
        if bgwx==-720:
            bgwx=720
        if bgwx2==-720:
            bgwx2=720
        
        surface.fill((255, 0, 0))
        surface.blit(bgw,(bgwx,0))
        surface.blit(bgw,(bgwx2,0))
        pygame.display.flip()       

def LoadingScreen():
    maxwidth=5
    while True:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
        # Framelimiter
        if maxwidth < 224:
            maxwidth = maxwidth + 10
        else:                        
            WelcomeScreen()
        surface.fill((150, 150, 0))
        surface.blit(label, (100, 225))
        surface.blit(bg3,(0,0))
        surface.blit(bg6,(0,0))
        surface.blit(bg7,(0,0))
        surface.blit(Load,(300,315))
        pygame.draw.rect(surface, (0,250,0), pygame.Rect(230,340,230,10), 1)
        pygame.draw.rect(surface, (255,210,0), pygame.Rect(232,342,maxwidth,6))
        pygame.display.flip()    


#MainLoop
def MainGameScreen():
    bgx=0
    bgy=0
    bgx2=720
    bgy2=0
    bg=pygame.image.load("bg/img.png")
    bg=pygame.image.load("bg/img.png")
    t1=pygame.image.load("bg/img10.png")
    t2=pygame
    
    .image.load("bg/img11.png")
    bg=pygame.image.load("bg/img.png")
    dino=pygame.image.load("asset/png/idle1.png")
    bg=pygame.transform.scale(bg, (720,520))
    
    scale=pygame.transform.scale
    value=0
    l=0
    tx2=720
    ty2=440
    tx=0
    ty=440
    #-220 to -360
    t2x=720
    t2y=440
    k=0
    dinoy=309
    dinox=90
    over=1
    jum=0
    jum2=0
    mrx=720
    mry=380
    mr2x=1000
    mr2y=380
    stonex=1800
    
    stoney=380
    ss=0
    gg=0
    dino=scale(dino,(150,150))    
    while True:        
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
            if over ==1:
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_LEFT or ev.key == pygame.K_UP:
                    
                        gg=1
        if over==1:            
            if dinoy>=180:           
                if gg == 1:
                    dinoy-=5
            
                    if dinoy<=180:                
                
                
                        ss=1
                        gg=0
            if ss==1:
                dinoy+=5
            
                if dinoy>=309:
                    gg=0
                    dino=309
                    ss=0
              
        # Framelimiter
        if over == 1:      
           bgx-=1/2
           bgx2-=1/2
           l+=1
           tx-=4
           tx2-=4
           k+=1
           mrx-=4
           mr2x-=4
           stonex-=4
           
        if t2x<=-220:
            jum=2
            if t2y>=-360:
                over=0
                dinoy+=2
                if dinoy>=420:
                     LoadingScreen()
        if mrx<=-800:
            ran=random.randint(2020,5000)
            mrx+=ran
        if stonex<=-800:
            ran3=random.randint(2000,5000)
            stonex+=ran3
        if stonex<=(mrx) and stonex>=(mrx-700) or mrx<=(stonex-700) and mrx>=(stonex):
            ran3=random.randint(2000,5000)
        if stonex<=(mr2x+700) and stonex>=(mr2x) or mr2x<=(stonex-700) and mr2x>=(stonex):
            ran3=random.randint(2000,5000)
        if mr2x<=-800:
            ran2=random.randint(2000,5000)
            mr2x+=ran2
        if mrx>=(mr2x-600) and mrx<=(mr2x+600) or mr2x>=(mrx-600) and mr2x<=(mrx+600):
            mrx=800
            mr2x=1500
        if tx <=-720:
            tx=720
        if tx2 <=-720:
            tx2=720      
        if bgx==-720:
            bgx=720
        if bgx2==-720:
            bgx2=720
        if jum==0:
            if True:
                if l==5:
                    l=0
                    value+=1
            if value >= len(dino_sprite):
                value=0  
        dinorun=dino_sprite[value]
        dinojump=dino_jump[value]
        dinodead=dino_dead[value]   
        surface.fill((205, 0, 250))
        surface.blit(bg, (bgx, bgy))
        surface.blit(bg,(bgx2,bgy2))      
        surface.blit(t1,(tx,ty))
        surface.blit(mr2,(mr2x,mr2y))
        surface.blit(t1,(tx2,ty2))
        surface.blit(mr1,(mrx,mry))
        surface.blit(mr2,(mr2x,mr2y))
        surface.blit(stone,(stonex,stoney))
        if dinoy==309:
            if mrx<=90:
                if mrx>=40:
                    GameOver()
            elif mr2x<=90:
                if mr2x>=40:
                    GameOver()
                
            elif stonex<=90:
                if stonex>=40:
                    GameOver()
        if jum==2:
            if True:
                if l==4:
                    l=0
                    value+=1
            if value >= len(dino_dead):
                value=0
                if value==0:
                    dinoy=309
                    jum=0
                    
            surface.blit(dinodead,(dinox,dinoy))
            
        if jum==0:
            surface.blit(dinorun,(dinox,dinoy))
        if jum==1:
            if True:
                if l==4:
                    l=0
                    value+=1
            if value >= len(dino_jump):
                value=0
                if value==0:
                    dinoy=309  
            surface.blit(dinojump,(dinox,dinoy))
        
            
        surface.blit(label3,(5,5))
        
        pygame.display.flip()






def HomeScreen():    
    bg1=pygame.image.load("bg/img.png")
    button=pygame.image.load("bg/button.png")
    scale=pygame.transform.scale
    bub=scale(pygame.image.load("bg/bub.png"),(180,180))
    button=scale(button,(290,290))
    bg1=scale(bg1,(720,520))
    l=0
    value=0
    while True:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_LEFT or ev.key == pygame.K_RIGHT:
                    MainGameScreen()
        l+=1
        if True:
            if l==10:
                l=0
                value+=1
        if value >= len(dino_idle):
            value=0  
        dinoidle=dino_idle[value]
          
        # Framelimiter                
        surface.fill((255, 0, 0))
        surface.blit(bg1,(0,0))
        surface.blit(dinoidle,(310,90))
        surface.blit(bub,(270,70))
        surface.blit(button,(220,230))
        pygame.display.flip() 
def GameOver():
    WelcomeScreen()
MainGameScreen()