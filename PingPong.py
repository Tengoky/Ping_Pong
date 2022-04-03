#Создай собственный Шутер
from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self,img,speed=10,x=400,y=200,w=65,h=65):
        super().__init__()
        self.image =  transform.scale(image.load(img),(65,65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))  

    def draw(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    
class Ball(GameSprite):
    def move(self):
        pass
    
            
class Racket(GameSprite):
    def move1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0  :
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height-70 :
            self.rect.y += self.speed
    def move2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0  :
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height-70 :
            self.rect.y += self.speed



win_widht = 800
win_height = 400
window = display.set_mode((win_widht,win_height))
display.set_caption('Пинг Понг')
#задай фон сцены
window.fill((40, 153, 17))
'''score = 0
lost = 0'''
ball = Ball('ball.png')
racket1 = Racket('r.png',10,735,200,65,65)
racket2 = Racket('r2.png',10,5,200,65,65)
mixer.init()
mixer.music.load('musicbg.ogg')
hit_sound = mixer.Sound('ping.ogg')

mixer.music.play()
game = True
#finish = False
clock = time.Clock()
FPS = 60
stop = False
'''end = False
tstart = font.render(
    'START', True, (0,0,0)
)
quit = font.render(
    'QUIT', True, (0,0,0)
)'''
while game:
#обработай событие «клик по кнопке "Закрыть окно"» 
    for e in event.get():
        if e.type == QUIT:
            game = False 
    window.fill((40, 153, 17))
    ball.draw()
    racket1.draw()
    racket1.move1()
    racket2.draw() 
    racket2.move2()    
    display.update()
    clock.tick(FPS)


















