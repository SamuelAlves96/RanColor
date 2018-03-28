import pygame
import random
import time


#Width and Height of each cell
WIDTH = 20
HEIGHT = 20
 
#margin between each cell
MARGIN = 5
 
#creates the grid
grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)  

#background color 
bg=(0,0,0)


pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("RanColor")
 
done = False

 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    
    for i in range(1):
        #random cell
        y=random.randint(0,9)
        u=random.randint(0,9)
        #a set of colors for the program to choose. True random values were
        #not used becuase otherwise 2 colors could be smiliar and the eye
        #could not notice the diferance between 2 cells
        a=(204,0,102)
        s=(153,0,153)
        d=(0,204,204)
        f=(147,250,78)
        g=(255,255,51)
        h=(250,95,78)
        i=(78,235,250)
        j=(250,78,124)
        k=(143,51,102)
        l=(255,0,0)
        z=(0,0,204)
        x=(255,97,171)
        c=(204,255,102)
        v=(229,204,255)
        #makes the tick wait
        time.sleep(0.1)
        #selects the cell
        grid[y][u] = random.randint(1,14)
                
       
    #screen and cell background
    screen.fill(bg)
    cell=(128,128,128)
    #draw grid
    for row in range(10):
        for column in range(10):
            color = cell
            if grid[row][column] == 1:
                color = a
            if grid[row][column] == 2:
                color = s
            if grid[row][column] == 3:
                color = d
            if grid[row][column] == 4:
                color = f
            if grid[row][column] == 5:
                color = g
            if grid[row][column] == 6:
                color = h
            if grid[row][column] == 7:
                color = j
            if grid[row][column] == 8:
                color = k
            if grid[row][column] == 9:
                color = l
            if grid[row][column] == 10:
                color = z
            if grid[row][column] == 11:
                color = x
            if grid[row][column] == 12:
                color = c
            if grid[row][column] == 13:
                color = v
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 

    #screen update
    pygame.display.update()

pygame.quit()
