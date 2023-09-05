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

#Objects
stone=scale(pygame.image.load("bg/stone.png"),(80,80))
mr1=scale(pygame.image.load("bg/mr1.png"),(70,70))
mr2=scale(pygame.image.load("bg/mr2.png"),(70,70))


#Background Assets
bg=scale(pygame.image.load("bg/img.png"),(720,520))
bg2=pygame.image.load("bg/img2.png")
bg3=pygame.image.load("bg/img4.png")
bg5=pygame.image.load("bg/img5.png")
bg6=pygame.image.load("bg/img6.png")
bg7=pygame.image.load("bg/img7.png")
bb=pygame.image.load("bg/bb.png")
ov=scale(pygame.image.load("bg/ov.png"),(720,520))
overbg=scale(pygame.image.load("bg/pause.png"),(720,520))
tile=pygame.image.load("bg/img10.png")
tile2=pygame.image.load("bg/img10.png")

#overbg=pygame.image.load("bg/over.png")
wbg=scale(pygame.image.load("bg/wbg.png"),(720,520))
#Team Members
myfont = pygame.font.SysFont("cambria", 6)
m1=scale(pygame.image.load("bg/m1.png"),(50,50))
m1n=myfont.render("Devendra Lodhi",1,(0,0,0))
m2=scale(pygame.image.load("bg/m2.png"),(50,50))
m2n=myfont.render("Harsh Yadav",1,(0,0,0))
m3=scale(pygame.image.load("bg/m3.png"),(50,50))
m3n=myfont.render("Pradeep Rawat",1,(0,0,0))
m4=scale(pygame.image.load("bg/m4.png"),(50,50))
m4n=myfont.render("Mayank Sharma",1,(0,0,0))
m5=scale(pygame.image.load("bg/m5.png"),(50,50))
m5n=myfont.render("Ashish Lodhi",1,(0,0,0))
#Setup Display Resolution(width,Height)
surface = pygame.display.set_mode((720, 520))

#Setup Fonts Style and Colors
font = pygame.font.SysFont(None, 35)
myfont = pygame.font.SysFont("cambria", 10)
label = myfont.render("Loading...", 1, (255, 255, 255))
Load=myfont.render("Loading...",1,(0,255,0))
clock = pygame.time.Clock()

#sprite Animation List
dino_sprite=[dr1,dr2,dr3,dr4,dr5,dr6,dr7,dr8]
dino_idle=[idle1,idle2,idle3,idle4,idle5,idle6,idle7,idle8,idle9,idle10]
dino_walk=[walk1,walk2,walk3,walk4,walk5,walk6,walk7,walk8,walk9,walk10]
dino_dead=[dead1,dead2,dead3,dead4,dead5,dead6,dead7,dead8]
dino_jump=[jump1,jump2,jump3,jump4,jump5,jump6,jump7,jump8,jump9,jump10]
#Important Variables
value=0

#Grass and Trees
g1=scale(pygame.image.load("tiles/png/Object/bush1.png"),(70,50))
g2=scale(pygame.image.load("tiles/png/Object/bush2.png"),(70,50))
g3=scale(pygame.image.load("tiles/png/Object/bush3.png"),(70,50))
g4=scale(pygame.image.load("tiles/png/Object/bush4.png"),(70,50))
tree1=scale(pygame.image.load("tiles/png/Object/Tree_1.png"),(100,100))
tree2=scale(pygame.image.load("tiles/png/Object/Tree_2.png"),(300,300))
tree3=scale(pygame.image.load("tiles/png/Object/Tree_3.png"),(300,300))

value=0

#Score Handling
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    surface.blit(screen_text, [x,y])
with open("hiscore.txt", "r") as f:
    hiscore = f.read()
f = open("hiscore.txt", "r")

#LoadingScreen
def loading():
    maxwidth=5
    l=0
    value=0
    while True:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
        # Framelimiter
        if maxwidth < 224:
            maxwidth = maxwidth + 2
        else:                        
            welcome()
        l+=1
        if l==2:
            l=0
            value+=1
        if value >= len(dino_walk):
            value=0  
        dinowalk=dino_walk[value]
        surface.fill((150, 150, 0))
        surface.blit(label, (100, 325))
        surface.blit(bg3,(0,0))
        surface.blit(bb,(0,0))
        surface.blit(dinowalk,(310,192)) 
        surface.blit(Load,(240,425))
        pygame.draw.rect(surface, (0,250,0), pygame.Rect(240,440,230,10), 1)
        pygame.draw.rect(surface, (255,210,0), pygame.Rect(242,442,maxwidth,6))
        pygame.display.flip()

#WelcomeScreen
def welcome():
    maxwidth=5
    while True:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
        maxwidth+=5
        if maxwidth==500:
            homescreen()
        # Framelimiter
        surface.fill((150, 150, 0))
        surface.blit(wbg,(0,0))
        surface.blit(m1,(160,400))
        surface.blit(m2,(240,400))
        surface.blit(m3,(320,400))
        surface.blit(m4,(400,400))
        surface.blit(m5,(480,400))
        surface.blit(m1n,(160,455))
        surface.blit(m2n,(240,455))
        surface.blit(m3n,(320,455))
        surface.blit(m4n,(400,455))
        surface.blit(m5n,(480,455))
        pygame.display.flip()
        
