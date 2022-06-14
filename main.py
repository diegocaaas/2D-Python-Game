import pygame
from sys import exit
import random

pygame.init()

WIDTH,HEIGHT = 800, 400
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Escape from Shronah")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('character.png').convert_alpha(), [75,125])
        self.rect = self.image.get_rect(midbottom = (200,300))
        self.gravity = 0
        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    def update(self):
        self.player_input()
        self.apply_gravity()

player = pygame.sprite.GroupSingle()
player.add(Player())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('white')
    player.draw(screen)
    player.update()
    
    pygame.display.update()
    clock.tick(60)
