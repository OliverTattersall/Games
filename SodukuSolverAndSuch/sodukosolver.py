import numpy as np
import copy

# print("input soduko row by row put 0 for blank spaces and a space between each box")
# soduko=''
# for i in range(8):
#     soduko+=input("row: ")+"\n"
# soduko+=input("final row: ")


soduko = '''5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9'''

soduko=soduko.split("\n")
for i in range(9):
    soduko[i]=soduko[i].split(" ")
    # fun = lambda x:int(x)
    soduko[i] = list(map(int, soduko[i]))
print(soduko)
print(np.matrix(soduko))






#### Soduko solver without back tracking
available=[[set([i for i in range(1,10)]) for i in range(9)] for i in range(9)]
# print(available)
# remove()

for i in range(9):
    for j in range(9):
        temp=soduko[i][j]
        if temp!=0:
            available[i][j]=set([])
            for k in range(9):
                if temp in available[i][k]:
                    available[i][k].remove(temp)
                if temp in available[k][j]:
                    available[k][j].remove(temp)
            stepi = (i)//3
            stepj=j//3
            for m in range(3):
                for n in range(3):
                    if temp in available[m+stepi*3][n+stepj*3]:
                        available[m+stepi*3][n+stepj*3].remove(temp)

# print(np.matrix(available))

def update(i,j, num, available):
    available[i][j]=set([])
    for k in range(9):
        if num in available[i][k]:
            available[i][k].remove(num)
        if num in available[k][j]:
            available[k][j].remove(num)
    stepi = (i)//3
    stepj=j//3
    for m in range(3):
        for n in range(3):
            if num in available[m+stepi*3][n+stepj*3]:
                available[m+stepi*3][n+stepj*3].remove(num)
    return available

def change(available):
    for i in range(9):
        for j in range(9):
            if len(available[i][j])==1:
                # print(available[i][j], i, j)
                soduko[i][j]=list(available[i][j])[0]
                available[i][j]=set([])
                available= update(i, j, soduko[i][j], available)
                change(available)

    


change(available)
# print(np.matrix(available))
# print(np.matrix(soduko))






soduko = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]

### soduko solver with back tracking

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
def solve(grid):
    global count
    global ans
    for y in range(9):
        for x in range(9):
            if grid[y][x]==0:
                for n in range(1, 10):
                    if possible(grid, x,y,n):
                        grid[y][x]=n
                        solve(grid)
                        grid[y][x]=0
                return 



    count+=1
    print(np.matrix(grid))
    # print(count)
    ans = copy.deepcopy(grid)
    return grid

print(soduko)
x=[[0, 0, 0, 8, 0, 3, 0, 0, 5], [0, 0, 0, 4, 0, 0, 7, 0, 0], [0, 0, 8, 0, 0, 0, 0, 3, 6], [0, 0, 4, 0, 6, 0, 0, 0, 0], [3, 6, 5, 7, 9, 8, 0, 1, 0], [7, 0, 0, 1, 2, 4, 5, 6, 0], [5, 3, 0, 0, 4, 0, 0, 0, 0], [8, 0, 0, 9, 3, 7, 6, 5, 0], [0, 7, 0, 5, 8, 0, 0, 4, 2]]
count=0
ans=[]
print(solve(soduko))
print(ans)
# print(x)

