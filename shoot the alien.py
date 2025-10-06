import pgzrun
import random

WIDTH = 600
HEIGHT = 500

alien = Actor("alien")
alien.pos = 300,300
msg = ""
score = 0


def draw():
    screen.fill("violet")
    screen.draw.text("SHOOT THE ALIEN",(250,70),color="blue")
    screen.draw.text(msg,(50,30),color="red")
    screen.draw.text(f"score:{score}",(50,400),color="green")

    alien.draw()

def on_mouse_down(pos):
    global msg,score
    if alien.collidepoint(pos):
        alien.x = random.randint(50,550)
        alien.y = random.randint(50,450)
        msg = "Good Shoot!"
        score +=1
    else:
        msg = "You missed!Try again!!"
        score -=1


def update():
    pass

pgzrun.go()