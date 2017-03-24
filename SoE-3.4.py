import pygame, sys
from pygame.locals import *
import random
import time
DIRT = 0
GRASS = 1
TILESIZE = 40
MAPWIDTH = 20
MAPHEIGHT = 15
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
orange = (255,127,0)
resources = [DIRT, GRASS]
textures = {
            DIRT : pygame.image.load('dirt.jpg'),
            GRASS : pygame.image.load('grass.jpg')
           } 
tilemap = [[random.choice(resources) for w in range(MAPWIDTH)]for h in range(MAPHEIGHT)]
pygame.init()
gameDisplay = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
pygame.display.set_caption('Sword of Eternus')
clock = pygame.time.Clock()
heroImg = pygame.image.load('hero.png').convert_alpha()
enemyImg = pygame.image.load('enemy.png').convert_alpha()
bossImg = pygame.image.load('boss.png').convert_alpha()
bkgimg1 = pygame.image.load('Demonland.png')
bkgimg2 = pygame.image.load('heroguy.png')
bkgimg3 = pygame.image.load('bossfight.png')
bkgimg4 = pygame.image.load('gates.jpg')
S1 = pygame.image.load('S1.png')
S2 = pygame.image.load('S2.png')
S3 = pygame.image.load('S3.png')
S4 = pygame.image.load('S4.png')
S5 = pygame.image.load('S5.png')
S6 = pygame.image.load('S6.png')
S7 = pygame.image.load('S7.png')
S8 = pygame.image.load('S8.png')
S9 = pygame.image.load('S9.png')

#################################HEALTH-STATS##########################################################

