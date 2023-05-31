from pygame import *
from enemy import  *

from initial_setting import *
from random import randint

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
        window.blit(text2, (window_w / 2, 0))


        # respawn enemys
        if  now == zero + 1: 
            print(zero)
            zero = now
            # if zero % 10 == 0 and len(boss1_list) < 1: # respawn boss1
            #     boss1 = Boss1(60, 60, 1200, 200, 3)
            # if zero % 20 and len(boss2_list) < 1 :
            #     boss2 = Boss2(80, 80, 1300, 200, 5)
            if zero % 5 == 0 and len(boss_list) == 0:
                index = randint(1, 3)
                if index == 1:
                    boss1 = Boss1(60, 60, 1200, 200, 3)
                if index == 2:
                    boss2 = Boss2(80, 80, 1300, 200, 5)
                    drop_flag = True
                    if boss2 not in boss_list:
                        drop_flag = False

            if enemy_flag:
                enemy0 = Enemy(48, 48, window_w + 48, 202, 5) 

            # if Boss2:
            #     Drop()
            if drop_flag:
                Drop()
 
        for drop in drop_list:
            drop.logic()    
        
        if len(boss_list) == 0:
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
            if even.button == 3:
                print(even.pos)
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



