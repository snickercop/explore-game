import pygame
import math
import csv

WATER = 0
DIRT = 1
GRASS = 2

display_width = 800
display_height = 600

x = display_width*.45
y = display_height*.8
playerSize = 20

tileset = {0:pygame.image.load('water.png'), 1:pygame.image.load('dirt.png'), 2:pygame.image.load('grass.png')}

pygame.init()

with open('explore_map.csv', 'r') as f:
    reader = csv.reader(f)
    currentmap = list(reader)


screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('explore!')

clock = pygame.time.Clock()
crashed = False

black = (0,0,0)
tileSize = 20
white = (255,255,255)
playerImg = pygame.image.load('player.png')

def player(x,y):
	screen.blit(playerImg, (x,y))
	
def drawTile(tile, x, y):
	screen.blit(tileset[tile], (x,y))

def drawMap(map):
	for row in range(0, len(map)):
		for tileIn in range(0, len(map[0])):
			tile = map[row][tileIn]
			x = tileIn * tileSize
			y = row * tileSize
			drawTile(int(tile), x, y)

def getCurrentTile(x, y):
	row = math.floor(y/tileSize)
	col = math.floor(x/tileSize)
	return map[row][column]

xspeed = 4
yspeed = xspeed
dspeed = math.sqrt(xspeed)

leftKey = pygame.K_a
rightKey = pygame.K_d
upKey = pygame.K_w
downKey = pygame.K_s


keysPressed = [0,0,0,0] #W, A, S, D (or up, left, down, right)


class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('player.png')
		self.rect = self.image.get_rect()
		self.vx = 0
		self.vy = 0
	def update(self):
		self.vx = 0
		self.vy = 0
		if keysPressed[1] == 1:
			self.vx -= xspeed
		if keysPressed[3] == 1:
			self.vx += xspeed
		if keysPressed[0] == 1:
			self.vy -= yspeed
		if keysPressed[2] == 1:
			self.vy += yspeed
		
		if sum(keysPressed) == 2:
			if self.vx != 0 and self.vy != 0:
				if self.vx > 0:
					self.vx = dspeed
				else:
					self.vx = -dspeed
				if self.vy > 0:
					self.vy = dspeed
				else:
					self.vy = -dspeed
		

	
		self.rect.x += self.vx
		self.rect.y += self.vy
	
		#set back player if he has crossed a screen boundary
		if self.rect.x > display_width-playerSize:
			self.rect.x = display_width-playerSize
		if self.rect.x < 0:
			self.rect.x = 0
		if self.rect.y > display_height-playerSize:
			self.rect.y = display_height-playerSize
		if self.rect.y < 0:
			self.rect.y = 0

player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
		if event.type == pygame.KEYUP:
			if event.key == leftKey:
				keysPressed[1] = 0
			if event.key == rightKey:
				keysPressed[3] = 0
			if event.key == upKey:
				keysPressed[0] = 0
			if event.key == downKey:
				keysPressed[2] = 0
		if event.type == pygame.KEYDOWN:
			if event.key == leftKey:
				keysPressed[1] = 1
			if event.key == rightKey:
				keysPressed[3] = 1
			if event.key == upKey:
				keysPressed[0] = 1
			if event.key == downKey:
				keysPressed[2] = 1
	
	drawMap(currentmap)
	
	all_sprites.update()
	all_sprites.draw(screen)
	
	pygame.display.update()
	clock.tick(30)
	
pygame.quit()
quit()