#Home Screen
def homescreen():
    maxwidth=5
    while True:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
        maxwidth+=5
        if maxwidth==500:
            gameloop()
        # Framelimiter
        surface.fill((150, 150, 0))
        surface.blit(wbg,(0,0))
        pygame.display.flip()
    
#Main Game Screen
def gameloop():
    maxwidth=5
    value=0
    l=0
    jj=0
    jj2=0
    ss=0
    gg=0
    over=0
    mr1x=1200
    mr2x=2000
    #Dino Cordinates
    dinox=100
    dinoy=311
    #Background Cordinates
    bgx=0
    bgy=0
    bgx2=720
    bgy2=0
    #Game Pause System
    pause=0
    gover=0
    #Tiles Cordinates
    tilex=0
    tiley=440
    tile2x=720
    tile2y=440
    #trees Cordinates
    #Tree X Cordinates
    tree1x=1000
    tree2x=2200
    tree3x=3500
    #Tree Y cordinates
    tree1y=340
    tree2y=150
    tree3y=150
    #Grass Cordinates
    #Grass X cordinates
    g1x=1200
    g2x=1700
    g3x=500
    g4x=2000
    #Grass Y cordinates
    g1y=410
    g2y=400
    g3y=410
    g4y=400
    score=0
    red=(255,0,0)
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
    f = open("hiscore.txt", "r")
    #Game Loop Start
    while True:
        
        if score>int(hiscore):
            hiscore = score
        with open("hiscore.txt", "w") as f:
            f.write(str(hiscore))
        l+=1
        #INPUT EVENTS
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
            if over ==0:
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_LEFT or ev.key == pygame.K_UP:
                    
                        gg=1
            if ev.type == pygame.KEYDOWN:
                if gover<1:
                    if ev.key == pygame.K_p:
                 
                        pause+=1
                        gover=0
                        if pause >= 2:
                            pause=0
                if pause<1:
                    if ev.key==pygame.K_o:
                        gover+=1
                        pause=-5
                        if gover>=2:
                            gover=0
                            gameloop()
        if maxwidth==500:
            homescreen()
        if over==0:
            if dinoy<=180:                
                
                
                ss=1            
            if dinoy>=180:           
                if gg == 1:
                    dinoy-=5
            
                    if dinoy<=180:                
                
                
                        
                        gg=0
            if ss==1:
                dinoy+=5
            
                if dinoy>=309:
                    gg=0
                    dinoy=309
                    ss=0
        if pause==0:
            
            if l>=4:
                l=0
                value+=1
            if value >= len(dino_sprite):
                value=0  
            dinorun=dino_sprite[value]
            #Elements Animations
            bgx-=1
            bgx2-=1
            tilex-=6
            tile2x-=6
            tree1x-=6
            tree2x-=6
            tree3x-=6
            g1x-=6
            g2x-=6
            g3x-=6
            g4x-=6
            mr1x-=6
            mr2x-=6
            if mr1x<0:
                jj2+=1
                if jj2==1:
                    score+=10
            if mr2x<0:
                jj+=1
                if jj==1:
                    score+=10
            #Masgroom Loop
            if mr1x<=-400:
                mr1x=random.randint(720,5000)
                jj2=0
            if mr2x<=-400:
                mr2x=random.randint(720,5000)
                jj=0
            #background Loop
            if bgx<=-720:
                bgx=720
            if bgx2<=-720:
                bgx2=720
            #Tiles Loop
            if tilex<=-720:
                tilex=720
            if tile2x<=-720:
                tile2x=720
            #Trees Loop
            if tree1x<=-700:
                tree1x=random.randint(720,5000)
            if tree2x<=-700:
                tree2x=random.randint(720,5000)     
            if tree3x<=-700:
                tree3x=random.randint(700,5000)
            #Grass Loops
            if g1x<=-700:
                g1x=random.randint(720,5000)
            if g2x<=-700:
                g2x=random.randint(720,5000)     
            if g3x<=-700:
                g3x=random.randint(720,5000)
            if g4x<=-700:
                g4x=random.randint(720,5000)
        # Framelimiter
        if dinoy==311:
            if mr1x<=90:
                if mr1x>=40:
                    gover+=1
                    pause=-5
            elif mr2x<=90:
                if mr2x>=40:
                    gover+=1
                    pause=-5
                
                   
        surface.fill((150, 150, 0))
        surface.blit(bg,(bgx,bgy))
        surface.blit(bg,(bgx2,bgy2))
        surface.blit(tree2,(tree2x,tree2y))
        surface.blit(tree3,(tree3x,tree3y))
        surface.blit(tile,(tilex,tiley))
        surface.blit(tile2,(tile2x,tile2y))      
        surface.blit(g1,(g1x,g1y))
        surface.blit(g2,(g2x,g2y))
        surface.blit(g3,(g3x,g3y))
        surface.blit(g4,(g4x,g4y))
        surface.blit(mr1,(mr1x,390))
        surface.blit(mr2,(mr2x,390))
        text_screen("High Score: "+str(hiscore),(0,100,200),5,5)
        text_screen("Score: " + str(score), red, 5, 30)
        if pause<2:
            surface.blit(dinorun,(dinox,dinoy))
            
        if pause>=1:
            surface.blit(overbg,(0,0))
        #Game Over Algorithm
        if gover>=1:
            
            surface.blit(ov,(0,0))
            text_screen(str(hiscore),(0,200,5),328,235)
            text_screen(str(score),(0,200,200),340,160)
        pygame.display.flip()   

gameloop()