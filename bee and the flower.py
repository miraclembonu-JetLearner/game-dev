import pgzrun
import random


WIDTH = 600
HEIGHT = 500


flower = Actor("flower")
flower.pos = 250,350

bee = Actor("bee")
bee.pos = 300,300
msg = ""
score = 0

def draw():
    screen.blit("bg",(0,0))
    screen.draw.text("GET THE FLOWER",(250,70),color="blue")
    screen.draw.text(msg,(50,30),color="red")
    screen.draw.text(f"score:{score}",(50,400),color="Black")

    bee.draw()
    flower.draw()

def update():
    if keyboard.up:
        bee.y-=1
    elif keyboard.left:
        bee.x-=1
    elif keyboard.right:
        bee.x+=1
    elif keyboard.down:
        bee.y+=1    

        
        

pgzrun.go()