def hero_health(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Hero: "+str(count),True,white)
    gameDisplay.blit(text,(0,0))

def enemy_health1(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Enemy1: "+str(count),True,white)
    if count>0:
        gameDisplay.blit(text,(0,15))

def enemy_health2(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Enemy2: "+str(count),True,white)
    if count>0:
        gameDisplay.blit(text,(0,30))

def enemy_health3(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Enemy3: "+str(count),True,white)
    if count>0:
        gameDisplay.blit(text,(0,45))

def enemy_health4(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Enemy4: "+str(count),True,white)
    if count>0:
        gameDisplay.blit(text,(0,60))

def enemy_health5(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Enemy5: "+str(count),True,white)
    if count>0:
        gameDisplay.blit(text,(0,75))

def enemy_health6(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Enemy6: "+str(count),True,white)
    if count>0:
        gameDisplay.blit(text,(0,90))

######################################CHAR_FUNCTION_DEFINITION########################################################
        
def enemy1(ex1,ey1,eH1):
    if eH1>0:
        gameDisplay.blit(enemyImg, (ex1*TILESIZE,ey1*TILESIZE))

def enemy2(ex2,ey2,eH2):
    if eH2>0:
        gameDisplay.blit(enemyImg, (ex2*TILESIZE,ey2*TILESIZE))

def enemy3(ex3,ey3,eH3):
    if eH3>0:
        gameDisplay.blit(enemyImg, (ex3*TILESIZE,ey3*TILESIZE))

def enemy4(ex4,ey4,eH4):
    if eH4>0:
        gameDisplay.blit(enemyImg, (ex4*TILESIZE,ey4*TILESIZE))

def enemy5(ex5,ey5,eH5):
    if eH5>0:
        gameDisplay.blit(enemyImg, (ex5*TILESIZE,ey5*TILESIZE))

def enemy6(ex6,ey6,eH6):
    if eH6>0:
        gameDisplay.blit(enemyImg, (ex6*TILESIZE,ey6*TILESIZE))

def boss(bx,by,bH):
    if bH>0:
        gameDisplay.blit(bossImg, (bx*TILESIZE,by*TILESIZE))
        pygame.display.update()
    
def hero(x,y,H):
    gameDisplay.blit(heroImg, (x*TILESIZE, y*TILESIZE))

#######################################FUNCTIONS FOR DISPLAYING TEXT#####################################################


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font(None, 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((MAPWIDTH*TILESIZE/2, MAPHEIGHT*TILESIZE/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    mainGame_loop()

def intro_display(text):
    largeText = pygame.font.Font(None, 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((MAPWIDTH*TILESIZE/2, MAPHEIGHT*TILESIZE/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(6)
    gameDisplay.fill(black)
    

def message_Display(text):
    largeText = pygame.font.Font(None, 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((MAPWIDTH*TILESIZE/2, MAPHEIGHT*TILESIZE/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(6)
    gameDisplay.fill(black)

def message_Display1(text):
    largeText = pygame.font.Font(None, 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((MAPWIDTH*TILESIZE/2, MAPHEIGHT*TILESIZE/2))
    gameDisplay.blit(bkgimg1,(0,0))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(6)
    gameDisplay.fill(black)

def message_Display2(text):
    largeText = pygame.font.Font(None, 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((MAPWIDTH*TILESIZE/2, MAPHEIGHT*TILESIZE/2))
    gameDisplay.blit(bkgimg2,(0,0))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(6)
    gameDisplay.fill(black)

def message_Display3(text):
    largeText = pygame.font.Font(None, 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((MAPWIDTH*TILESIZE/2, MAPHEIGHT*TILESIZE/2))
    gameDisplay.blit(bkgimg3,(0,0))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(6)
    gameDisplay.fill(black)


def message_Display4(text):
    largeText = pygame.font.Font(None, 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((MAPWIDTH*TILESIZE/2, MAPHEIGHT*TILESIZE/2))
    gameDisplay.blit(bkgimg4,(0,0))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(6)
    gameDisplay.fill(black)

def intro_Display(text):
    largeText = pygame.font.Font(None, 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((MAPWIDTH*TILESIZE/2, MAPHEIGHT*TILESIZE/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(black)

#####WON#####
        
def won():
    message_display('You Won')

####DEAD####

def die():
    message_display('You Died')
    mainGame_loop()

#########LOADING SCREEN###################

def intro():
    intro_Display('Initialising Game...')
    intro_Display('Loading.')
    intro_Display('Loading..')
    intro_Display('Loading...')
    intro_Display('Loading....')
    intro_Display('Loading.')
    intro_Display('Loading..')
    intro_Display('Loading...')
    intro_Display('Loading....')
    intro_Display('Loading.')
    intro_Display('Loading..')

#################GAME STORY###################

def story_line():
    message_Display1('A thousand years ago, the land of Almanoc was ruled by cruel demons.')
    message_Display2('One mighty hero, rose up against the demons, fought them, and exiled them back to their own realm.')
    message_Display3('Then, he fought against the evil, Demon King, Xuryx. Their fight lasted for four days.')
    message_Display3('At the end, in one winning stroke, the mighty hero, Eternus, pierced the heart of Xuryx.')
    message_Display3("But as Xuryx was exiled back to his realm, the sword of Eternus, absorbed some of the Demons' magic")
    message_Display4('Eternus, with the help of a sorcerrer, locked the Gates of Darkness, the gateway to the Demon Realm.')
    message_Display('The Sword of Eternus disppeared and became a thing of legend.')
    message_Display('Now the Gates of Darkness is weakening, and Demons are once again running rampant in Almanoc.')
    message_Display('And the Sword of Eternus has appeared once again and waiting to be wielded by the hero of Almanoc.')
    message_Display('You are destined for great things, hero.')
    message_Display('Take the Sword of Eternus and go forth.')
    message_Display('Your destiny awaits you..')

###################GAME INTRO SCREEN#################

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        gameDisplay.blit(S1,(0,0))
        pygame.display.update()
        time.sleep(0.5)
        gameDisplay.blit(S2,(0,0))
        pygame.display.update()
        time.sleep(0.5)
        gameDisplay.blit(S3,(0,0))
        pygame.display.update()
        time.sleep(0.5)
        gameDisplay.blit(S4,(0,0))
        pygame.display.update()
        time.sleep(0.5)
        gameDisplay.blit(S5,(0,0))
        pygame.display.update()
        time.sleep(5)
        gameDisplay.blit(S6,(0,0))
        pygame.display.update()
        time.sleep(0.5)
        gameDisplay.blit(S7,(0,0))
        pygame.display.update()
        time.sleep(0.5)
        gameDisplay.blit(S8,(0,0))
        pygame.display.update()
        time.sleep(0.5)
        gameDisplay.blit(S9,(0,0))
        pygame.display.update()
        time.sleep(0.5)
        intro = False

#####################GAME LOOP########################

def mainGame_loop():

    x = 10
    y = 7
    ex1 = 9
    ey1 = 0
    ex2 = 15
    ey2 = 0
    ex3 = 10
    ey3 = 10
    ex4 = 6
    ey4 = 5
    ex5 = 14
    ey5 = 9
    ex6 = 4
    ey6 = 8
    bx = 10
    by = 10
    eH1 = eH2 = eH3 = eH4 = eH5 = eH6 = 100
    H = 400
    bH = 250

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if (event.key == K_RIGHT) and x < MAPWIDTH - 1:
                    x += 1
                elif (event.key == K_LEFT) and x > 0:
                    x -= 1
                elif (event.key == K_UP) and y > 0:
                    y -= 1
                elif (event.key == K_DOWN) and y < MAPHEIGHT-3:
                    y += 1
                elif event.key == K_SPACE:
                    pygame.mixer.music.load('whoosh.ogg')
                    pygame.mixer.music.play(1)
                    if x == ex1+1:
                        if eH1>0:
                            pygame.mixer.music.load('Enemyhit.ogg')
                            pygame.mixer.music.play(1)
                            a = random.randrange(5,25)
                            eH1 = eH1 - a
                            b = random.randrange(2,20)
                            H = H - b
                            if H<0:
                                die()
                    if x == ex2+1:
                        if eH2>0:
                            pygame.mixer.music.load('Enemyhit.ogg')
                            pygame.mixer.music.play(1)
                            a = random.randrange(5,25)
                            eH2 = eH2 - a
                            b = random.randrange(2,20)
                            H = H - b
                            if H<0:
                                die()
                    if x == ex3+1:
                        if eH3>0:
                            pygame.mixer.music.load('Enemyhit.ogg')
                            pygame.mixer.music.play(1)
                            a = random.randrange(5,25)
                            eH3 = eH3 - a
                            b = random.randrange(2,20)
                            H = H - b
                            if H<0:
                                die()
                    if x == ex4+1:
                        if eH4>0:
                            pygame.mixer.music.load('Enemyhit.ogg')
                            pygame.mixer.music.play(1)
                            a = random.randrange(5,25)
                            eH4 = eH4 - a
                            b = random.randrange(2,20)
                            H = H - b
                            if H<0:
                                die()
                    if x == ex5+1:
                        if eH5>0:
                            pygame.mixer.music.load('Enemyhit.ogg')
                            pygame.mixer.music.play(1)
                            a = random.randrange(5,25)
                            eH5 = eH5 - a
                            b = random.randrange(2,20)
                            H = H - b
                            if H<0:
                                die()
                    if x == ex6+1:
                        if eH6>0:
                            pygame.mixer.music.load('Enemyhit.ogg')
                            pygame.mixer.music.play(1)
                            a = random.randrange(5,25)
                            eH6 = eH6 - a
                            b = random.randrange(2,20)
                            H = H - b
                            if H<0:
                                die()
                    if ex1<=0 and ex2<=0 and ex3<=0 and ex4<=0 and ex5<=0 and ex6<=0:
                        boss(bx,by,bH)
                        if x == bx-1:
                            H = 500
                            if bH>0:
                                pygame.mixer.music.load('Enemyhit.ogg')
                                pygame.mixer.music.play(1)
                                a = random.randrange(10,50)
                                bH = bH - a
                                b = random.randrange(5,20)
                                H = H - b
                                if H<=0:
                                    die()
                                elif bH<=0:
                                    won()                            
        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                gameDisplay.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))

        hero_health(H)
        enemy_health1(eH1)
        enemy_health2(eH2)
        enemy_health3(eH3)
        enemy_health4(eH4)
        enemy_health5(eH5)
        enemy_health6(eH6)
        enemy1(ex1,ey1,eH1)
        enemy2(ex2,ey2,eH2)
        enemy3(ex3,ey3,eH3)
        enemy4(ex4,ey4,eH4)
        enemy5(ex5,ey5,eH5)
        enemy6(ex6,ey6,eH6)
        hero(x,y,H)
        pygame.display.update()
        clock.tick(60)
pygame.mixer.music.load('Theme.ogg')
pygame.mixer.music.play(-1)
intro()
story_line()
game_intro()
mainGame_loop()
pygame.quit()
sys.exit()
