from turtle import color
import pgzrun
import random


WIDTH = 500
HEIGHT = 600


msg = ""
score = 0

no_of_satelites=10
sats=[]
lines = []
next=0
for i in range(no_of_satelites):
    satelite = Actor("satelite")
    satelite.pos = 250,350
    satelite.x = random.randint(50,450)
    satelite.y = random.randint(50,350)
    sats.append(satelite)



def draw():
    screen.blit("space",(0,0))
    screen.draw.text("Connect the satelite",(250,10),color="red")
    number =1
    for i in sats:
        i.draw()
        screen.draw.text(str(number),(i.x,i.y+10),color="white")
        number+=1




    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))  


def on_mouse_down(pos):
    global sats,next,lines
    if sats[next].collidepoint(pos):
        if next:
            lines.append((sats[next-1].pos,sats[next].pos))
        next+=1
    else:
        lines = []
        next=0

def update():
    pass





pgzrun.go()    