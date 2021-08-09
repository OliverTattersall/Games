import pygame, sys
from pygame.locals import*
import random
# print(dir(pygame))
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")
win.fill((25,70,0))
pygame.draw.rect(win, (255,0,0), (400, 400, 20, 20),0)

pygame.display.update()

class rect(object):
    
    def __init__(self, x=random.randint(100,400), y = random.randint(100,400), width=40, height=40, color = (255,0,0)):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color

    def draw(self):
        pygame.draw.rect(win, color, (self.x,self.y,self.width, self.height))

class player(object):

    def __init__(self, x, y, width, height, color):
        rect.__init__(self, x,y,width, height, color)




x=50
y=50
width=40
height=40
vel=5

run = True

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type==pygame.KEYDOWN:
            # print(event)

            if event.key==pygame.K_LEFT:
                if x<=50:
                    print()
        # else:
        #     print(event)

    keys = pygame.key.get_pressed()
    # print(keys[pygame.K_LEFT])
    pygame.draw.rect(win, (30,80,255), (x,y,width, height),0)

    pygame.display.update()
    



pygame.quit()


# import pygame, sys
# from pygame.locals import*

# pygame.init()
# SCREENWIDTH = 800
# SCREENHEIGHT = 800
# RED = (255,0,0)
# screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

# pygame.draw.rect(screen, RED, (400, 400, 20, 20),0)
# screen.fill(RED)

# pygame.display.update()

# # waint until user quits
# running = True
# while running:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False


# pygame.quit()