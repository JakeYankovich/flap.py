import pygame
import random
pygame.init()

gWidth = 900
gHeight = 600

win = pygame.display.set_mode((gWidth, gHeight))

gameSpeed = 15 #lower is faster

run = True
lose = False

birdup = pygame.image.load('birdup.png')        # importing all the images
pygame.display.set_icon(birdup) 
birdup = pygame.transform.scale(birdup, ((22*3), (18*3)))               # (66 wide, 54 tall)
birddown = pygame.image.load('birddown.png')
birddown = pygame.transform.scale(birddown, ((22*3), (18*3)))   # (66 wide, 54 tall)
pipe = pygame.image.load('pipelong.png')
toppipe = pygame.transform.rotate(pipe, 180)
y = 250
dy = 0
score = 0
def pipey():
    pipeh = random.randint(175, 625)
    toppipeh = pipeh - 675
    px = 1086
    return(pipeh, toppipeh, px)

(pipeheight, toppipeheight, pipex ) = pipey()
(pipeheight2, toppipeheight2, pipex2 ) = pipey()
(pipeheight3, toppipeheight3, pipex3 ) = pipey()
pipex = 800
pipex2 = 1200
pipex3 = 1600

myfont = pygame.font.SysFont('candara', 45) 
textsurface = myfont.render("GAME OVER   [press space to quit]", False, (0,0,0))
scoretext = myfont.render("score ", False, (0,0,0))
newpipe = 1
lastpipe = 3
while run:
    pygame.time.delay(gameSpeed) #delay between frames

    win.fill((215, 230, 255)) #fill background color
    for event in pygame.event.get(): # without this for loop, pygame will go not responding
        if event.type == pygame.QUIT:
            run = False
    
    if dy > -7:     win.blit(birdup,         [400,y]) # draw falling bird
    else:               win.blit(birddown, [400,y]) # draw flapping bird
    
    
    dy += + 0.5 # you are being pulled down by gravity, your speed becomes .5 faster per frame towards the bottom of the screen
    y += dy # height changes based on your speed
    
    pipex -= 3 #moving the three pipes to the left
    pipex2 -= 3
    pipex3 -= 3
    #birdrect = pygame.Rect(400, y, 66, 54)
    p1rect = pygame.Rect(pipex, pipeheight, 86, 800)        # bottom pipe hitboxes
    p2rect = pygame.Rect(pipex2, pipeheight2, 86, 800)
    p3rect = pygame.Rect(pipex3, pipeheight3, 86, 800)
    
    tp1rect = pygame.Rect(pipex, toppipeheight, 86, 500)        # top pipe hitboxes
    tp2rect = pygame.Rect(pipex2, toppipeheight2, 86, 500)
    tp3rect = pygame.Rect(pipex3, toppipeheight3, 86, 500)
    
    
    if p1rect.collidepoint(430, (y+50)):
        win.blit(textsurface,(125, (pipeheight-130)))              #detect hit bottom pipe
        lose = True
    elif p2rect.collidepoint(430, (y+50)):
        win.blit(textsurface,(125, (pipeheight2-130)))          
        lose = True
    elif p3rect.collidepoint(430, (y+50)):
        win.blit(textsurface,(125, (pipeheight3-130)))          
        lose = True
    
    floor = pygame.Rect(0, 650,  900, 50)           # hit floor
    if floor.collidepoint(430, (y+50) ):
        win.blit(textsurface,(125, (pipeheight-130)))          
        lose = True
    
    ceiling = pygame.Rect(0,-10, 900, 10)       #hit ceiling
    if ceiling.collidepoint(430, (y) ):
        dy = 0
    
    if tp1rect.collidepoint(430, (y+15)):
        win.blit(textsurface,(120, (pipeheight-130)))              #detect hit top pipe
        lose = True
    elif tp2rect.collidepoint(430, (y+15)):
        win.blit(textsurface,(120, (pipeheight2-130)))            
        lose = True
    elif tp3rect.collidepoint(430, (y+15)):
        win.blit(textsurface,(120, (pipeheight3-130)))              
        lose = True
    
    #pygame.draw.rect(win, (0, 0, 0), (390, 590, 5, 5))
    if p1rect.collidepoint(400, 650):
        newpipe = 1
        if newpipe != lastpipe:
            score += 1
            lastpipe = newpipe
    elif p2rect.collidepoint(400, 650):
        newpipe = 2
        if newpipe != lastpipe:
            score += 1
            lastpipe = newpipe
    elif p3rect.collidepoint(400, 650):
        newpipe = 3
        if newpipe != lastpipe:
            score += 1
            lastpipe = newpipe
    

    # print score
    scoretext = myfont.render(str(score), False, (0,0,0))
    win.blit(scoretext, (20,20))
    
    win.blit(pipe, [pipex, pipeheight])                         #drawing pipes
    win.blit(toppipe, [pipex, toppipeheight])
    win.blit(pipe, [pipex2, pipeheight2])
    win.blit(toppipe, [pipex2, toppipeheight2])
    win.blit(pipe, [pipex3, pipeheight3])
    win.blit(toppipe, [pipex3, toppipeheight3])
    pygame.display.set_caption(str(score)) 
    
    if pipex < -86:         (pipeheight,    toppipeheight,   pipex   ) = pipey()    # generating new pipes
    elif pipex2 < -86:  (pipeheight2,  toppipeheight2, pipex2 ) = pipey()
    elif pipex3 < -86:  (pipeheight3, toppipeheight3, pipex3 ) = pipey()

    if pygame.key.get_pressed()[pygame.K_SPACE] and dy > 0:         # IF you hit space, your velocity becomes upwards
        dy = -10
    
    while lose == True:     #once you lose the game:
        for event in pygame.event.get(): # without this for loop, pygame will go not responding
            if event.type == pygame.QUIT:
                run = False
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            run = False
            lose = False
        pygame.display.update()
    
    
    
    pygame.display.update() #draw the screen with whatever changes you've made above

pygame.quit()