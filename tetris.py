#tetris

import turtle
import random
import time

wn= turtle.Screen()
wn.title("Tetris by @urmishukla")
wn.bgcolor("honeydew")
wn.setup(width=600, height=800)
wn.tracer(0)


x=0
#shape=[[4,4],[4,4]]

writer = turtle.Turtle()
writer.speed(0)
writer.hideturtle()
writer.color("honeydew")
writer.goto(-80,320)
writer.color("black")
writer.write("TETRIS",move=False, align="left", font=("Helvetica", 32, "normal"))

pen1 = turtle.Turtle()
pen1.speed(0)
pen1.hideturtle()
pen1.color("honeydew")
pen1.goto (-60, 280)
pen1.color("black")
pen1.write("Score = ", move=False, align="left", font=("Helvetica", 18,"normal"))


delay = 0.8

def add(counter):
    counter +=1

class Shape():
    x=5
    y=0
    height=0
    length=0
    choice= random.randint(0,6)
    if (choice==0):
        color=4
        shape= [[4,4],[4,4]]
        height=2
        length=2
        
    
    if (choice==1):
        color=2
        shape= [[2,2,2,2]]
        height=4
        length=1
        
    if (choice==2):
        color=6
        shape= [[0,6,0],[6,6,6]]
        height=2
        length=3
        

    elif (choice==3):
        color=5
        shape= [[0,5,5],[5,5,0]]
        height=2
        length=3
        counter=0
        

    elif (choice==4):
        color=7
        shape= [[7,7,0],[0,7,7]]
        height=2
        length=3
        counter=0

    elif (choice==5):
        color=1
        shape= [[1,0,0],[1,1,1]]
        height=2
        length=3
        
    elif (choice==6):
        color=3
        shape= [[0,0,3],[3,3,3]]
        height=2
        length=3

def erase(self, grid):
    for g in range (len(self.shape)):
        for f in range (len(self.shape[g])):
            if (self.shape[g][f] >0):
                grid[self.y+g][self.x+f] =0
    
                   
def moveLeft(self,grid):
    if (self.x > 0):
        if (grid [self.y][self.x -1] ==0):
            erase(self,grid)
            self.x -=1
            
def moveRight(self,grid):
    if (self.x < 12 - self.length):
        if (grid [self.y][self.x + self.length] ==0):
            erase(self,grid)
            self.x +=1
            
def moveDown(self,grid):
    if (canMove):
        erase(self,grid)
        self.y +=1
    
def accelerate(self,grid):
    if (canMove):
        for x in range (self.length):
            if (grid[self.y +self.height +3][self.x] ==0):
                self.y+=3

def canMove(self, grid):
    check=True
    for x in range (self.length):
        if (self.shape[self.height -1][x] >0):
            if (grid[self.y + self.height][self.x +x] != 0):
                check =False
    return check


def flip(self):
    counter=0
    wn.onkeypress(add(counter),"Up")
    if (self.choice==1):
        if (counter%2==0 or counter==0):
            self.shape =[[2,2,2,2]]
        elif (counter%2 != 0):
            self.shape= [[2],
                  [2],
                 [2],
                 [2]]
        self.height= len(shape)
        self.length= len(shape[0])
        
    elif (self.choice==2):
        if (counter%4==0 or counter==0):
            self.shape=[[0,6,0],[6,6,6]]
        elif (counter%4 ==1):
            self.shape= [[0,6],[6,6],[0,6]]
        elif (counter%4==2):
            self.shape=[[6,6,6],[0,6,0]]
        elif (counter%4==3):
            self.shape= [[6,0],[6,6],[6,0]]
            
        self.height= len(shape)
        self.length= len(shape[0])
             
    elif (self.choice==3):
        if (counter%2==0 or counter==0):
            self.shape=[[0,5,5],[5,5,0]]
        elif (counter%2 != 0):
            self.shape= [[5,0],[5,5],[0,5]]
            
        self.height= len(shape)
        self.length= len(shape[0])

    elif (self.choice==4):
        if (counter%2==0 or counter==0):
            self.shape=[[7,7,0],[0,7,7]]
        elif (counter%2 != 0):
            self.shape= [[0,7],[7,7],[7,0]]
            
        self.height= len(shape)
        self.length= len(shape[0])

    elif (self.choice==5):
        if (counter%4==0 or counter==0):
            self.shape=[[1,0,0,0],[1,1,1,1]]
        elif (counter%4 ==1):
            self.shape= [[0,1],[0,1],[0,1],[1,1]]
        elif (counter%4==2):
            self.shape= [[1,1,1,1],[0,0,0,1]]
        elif (counter%4==3):
            self.shape= [[1,1],[1,0],[1,0],[1,0]]

        self.height= len(shape)
        self.length= len(shape[0])

    elif (self.choice==6):
        if (counter%4==0 or counter==0):
            self.shape=[[0,0,3],[3,3,3]]
        elif (counter%4 ==1):
            self.shape= [[3,3],[0,3],[0,3],[0,3]]
        elif (counter%4==2):
            self.shape= [[3,3,3,3],[3,0,0,0]]
        elif (counter%4==3):
            self.shape= [[3,0],[3,0],[3,0],[3,3]]

        self.height= len(shape)
        self.length= len(shape[0])

self= Shape()
    
grid =[
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [1, 2, 3, 4, 4, 5, 6, 7, 5, 3, 2, 1]]


wn.listen()
wn.onkeypress(moveLeft(self,grid),"Left")
wn.onkeypress(moveRight(self,grid),"Right")
wn.onkeypress(accelerate(self,grid),"Down")

pen= turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(None)

Pen = turtle.Turtle()
Pen.penup()
Pen.hideturtle()
Pen.speed(0)
Pen.shape("square")
#Pen.setundobuffer(None)


colors= ["black","royalblue","mediumturquoise","darkorange","yellow","green", "mediumorchid","firebrick","gold","goldenrod"]

def draw_grid(pen,grid):
    pen.clear()
    top=230
    left=-110
    # 180 =x, 340=y
            
    for y in range (len(grid)):
        for x in range (len(grid[0])):
            screen_x= left+ (x * 20)
            screen_y= top - (y * 20)
            color1= colors[grid[y][x]] 
            pen.color(color1)
            pen.goto(screen_x, screen_y)
            pen.stamp()
                
draw_grid(pen, grid)

def drawBlock(self,grid):
    top=230
    left=-110
    for g in range (0,len(self.shape)):
        for f in range (0,len(self.shape[0])):
            Color= self.shape[g][f]  # returns a number representing color code
            pen.color(colors[Color])
            coordinateX= left + 20 *(self.x +f)
            coordinateY= top - 20*(self.y+g)
            pen.goto(coordinateX,coordinateY)
            pen.stamp()  
#self= Shape()
#main game loop
linesFilled=0
self = Shape()

while True:
    time.sleep(0.01)
    wn.update()

    erase(self,grid)
    drawBlock(self,grid)
    moveDown(self,grid)
    time.sleep(delay)
    
    
    
    


wn.mainloop()
