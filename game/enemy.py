from pygame import *
from initial_setting import *


init()

window_w = 1200
window_h = 700

window = display.set_mode((window_w, window_h))



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

    
    def touch_area(self):
        draw.rect(window, (255, 0, 0), Rect(self.x, self.y, self.width, self.height), 1)
    
    def draw(self):
        window.blit(self.image, (self.x, self.y))
        self.rect.x = self.x
        self.rect.y = self.y
    
    def logic(self):
        for enemy in small_enemy_list:
            if enemy.rect.colliderect(self.rect):
                small_enemy_list.remove(enemy)






class Enemy:
    def __init__(self, width, height, x, y, speed):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed
        self.image = transform.scale(image.load(r'C:\Users\028\Downloads\game\sprites\enemy.png').convert_alpha(), (self.width, self.height))
        self.rect = Rect(self.x, self.y, self.width, self.height)
        small_enemy_list.append(self)
    
    def update(self):
        self.x -= self.speed
        self.rect.x = self.x
        if self.x < 0:
            small_enemy_list.remove(self)
        
    
    def touch_area(self):
        draw.rect(window, (255, 0, 0), Rect(self.x, self.y, self.width, self.height), 1)
    
    def draw(self):
        window.blit(self.image, (self.x, self.y))
    
    def logic(self):
        self.update()
        self.draw()
        self.touch_area()


hero = Hero(48, 48, 15, 200, 10)
small_enemy_list = []
