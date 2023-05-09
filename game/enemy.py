from pygame import *


init()

window_w = 1200
window_h = 700

window = display.set_mode((window_w, window_h))
display.set_caption("Ghost")

class Sprite:
    def __init__(self, filename, width, height, x, y, speed):
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(filename).convert_alpha(), (self.width, self.height))

        self.x = x
        self.y = y
        self.speed = speed
        self.rect = Rect(self.x, self.y, self.width, self.height)

    def touch_area(self):
        draw.rect(window, (255, 0, 0), Rect(self.x, self.y, self.width, self.height), 0)

    def reset(self):
        window.blit(self.image, (self.x, self.y))


class Hero(Sprite):

    def __init__(self, filename, width, height, x, y, speed):
        super().__init__(filename, width, height, x, y, speed)
        self.jump = False
        self.j_count = 10
    
    def update(self):
        pass



bg = Sprite(r'C:\Users\028\Downloads\game\sprites\background.jpg', window_w, window_h, 0, 0, 1)
bg1 = Sprite(r'C:\Users\028\Downloads\game\sprites\background.jpg', window_w, window_h, bg.width, 0, 1)


small_enemy = Sprite(r"C:\Users\028\Downloads\game\sprites\enemy.png", 48, 48, 820, 160, 2) # small enemy

hero = Hero(r'C:\Users\028\Downloads\game\sprites\walk1.png', 48, 48, 15, 200, 10) # main person



exit()
