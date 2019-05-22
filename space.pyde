# Player
player_x = 300
player_y = 500

# Enemies
enemy_x = 25
enemy_y = 50
enemy_dx = 1
enemy_step_y = 10

enemy_width = 40
enemy_space = 60
enemy_height = 50

enemies=[
       ["square", "square", "square", "square", "square"],
       ["square", "square", "square", "square", "square"],
       ["circle", "circle", "circle", "circle", "circle"],
       ["circle", "circle", "", "circle", "circle"],
]

def setup():
    size(600, 600)
    
def draw():
    background(0,0,0)
    drawEnemies()
    drawShip(player_x, player_y)
    
    moveEnemies()
    checkGameOver()
    
    delay(16)
    
def drawEnemies():    
    stroke(255,255,255)
    fill(255, 0, 255)
    y = enemy_y
    for r in enemies:
        x = enemy_x
        for e in r:
            if e == "square":
                rect(x, y, enemy_width, enemy_width)
            elif e == "circle":
                ellipse(x+enemy_width/2, y+enemy_width/2, enemy_width, enemy_width)
            x += (enemy_width + enemy_space)
        y += enemy_height

def moveEnemies():
    global enemy_x
    global enemy_y
    global enemy_dx
    
    if enemy_x < 25 or enemy_x > 125:
        enemy_dx *= -1
        enemy_y += enemy_step_y
    enemy_x += enemy_dx

def checkGameOver():
    global enemy_dx
    enemy_rows = 0
    for r in enemies:
        for e in r:
            if e != "":
                enemy_rows+=1
                break
    textSize(60)
    fill(255, 255, 255)
    if enemy_rows == 0:
        # WINNER
        enemy_dx = 0
        text("You won!!", 150, 250)
    
    elif (enemy_y + enemy_rows * enemy_height) >= player_y:
        enemy_dx = 0
        text("GAME OVER", 150, 250)

def drawShip(ship_x, ship_y):
    fill(0, 255, 0)
    ship_size = 10
    triangle(ship_x - ship_size, ship_y, ship_x, ship_y - ship_size, ship_x + ship_size, ship_y)
