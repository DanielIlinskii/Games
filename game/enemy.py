from pygame import *


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
        for i in range(self.hp):
            window.blit(self.heart, (100 + i*50, 50))
        self.rect.x = self.x
        self.rect.y = self.y
    
    def logic(self):
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
                bullet_list.remove(self)
                enemy.hp -= self.damage

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

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x
        if self.x < 0 or self.hp < 1:
            all_enemy.remove(self)

        for self in all_enemy:
            if self.rect.colliderect(hero.rect):
                all_enemy.remove(self)
                # hero.hp -= 1
        
    
    def touch_area(self):
        draw.rect(window, (255, 0, 0), Rect(self.x, self.y, self.width, self.height), 1)
    
    def draw(self):
        window.blit(self.image, (self.x, self.y))
    
    def logic(self):
        self.update()
        self.draw()
        self.touch_area()
enemy_flag = True



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
        boss1_list.append(self)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x
        if self.x < 0 or self.hp < 1:
            all_enemy.remove(self) 
            boss1_list.remove(self) 
        
        
    
    def touch_area(self):
        draw.rect(window, (255, 0, 0), Rect(self.x, self.y, self.width, self.height), 1)
    
    def draw(self):
        window.blit(self.image, (self.x, self.y))
    
    def logic(self):
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
        boss2_list.append(self)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x
        if self.x < 0 or self.hp < 1:
            all_enemy.remove(self) 
            boss2_list.remove(self) 
    
    def touch_area(self):
        draw.rect(window, (255, 0, 0), Rect(self.x, self.y, self.width, self.height), 1)
    
    def draw(self):
        window.blit(self.image, (self.x, self.y))
    
    def logic(self):
        self.update()
        self.draw()
        self.touch_area()
boss2_list = []
