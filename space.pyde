enemy_x = 25
enemy_y = 50
enemy_dx = 3
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
    global enemy_x
    global enemy_y
    global enemy_dx
    
    background(0,0,0)
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
        
    if enemy_x < 25 or enemy_x > 125:
        enemy_dx *= -1
        enemy_y += enemy_step_y
    enemy_x += enemy_dx
    
    if (enemy_y + len(enemies) * enemy_height) > 550:
        enemy_dx = 0
        print("GAME OVER")
    
    delay(16)
    
