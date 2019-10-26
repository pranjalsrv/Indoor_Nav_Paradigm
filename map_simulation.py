import pygame,random
from pygame.locals import *
from collections import namedtuple

pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((640,480))

class Block(object):
    sprite = pygame.image.load("dirt.png").convert_alpha()
    def __init__(self, x, y):
        self.rect = self.sprite.get_rect(centery=y, centerx=x)

class Player(object):
    sprite = pygame.image.load("dirt1.png").convert()
    sprite.set_colorkey((0,255,0))
    def __init__(self, x, y):
        self.rect = self.sprite.get_rect(centery=y, centerx=x)
        self.xvel = 0
        self.yvel = 0
        self.move_speed = 8

    def update(self, move, blocks):
        # simple left/right movement
        if move.left: self.xvel = -self.move_speed
        if move.right: self.xvel = self.move_speed

        # simple up/down movement
        if move.up: self.yvel = -self.move_speed
        if move.down: self.yvel = self.move_speed

        # if no left/right movement, x speed is 0, of course
        if not (move.left or move.right):
            self.xvel = 0
        
        # if no up/down movement, y speed is 0, of course
        if not (move.up or move.down):
            self.yvel = 0

        # move horizontal, and check for horizontal collisions
        self.rect.left += self.xvel
        self.collide(self.xvel, 0, blocks)

        # move vertically, and check for vertical collisions
        self.rect.top += self.yvel
        self.collide(0, self.yvel, blocks)

    def collide(self, xvel, yvel, blocks):
        for block in [blocks[i] for i in self.rect.collidelistall(blocks)]:

            # if xvel is > 0, we know our right side bumped 
            # into the left side of a block etc.
            if xvel > 0: self.rect.right = block.rect.left
            if xvel < 0: self.rect.left = block.rect.right

            # if yvel > 0, we are falling, so if a collision happpens 
            # we know we hit the ground (remember, we seperated checking for
            # horizontal and vertical collision, so if yvel != 0, xvel is 0)
            if yvel > 0:
                self.rect.bottom = block.rect.top
                self.yvel = 0
            # if yvel < 0 and a collision occurs, we bumped our head
            # on a block above us
            if yvel < 0: self.rect.top = block.rect.bottom

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
        p.update(move, blocklist)
        screen.blit(p.sprite, p.rect)
    clock.tick(60)
    pygame.display.flip()
