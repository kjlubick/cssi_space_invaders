# Player
player_x = 300
player_y = 500
player_projectiles = []
MAX_PROJECTILES = 3
PROJECTILE_COOLDOWN = 20
projectile_cooldown = 0
ship_size = 10
player_score = 0

# Enemies
enemy_x = 25
enemy_y = 50
enemy_dx = 1
enemy_step_y = 10

enemy_width = 40
enemy_space = 60
enemy_block_width = enemy_width + enemy_space
enemy_block_height = 50

enemies=[
       ["square", "square", "square", "square", "square"],
       ["square", "square", "square", "square", "square"],
       ["circle", "circle", "circle", "circle", "circle"],
       ["circle", "circle", "circle", "circle", "circle"],
]

# Board
WIDTH = 600
HEIGHT = 600

def setup():
    global WIDTH, HEIGHT
    size(WIDTH, HEIGHT)
    
def draw():
    background(0,0,0)
    drawScore()
    drawEnemies()
    updateShip()
    checkProjectiles()
    drawProjectiles()
    drawShip(player_x, player_y)
    
    moveEnemies()
    checkGameOver()
    
    delay(16)
    
def drawScore():
    textSize(30)
    fill(255, 255, 255) 
    text("Score: "+str(player_score), 400, 30) 

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
        y += enemy_block_height

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
    
    elif (enemy_y + enemy_rows * enemy_block_height) >= player_y:
        enemy_dx = 0
        text("GAME OVER", 150, 250)

def checkProjectiles():
    global player_score
    to_remove = None
    for e_i, r in enumerate(enemies):
        for e_j, e in enumerate(r):
            if e == "":
                continue
            for p_i, p in enumerate(player_projectiles):
                px, py = p[0], p[1]
                ex = e_j * enemy_block_width  + enemy_x
                ey = e_i * enemy_block_height + enemy_y
                if e == "square":
                    if px > ex and px < (ex + enemy_width) and py > ey and py < (ey + enemy_width):
                        enemies[e_i][e_j] = ""
                        to_remove = p_i
                        player_score += 200
                elif e == "circle":
                    r = enemy_width/2
                    cx = ex + r
                    cy = ey + r
                    d = sqrt((cx - px) * (cx - px) + (cy - py) * (cy - py))
                    if d < r:
                        enemies[e_i][e_j] = ""
                        to_remove = p_i
                        player_score += 100
    if to_remove is not None:
        print("hit", to_remove)
        player_projectiles.pop(to_remove)
        
def drawShip(ship_x, ship_y):
    fill(0, 255, 0)
    global ship_size
    triangle(ship_x - ship_size, ship_y, ship_x, ship_y - ship_size, ship_x + ship_size, ship_y)

def drawProjectiles():
    global player_projectiles
    dy = -10
    fill(255, 255, 255)
    to_remove = None
    for i, projectile in enumerate(player_projectiles):
        projectile[1] = projectile[1] + dy
        if projectile[1] < 0:
            if to_remove:
                print("multiple projectiles to remove!?")
            to_remove = i
        else:
            ellipse(projectile[0], projectile[1], 10, 10)
    if to_remove is not None:
        print("removing", to_remove)
        player_projectiles.pop(to_remove)



def updateShip():
    global projectile_cooldown
    projectile_cooldown = projectile_cooldown - 1
    if not keyPressed:
        return
    global player_x, WIDTH, player_projectiles
    dx = 5
    if key == " ":
      if projectile_cooldown <= 0 and len(player_projectiles) < MAX_PROJECTILES:
        player_projectiles.append([player_x, player_y - ship_size])
        print ("fired a missile")
        projectile_cooldown = PROJECTILE_COOLDOWN

    elif key == CODED:
        if keyCode == LEFT or keyCode == RIGHT:
            if keyCode == LEFT:
                dx = -dx
            player_x = player_x + dx
            if player_x - ship_size < 0:
                player_x = ship_size
            elif player_x + ship_size > WIDTH:
                player_x = WIDTH - ship_size
