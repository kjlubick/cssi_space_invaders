enemy_x = 50
enemy_y = 50
enemy_dx = 1
enemy_step_y = 10

enemy_width = 40
enemy_space = 60
enemy_height = 100

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
    background(0,0,0)
    stroke(255,255,255)
    fill(255, 0, 255)
    y = enemy_y
    for r in enemies:
        x = enemy_x
        for e in enemies:
            rect(x, y, enemy_width, enemy_width)
            x += (enemy_width + enemy_space)
        y += enemy_height
        
    enemy_x += enemy_dx
    
    delay(16)
    
