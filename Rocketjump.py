#Мой первый коммит
from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, rect_x, rect_y, player_height, player_width):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
score = 0
lost = 0
finish = 0
class Enemy(GameSprite):
    def update(self):
        global lost
        if self.rect.y < 500:
            
            self.rect.y += self.speed
        else:
            self.rect.y = 0
            self.rect.x = randint(0, 650)
            lost = lost + 1
font.init()
font1 = font.Font(None, 36)
font.init()
font2 = font.Font(None, 80)


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
        if key_pressed[K_d] and self.rect.x < 630:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png",  15, self.rect.centerx, self.rect.top, 20, 15)
        bullets.add(bullet)                

win_width = 700
bullets = sprite.Group()
monsters = sprite.Group()
player = Player("rocket.png", 10, 350, 400, 100, 80)
for i in range(5):
    monster = Enemy("ufo.png", randint(1, 5), randint(80, win_width - 80), -40, 50, 80)
    monsters.add(monster)
window = display.set_mode((700, 500))
display.set_caption("Ракета")
collides = sprite.groupcollide(monsters, bullets, True, True)
background = transform.scale(image.load("galaxy.jpg"),(700, 500))
clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
fire_sound = mixer.Sound("fire.ogg")
win = font2.render("YOU WINED", True, (0, 225, 0))
lose = font2.render("YOU LOSE", True, (225, 0, 0))
game = True
finish = False
while game:
    window.blit(background,(0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
        
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                player.fire()

    text1 = font1.render("Счёт:" + str(lost), 1, (225, 225, 225))
    text = font1.render("Пропущенно:" + str(lost), 1, (225, 225, 225))    

        
    window.blit(text1, (0,0))
    window.blit(text, (0,50))

    
    bullets.update()
    bullets.draw(window)

    monsters.update()
    monsters.draw(window)
    player.reset()
    player.update()
    for c in collides:
        score = score + 1
        monster = Enemy("ufo.png", randint(1, 5), randint(80, win_width - 80), -40, 50, 80)
        monsters.add(monster)

        if lost == 3 or sprite.spritecollide(player, monsters, False):
            lost == False  
        window.blit(lose, (230,250))
    clock.tick(FPS)
    display.update()
