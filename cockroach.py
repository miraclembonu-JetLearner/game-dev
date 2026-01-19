import pgzrun
import random


WIDTH = 600
HEIGHT = 500


roach = Actor("roach")
roach.pos = 300,300

msg = ""
score = 0

def draw():
    screen.blit("bg",(0,0))
    screen.draw.text("GET THE cockroach",(250,70),color="blue")
    screen.draw.text(msg,(50,30),color="red")
    screen.draw.text(f"score:{score}",(100,400),color="green")





    roach.draw()

def on_mouse_down(pos):
    global msg
    if thief.collidepoint(pos):
        thief.x = random.randint(50,550)
        thief.y = random.randint(50,450)
        msg = "Good Shoot!"
    else:
        msg = "You missed!Try again!!"

def update():
    global msg,score
    if keyboard.up:
        bee.y-=10
    elif keyboard.left:
        bee.x-=10
    elif keyboard.right:
        bee.x+=10
    elif keyboard.down:
        bee.y+=10
    if bee.colliderect(flower):
        flower.x = random.randint(50,550)
        flower.y = random.randint(50,450)
        msg = "Good catch"
        score  +=1        

pgzrun.go()