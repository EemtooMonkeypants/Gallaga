import pgzrun
WIDTH = 600
HEIGHT = 800
TITLE = 'Gallaga Game'
ship = Actor('galaga')
ship.x = 300
ship.y = 750
bugs = []
bullets = []
for i in range(5):
    for j in range(5):
        bug = Actor('bug')
        bugs.append(bug)
        bug.x = 100+i*100
        bug.y = 100+j*50

def draw():
    screen.clear()
    ship.draw()
    for thing in bugs:
        thing.draw()
    for i in bullets:
        i.draw()
def update():
    if keyboard.left:
        ship.x = ship.x - 10
    if keyboard.right:
        ship.x = ship.x+10
    for thing in bugs:
        thing.y = thing.y+0.5
    for i in bullets:
        i.y = i.y - 10
def on_key_down(key):
    global bullets
    if key==keys.SPACE:
        bullet = Actor('bullet')
        bullet.x = ship.x
        bullet.y = ship.y
        bullets.append(bullet)
pgzrun.go()
