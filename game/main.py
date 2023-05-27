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
        window.blit(bg, (0,0))
        draw.line(window, (0, 0, 0), (0, 250), (1200, 250), width=7)
        text2 = f2.render(str(now), True, (0, 0, 0))
        window.blit(text2, (100, 100))


        # respawn enemys
        if  now == zero + 1: 
            print(zero)
            zero = now
            if zero % 10 == 0 and len(boss1_list) < 1: # respawn boss1
                boss1 = Boss1(60, 60, 1200, 200, 3)
            

            
            if enemy_flag:
                enemy0 = Enemy(48, 48, window_w + 48, 202, 5)
            
        
        if len(boss1_list) == 0:
            enemy_flag = True
        else:
            enemy_flag = False
        

        for enemy in all_enemy:
            enemy.logic()
        
        for bull in bullet_list:
            bull.logic()


        hero.logic()
    else:
        window.blit(gos, (0,0))




    # system
    for even in event.get():
        if even.type == QUIT:
            game_status = False
        if even.type == MOUSEBUTTONDOWN:
            if even.button == 1:
                bullet = Bullet()
    keys = key.get_pressed()
    if keys[K_SPACE]:
        hero.jump = True
    if keys[K_a] and hero.x > 0:
        hero.x -= hero.speed
    if keys[K_d] and hero.x < window_w - hero.width:
        hero.x += hero.speed
    # if keys[K_q]:
    #     bullet = Bullet()
  
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



