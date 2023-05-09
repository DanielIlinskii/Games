from pygame import *
from enemy import  *


init()

clock = time.Clock()

game_status = True
while game_status:
    
    # # выйти из цикличности классового параметра
    # window.blit(bg, (bg_x, 0))
    # window.blit(bg, (bg_x + window_w, 0))

    bg.reset()
    bg1.reset()
    bg.x -= bg.speed
    bg1.x -= bg.speed
    if bg.x == -bg.width:
        bg.x = bg.width
    if bg1.x == -bg1.width:
        bg1.x = bg1.width


    draw.line(window, (0, 0, 0), (0, 250), (1200, 250), width=7)


    hero.touch_area()
    hero.reset()
    hero.update()

    for even in event.get():

        # система
        if even.type == QUIT:
            game_status = False


    keys = key.get_pressed()
    if keys[K_SPACE]:
        hero.jump = True
    if keys[K_a] and hero.x > 0:
        hero.x -= hero.speed
        # bg.speed = 1
        # bg1.speed = 1
    if keys[K_d] and hero.x < window_w - hero.width:
        hero.x += hero.speed
        # bg.speed = 3
        # bg1.speed = 3
    




    
    if hero.jump:
        if hero.j_count >= -10:
            if hero.j_count <= 0:
                hero.y += (hero.j_count ** 2) / 3
            else:
                hero.y -= (hero.j_count ** 2) / 3
            hero.j_count -= 1
        else:
            hero.jump = False
            hero.j_count = 10






    display.update()
    clock.tick(60)



