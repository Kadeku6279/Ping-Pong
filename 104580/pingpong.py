from pygame import *
window = display.set_mode((500,500))
display.set_caption("Пинг-понг")

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,p_size_x,p_size_y, player_speed):
        super().__init__()
        self.size_x = p_size_x
        self.size_y = p_size_y
        self.image = transform.scale(image.load(player_image),(self.size_x,self.size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.y = player_y
        self.rect.x = player_x

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed

light_blue = (51, 220, 255)
window.fill(light_blue)

wall_right = Player("wall.png",30,250,10,100,0.5)
wall_left = Player("wall.png",470,250,10,100,0.5)
ball = GameSprite('',100,100,100,100)

FPS = 60
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    if finish != True:
        window.fill(light_blue)
        ball.reset()
        wall_left.reset()
        wall_right.reset()
        wall_left.update_l()
        wall_right.update_r()
        
    
    display.update()
