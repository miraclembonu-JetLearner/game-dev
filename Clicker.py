import pgzrun
import time


WIDTH= 300
HEIGHT = 300

coin = Actor("coin")
coin.pos = 300,300


msg = ""
coins = 0
coins_per_click = 1
coins_per_second = 0

upgrade_click_cost = 10
upgrade_auto_cost = 25

last_time = time.time()



def draw():
    screen.fill("white")
    screen.draw.text("num1=upgradeclicks , num2=upgradeautoclick, click with mouse",(250,70),color="blue")
    coin.draw()

if coins >= upgrade_click_cost:
    screen.draw.text("Upgrade click available!",(250,100),color="green")
else:
    screen.draw.text("Upgrade click unavailable!",(250,100),color="red")

if coins >= upgrade_auto_cost:
    screen.draw.text("Upgrade auto available!",(250,130),color="green")
else:
    screen.draw.text("Upgrade auto unavailable!",(250,130),color="red")

def on_mouse_down(pos):
    if coin.collidepoint(pos):
        click()





msg = f"Coins: {coins} | Coins per click: {coins_per_click} | Coins per second: {coins_per_second}"


def click():
    global coins
    coins += coins_per_click
    print(f"You clicked! Coins: {coins}")

def upgrade_click():
    global coins, coins_per_click, upgrade_click_cost
    if coins >= upgrade_click_cost:
        coins -= upgrade_click_cost
        coins_per_click += 1
        upgrade_click_cost*= 2
        print(f"Click upgraded! Coins per click: {coins_per_click}")
    else:
        print("Not enough coins to upgrade click.")

def upgrade_auto():
    global coins, coins_per_second, upgrade_auto_cost
    if coins >= upgrade_auto_cost:
        coins -= upgrade_auto_cost
        coins_per_second += 1
        upgrade_auto_cost*= 2
        print(f"Auto upgrade! Coins per second: {coins_per_second}")
    else:
        print("Not enough coins to upgrade auto.")


while True:
    now = time.time()
    elapsed = now - last_time
    last_time = now 
    coins += coins_per_second * elapsed


    print_status()
    choice = input('input choice: ')

    if choice == "1":
      upgrade_click()

    elif choice == "2":
        upgrade_auto()

    else:
        print("Invalid choice. Please try again.")




    

