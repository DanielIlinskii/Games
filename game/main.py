from pygame import *
from enemy import  *
from initial_setting import *


init()
clock = time.Clock()
display.set_caption("Ghost")

zero = time.get_ticks()//1000
game_status = True
while game_status:
    if hero.hp > 0:
        now = time.get_ticks()//1000
        window.fill(Color('white'))
        draw.line(window, (0, 0, 0), (0, 250), (1200, 250), width=7)

        for even in event.get():
            # система
            if even.type == QUIT:
                game_status = False

        keys = key.get_pressed()
        if keys[K_SPACE]:
            hero.jump = True
        if keys[K_a] and hero.x > 0:
            hero.x -= hero.speed
        if keys[K_d] and hero.x < window_w - hero.width:
            hero.x += hero.speed
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

        # respawn enemy0
        if  now == zero + 1: 
            zero = now
            enemy0 = Enemy(48, 48, window_w + 48, 202, 5)



        for enemy in small_enemy_list:
            enemy.logic()

        hero.draw()
        hero.touch_area()
        hero.logic()
        
    for even in event.get():
        # система
        if even.type == QUIT:
            game_status = False
    display.update()
    clock.tick(60)



