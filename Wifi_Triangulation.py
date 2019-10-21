import math
import pygame
import random
from pygame.locals import *
from collections import namedtuple

pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((1600,900))

class Block(object):
    sprite = pygame.image.load("dirt.png").convert_alpha()
    
    def __init__(self, x, y):
        self.rect = self.sprite.get_rect(centery=y, centerx=x)
        self.x = x
        self.y = y

class Player(object):
    sprite = pygame.image.load("dirt1.png").convert()
    sprite.set_colorkey((0,255,0))
    def __init__(self, x, y):
        self.rect = self.sprite.get_rect(centery=y, centerx=x)
        self.x = x
        self.y = y
        self.xvel = 0
        self.yvel = 0
        self.move_speed = 8

    def update(self, move, blocks):
        if move.left: 
            self.xvel = -self.move_speed
            
        if move.right: 
            self.xvel = self.move_speed
            
        if move.up: 
            self.yvel = -self.move_speed
            
        if move.down: 
            self.yvel = self.move_speed
            
        if not (move.left or move.right):
            self.xvel = 0
        
        if not (move.up or move.down):
            self.yvel = 0

        self.rect.left += self.xvel
        
        self.rect.top += self.yvel
        
        self.x += self.xvel
        self.y += self.yvel
        

blocklist = []
player = []
colliding = False
Move = namedtuple('Move', ['up', 'down', 'left', 'right'])
while True:
    screen.fill((25,30,90))
    mse = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT: exit()

        if key[K_LSHIFT]:
            if event.type==MOUSEMOTION:
                if not any(block.rect.collidepoint(mse) for block in blocklist):
                    x=(int(mse[0]) / 32)*32
                    y=(int(mse[1]) / 32)*32
                    blocklist.append(Block(x+16,y+16))
                
        else:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    to_remove = [b for b in blocklist if b.rect.collidepoint(mse)]
                    for b in to_remove:
                        blocklist.remove(b)

                    if not to_remove:
                        x=(int(mse[0]) / 32)*32
                        y=(int(mse[1]) / 32)*32
                        blocklist.append(Block(x+16,y+16))

                elif event.button == 3:
                    x=(int(mse[0]) / 32)*32
                    y=(int(mse[1]) / 32)*32
                    player=[]
                    player.append(Player(x+16,y+16))

    move = Move(key[K_UP], key[K_DOWN], key[K_LEFT], key[K_RIGHT])
    
    
    for b in blocklist:      
        screen.blit(b.sprite, b.rect)
    


    for p in player:
        for b in blocklist:
            radius = math.sqrt((p.x-b.x)**2+(p.y-b.y)**2)
            pygame.draw.circle(screen, (0,0,0), (int(b.x),int(b.y)),int(radius),1)
            
        p.update(move, blocklist)
        screen.blit(p.sprite, p.rect)
    
    clock.tick(60)
    pygame.display.flip()

