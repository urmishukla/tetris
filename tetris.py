#tetris

import turtle
import random
import time

bg= turtle.Turtle()
bg.speed(0)
bg.color("papayawhip")
bg.shape("square")
bg.shapesize(stretch_wid=6, stretch_len=8)
bg.goto(0,0)

wn= turtle.Screen()
wn.title("Tetris by @urmishukla")
wn.bgcolor("black")
wn.setup(width=600, height=800)
wn.tracer(0)

delay = 0.1

def add(counter):
    counter +=1

class Shape():
    x=5
    y=0
    choice= random.randint(0,7)
    if (choice==0):
        color=4
        square= [[4,4],[4,4]]
        height=2
        length=2
        
    
    if (choice==1):
        color=2
        HL= [[2,2,2,2]]
        height=4
        length=1
        
    if (choice==2):
        color=6
        t= [[0,6,0],[6,6,6]]
        height=2
        length=3
        

    elif (choice==3):
        color=5
        rightZ= [[0,5,5],[5,5,0]]
        height=2
        length=3
        counter=0
        

    elif (choice==4):
        color=7
        leftZ= [[7,7,0],[0,7,7]]
        height=2
        length=3
        counter=0

    elif (choice==5):
        color=1
        rightL= [[1,0,0],[1,1,1]]
        height=2
        length=3
        
    elif (choice==6):
        color=3
        leftL= [[0,0,3],[3,3,3]]
        height=2
        length=3
                   
def moveLeft():
    self.x -= 1
def moveRight():
    self.x+=1
def moveDown():
    self.y+=1
def accelerate():
    self.y+=3

def flip(self):
    wn.onkeypress(add(counter),"Up")
    if (self.choice==1):
        if (counter%2==0 or counter==0):
            self.HL =[[2,2,2,2]]
        elif (counter%2 != 0):
            self.HL= [[2],
                  [2],
                 [2],
                 [2]]
    elif (self.choice==2):
        if (counter%4==0 or counter==0):
            self.t=[[0,6,0],[6,6,6]]
        elif (counter%4 ==1):
            self.t= [[0,6],[6,6],[0,6]]
        elif (counter%4==2):
            self.t=[[6,6,6],[0,6,0]]
        elif (counter%4==3):
            self.t= [[6,0],[6,6],[6,0]]
             
    elif (self.choice==3):
        if (counter%2==0 or counter==0):
            self.rightZ=[[0,5,5],[5,5,0]]
        elif (counter%2 != 0):
            self.rightZ= [[5,0],[5,5],[0,5]]

    elif (self.choice==4):
        if (counter%2==0 or counter==0):
            self.leftZ=[[7,7,0],[0,7,7]]
        elif (counter%2 != 0):
            self.leftZ= [[0,7],[7,7],[7,0]]

    elif (self.choice==5):
        if (counter%4==0 or counter==0):
            self.rightL=[[1,0,0,0],[1,1,1,1]]
        elif (counter%4 ==1):
            self.rightL= [[0,1],[0,1],[0,1],[1,1]]
        elif (counter%4==2):
            self.rightL= [[1,1,1,1],[0,0,0,1]]
        elif (counter%4==3):
            self.rightL= [[1,1],[1,0],[1,0],[1,0]]

    elif (self.choice==6):
        if (counter%4==0 or counter==0):
            self.rightL=[[0,0,3],[3,3,3]]
        elif (counter%4 ==1):
            self.rightL= [[3,3],[0,3],[0,3],[0,3]]
        elif (counter%4==2):
            self.rightL= [[3,3,3,3],[3,0,0,0]]
        elif (counter%4==3):
            self.rightL= [[3,0],[3,0],[3,0],[3,3]]

#checking for collisions



wn.listen()
wn.onkeypress(moveLeft,"Left")
wn.onkeypress(moveRight,"Right")
wn.onkeypress(accelerate,"Down")
    
grid =[
      [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
      [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
      [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
      [8,8,8,1,1,1,1,1,1,1,1,1,1,1,1,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8],
      [8,8,8,0,1,2,3,4,5,6,7,0,1,2,3,8,8,8],
      [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
      [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
      [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]]



pen= turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(None)

        
def draw_grid(pen,grid):
    pen.clear()
    top=280
    left=-170
    # 180 =x, 340=y
    colors= ["black","blue","lightblue","orange","yellow","green", "purple","red","papayawhip"]
    
            
    for y in range (len(grid)):
        for x in range (len(grid[0])):
            screen_x= left + (x * 20)
            screen_y= top - (y * 20)
            color1= colors[grid[y][x]] 
            pen.color(color1)
            pen.goto(screen_x, screen_y)
            pen.stamp()
                
draw_grid(pen, grid)

wn.mainloop()
