from pygame import *
from random import randint

init()

window_w = 1200
window_h = 700

window = display.set_mode((window_w, window_h))
bg = transform.scale(image.load(r'C:\Users\028\Downloads\game\sprites\background.jpg').convert(), (window_w, window_h))

gos = transform.scale(image.load(r'C:\Users\028\Downloads\game\sprites\game-over-screen.jpg').convert(), (window_w, window_h))


class Hero:
    def __init__(self, width, height, x, y, speed):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed
        self.image = transform.scale(image.load(r'C:\Users\028\Downloads\game\sprites\walk1.png').convert_alpha(), (self.width, self.height))
        self.jump = False
        self.j_count = 10
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.heart = transform.scale(image.load(r'C:\Users\028\Downloads\game\sprites\heart.png').convert_alpha(), (25, 25))
        self.hp = 5

    
    def touch_area(self):
        draw.rect(window, (255, 0, 0), Rect(self.x, self.y, self.width, self.height), 1)
    
    def draw(self):
        window.blit(self.image, (self.x, self.y))
        self.rect.x = self.x
        self.rect.y = self.y

    def health(self):
        for i in range(self.hp):
            window.blit(self.heart, (950 + i*50, 25))
    

    
    def logic(self):
        self.health()
        self.touch_area()
        self.draw()

hero = Hero(48, 48, 15, 200, 10)




class Bullet:
    def __init__(self):
        self.image = transform.scale(image.load(r'C:\Users\028\Downloads\game\sprites\fireball.png').convert_alpha(), (16, 16))
        self.speed = 10
        self.x = hero.x
        self.y = hero.y + hero.height/2
        self.rect = Rect(self.x, self.y, 16, 16)
        self.damage = 1
        bullet_list.append(self)
    
    def update(self):
        self.x += self.speed
        self.rect.x = self.x
        if self.x < 0:
            bullet_list.remove(self)
        for enemy in all_enemy:
            if self.rect.colliderect(enemy.rect):
                # иногда пуля касается монстра и выходит за пределы карты одновременно, поэтому использую конструкцию try except
                try:
                    self.image = transform.scale(image.load(r'C:\Users\028\Downloads\game\sprites\explose.png').convert_alpha(), (48, 48))
                    bullet_list.remove(self)
                    enemy.hp -= self.damage
                    self.image = transform.scale(image.load(r'C:\Users\028\Downloads\game\sprites\fireball.png').convert_alpha(), (16, 16))
                except:
                    pass

    def touch_area(self):
        draw.rect(window, (255, 0, 0), Rect(self.x, self.y, 16, 16), 1)
    
    def draw(self):
        window.blit(self.image, (self.x, self.y))
    
    def logic(self):
        self.update()
        self.draw()
        self.touch_area()

bullet_list = []


all_enemy = []





class Enemy:
    def __init__(self, width, height, x, y, speed):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed
        self.image = transform.scale(image.load(r'C:\Users\028\Downloads\game\sprites\enemy.png').convert_alpha(), (self.width, self.height))
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.hp = 1
        all_enemy.append(self)
        self.dmg = 1

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x
        if self.x < 0 or self.hp < 1:
            all_enemy.remove(self)

        for self in all_enemy:
            if self.rect.colliderect(hero.rect):
                all_enemy.remove(self)
                hero.hp -= self.dmg
        
    
    def touch_area(self):
        draw.rect(window, (255, 0, 0), Rect(self.x, self.y, self.width, self.height), 1)
    
    def draw(self):
        window.blit(self.image, (self.x, self.y))
    
    def logic(self):
        self.update()
        self.draw()
        self.touch_area()
enemy_flag = True



boss_flag = False
class Boss1:
    def __init__(self, width, height, x, y, speed):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed
        self.image = transform.scale(image.load(r'C:\Users\028\Downloads\game\sprites\boss1.png').convert_alpha(), (self.width, self.height))
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.hp = 5
        all_enemy.append(self)
        boss_list.append(self)
        self.dmg = 999

    def update(self):
        global boss_flag
        self.x -= self.speed
        self.rect.x = self.x
        if self.x < 0 or self.hp < 1:
            all_enemy.remove(self) 
            boss_list.remove(self) 
            boss_flag = False
        elif self.rect.colliderect(hero.rect):
            all_enemy.remove(self) 
            boss_list.remove(self) 
            boss_flag = False
            hero.hp -= self.dmg
    def hp_bar(self):
        draw.line(window, (255, 0, 0), (self.x, self.y - 10), ((self.x + (self.width/5)*self.hp), self.y - 10), width=5)    
        
    
    def touch_area(self):
        draw.rect(window, (255, 0, 0), Rect(self.x, self.y, self.width, self.height), 1)
    
    def draw(self):
        window.blit(self.image, (self.x, self.y))
    
    def logic(self):
        self.hp_bar()
        self.update()
        self.draw()
        self.touch_area()
boss1_list = []




class Boss2:
    def __init__(self, width, height, x, y, speed):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed
        self.image = transform.scale(image.load(r'C:\Users\028\Downloads\game\sprites\boss2.png').convert_alpha(), (self.width, self.height))
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.hp = 15
        all_enemy.append(self)
        boss_list.append(self)
        self.move_left = True
        self.move_right = False
        self.dmg = 999
        self.flag = True

        

    def update(self):
        global drop_flag
        self.rect.x = self.x
        if self.move_left:
            self.x -= self.speed

        elif self.move_right:
            self.x += self.speed
        
        # движение влево-вправо
        if self.x < window_w/2 or self.x > window_w + 100:
            self.move_left, self.move_right = self.move_right, self.move_left

        if self.x < 0 or self.hp < 1:
            all_enemy.remove(self) 
            boss_list.remove(self)
            self.flag = False

        elif self.rect.colliderect(hero.rect):
            all_enemy.remove(self) 
            boss_list.remove(self) 
            hero.hp -= self.dmg
            self.flag = False
    # полоска здоровья красная
    def hp_bar(self):
        draw.line(window, (255, 0, 0), (self.x, self.y - 10), ((self.x + (self.width/15)*self.hp), self.y - 10), width=5)
    
    def touch_area(self):
        draw.rect(window, (255, 0, 0), Rect(self.x, self.y, self.width, self.height), 1)
    
    def draw(self):
        window.blit(self.image, (self.x, self.y))
    
    def logic(self):

        self.hp_bar()
        self.update()
        self.draw()
        self.touch_area()
boss_list = []

drop_flag = False
class Drop:
    def __init__(self):
        self.width = 32
        self.height = 32
        self.x = randint(0, window_w)
        self.y = 0 - self.height
        self.speed = 4
        self.image = transform.scale(image.load(r'C:\Users\028\Downloads\game\sprites\drop.png').convert_alpha(), (self.width, self.height))
        self.rect = Rect(self.x, self.y, self.width, self.height)
        drop_list.append(self)
        all_enemy.append(self)
        self.dmg = 1


    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        if self.y + self.height > window_h:
            drop_list.remove(self)
            all_enemy.remove(self)
        if self.rect.colliderect(hero.rect):
            drop_list.remove(self)
            all_enemy.remove(self)
            hero.hp -= self.dmg

    def touch_area(self):
        draw.rect(window, (255, 0, 0), Rect(self.x, self.y, self.width, self.height), 1)
    
    def draw(self):
        window.blit(self.image, (self.x, self.y))
    
    def logic(self):
        self.update()
        self.draw()
        self.touch_area()
drop_list = []


