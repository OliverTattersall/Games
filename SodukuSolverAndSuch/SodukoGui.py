import pygame
import requests
import copy
import time


WIDTH = 600 
bg_color = (251, 247, 245)

level = "easy"
response = requests.get("https://sugoku.herokuapp.com/board?difficulty="+level)
grid=response.json()['board']
grid_og=copy.deepcopy(grid)

# grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]
# grid_og=copy.deepcopy(grid)
# print(grid)
ans=[]


def possible(soduko, x, y, n):

    for i in range(0, 9):
        if soduko[y][i]==n:
            return False
        if soduko[i][x]==n:
            return False

    x0 = (x//3)*3
    y0=(y//3)*3
    for i in range(3):
        for j in range(3):
            if soduko[y0+i][x0+j]==n:
                return False

    return True
def solve(g):
    global ans
    for y in range(9):
        for x in range(9):
            if g[y][x]==0:
                for n in range(1, 10):
                    if possible(g, x,y,n):
                        g[y][x]=n
                        solve(g)
                        g[y][x]=0
                return 

    ans=copy.deepcopy(g)
    # print(ans)
    # print("b")

def check(grid, grid_og):
    grid2 = copy.deepcopy(grid)

    solve(grid2)
    for i in range(9):
        for j in range(9):
            if grid2[i][j]==grid_og[i][j]:
                return False

    return True

def fillboard(win, grid, grid2):

    global ans
    myfont = pygame.font.SysFont("Comic Sans MS", 35)
    # grid2=copy.deepcopy(grid)
    ans=[]
    solve(grid)
    # print(ans)
    # print(grid2)
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                # print(grid[i][j])
                if grid2[i][j]!=0:
                    pygame.draw.rect(win, bg_color, (50*(1+j)+4, 50*(i+1)+4, 42, 42))
                    
                value = myfont.render(str(ans[i][j]), True, (0,0,0))
                win.blit(value, (65+50*j, 50+50*i))
            # pygame.display.update()

    pygame.display.update()

def insert(win, pos, myfont):
    pos = (pos[0]//50-1, pos[1]//50 -1)
    if pos[0]<0 or pos[0]>8 or pos[1]<0 or pos[1]>8:
        return
    print(pos)
    if grid[pos[1]][pos[0]]!=0:
        print("fail")
        return

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type ==pygame.KEYDOWN:
                print(event.key)
                if event.key==8:
                    grid_og[pos[1]][pos[0]]=0
                    pygame.draw.rect(win, bg_color, (50*(1+pos[0])+4, 50*(pos[1]+1)+4, 42, 42))
                    pygame.display.update()


                if event.key>48 and event.key<58:
                    grid_og[pos[1]][pos[0]]=event.key-48
                    value=myfont.render(str(grid_og[pos[1]][pos[0]]), True, (0,0,0))
                    # win.blit(myfont.render("", True, (0,0,0)), (65+50*pos[1], 50+50*pos[0]))
                    pygame.draw.rect(win, bg_color, (50*(1+pos[0])+4, 50*(pos[1]+1)+4, 42, 42))
                    win.blit(value, (65+50*pos[0], 50+50*pos[1]))
                    pygame.display.update()
                    return

def main():
    global ans
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("SODUKO")
    win.fill(bg_color)
    myfont = pygame.font.SysFont("Comic Sans MS", 35)
    
    pygame.draw.rect(win, (220,34,123), (250, 525, 100, 30))
    win.blit(pygame.font.SysFont("Comic Sans MS", 13).render("Check answer", True, (0,0,0)), (255,525))
    pygame.draw.rect(win, (220,34,123), (355, 525, 100, 30))
    win.blit(pygame.font.SysFont("Comic Sans MS", 13).render("Show solution", True, (0,0,0)), (360,525))

    for i in range(0,10):
        temp=0
        if i%3==0:
            temp=2
        pygame.draw.line(win, (0,0,0), (50+50*i, 50),(50+50*i, 500),2+temp)
        pygame.draw.line(win, (0,0,0), (50, 50+50*i),(500, 50+50*i),2+temp)
        
    for i in range(9):
        for j in range(9):
            if grid[i][j]!=0:
                value=myfont.render(str(grid[i][j]), True, (52,130,60))
                
                win.blit(value, (65 + 50*j, 50 + 50*i))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONUP and event.button==1:
                pos=pygame.mouse.get_pos()
                if (pos[0]>=250 and pos[0]<=350) and (pos[1]>=525 and pos[1]<=555):
                    if check(grid, grid_og):
                        print("well done")
                    else:
                        print("incorrect answer")
                if (pos[0]>=350 and pos[0]<=450) and (pos[1]>=525 and pos[1]<=555):
                    fillboard(win, grid, grid_og)
                # print(pos)
                insert(win, pos, myfont)
            if event.type == pygame.QUIT:
                pygame.quit()
                return




main()