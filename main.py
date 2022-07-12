import pygame 
from sys import exit
from random import randint,choice




class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('char.png').convert_alpha()
        self.rect = self.image.get_rect(center = (130,130))
        self.gravity = 0
        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 375:
            self.gravity = -20
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 375:
            self.rect.bottom = 375
    def update(self):
        self.player_input()
        self.apply_gravity()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type): 
        super().__init__()

        if type == 'car':
            self.image = pygame.image.load("car.png").convert_alpha()
            y_pos = 370 
        else:
            self.image = pygame.image.load("plane.png").convert_alpha()
            y_pos = 275 
        self.rect = self.image.get_rect(center = (randint(900,1100), y_pos) )
    def update(self):
        self.rect.x -= 6
        self.destroy()
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def collision():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        obstacle_group.empty()
        return False
    else:
        return True

pygame.init()

WIDTH,HEIGHT = 800, 400
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Escape from Shronah")
clock = pygame.time.Clock()
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,900)

player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()

background = pygame.transform.scale(pygame.image.load('background.jpg').convert_alpha(), [WIDTH,HEIGHT])
screen.blit(background,(0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == obstacle_timer:
            obstacle_group.add(Obstacle(choice(['car', 'car', 'car', 'plane']))) 
    
    active = collision()
    if not active:
        break;
    
    screen.blit(background,(0,0))
    player.draw(screen)
    player.update()

    obstacle_group.draw(screen)
    obstacle_group.update()

    pygame.display.update()
    clock.tick(60) 
pygame.quit()
