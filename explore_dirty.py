import pygame
import math
import csv

WATER = 0
DIRT = 1
GRASS = 2

GREEN = (0,255,0)

display_width = 800
display_height = 600

x = display_width*.45
y = display_height*.8
playerSize = 20

all_sprites = pygame.sprite.Group()
map_sprites = pygame.sprite.Group()

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

def loadMap(map):
	for row in range(0, len(map)):
		for tileIn in range(0, len(map[0])):
			tile = map[row][tileIn]
			if int(tile) < 2:
				x = tileIn * tileSize
				y = row * tileSize
				map_sprites.add(Tile(int(tile), x, y))


def getCurrentTile(x, y):
	row = math.floor(y/tileSize)
	col = math.floor(x/tileSize)
	return map[row][column]

xspeed = 4
yspeed = xspeed
dspeed = xspeed*.75

leftKey = pygame.K_a
rightKey = pygame.K_d
upKey = pygame.K_w
downKey = pygame.K_s


keysPressed = [0,0,0,0] #W, A, S, D (or up, left, down, right)

class Tile(pygame.sprite.DirtySprite):
	def __init__(self, terrainID, x, y):
		pygame.sprite.DirtySprite.__init__(self)
		self.image = tileset[terrainID]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.dirty = 0
		self.defaultImage = self.image

class Player(pygame.sprite.DirtySprite):
	def __init__(self):
		pygame.sprite.DirtySprite.__init__(self)
		self.image = pygame.image.load('player.png')
		self.rect = self.image.get_rect()
		self.vx = 0
		self.vy = 0
		self.lastC = Tile(0,0,0)
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
			self.rect.y = display_height-playerSizewd
		if self.rect.y < 0:
			self.rect.y = 0
		self.dirty = 1
		
		# collision detection
		collideSpriteList = pygame.sprite.spritecollide(self, map_sprites, False, collided = None)
		if(collideSpriteList): #if there was a collision
			collideSprite = collideSpriteList[int(len(collideSpriteList)/2)]
			collideX = collideSprite.rect.x
			collideY = collideSprite.rect.y
			collideSprite.image = tileset[2]
			collisionBuffer = playerSize
			if self.rect.x in range(collideX-collisionBuffer, collideX+2*collisionBuffer):
				self.rect.y -= self.vy
			if self.rect.y in range(collideY-collisionBuffer, collideY+2*collisionBuffer):
				self.rect.x -= self.vx
			self.lastC = collideSprite
		else:
			self.lastC.image = self.lastC.defaultImage
			
		

player = Player()

all_sprites.add(player)

	
loadMap(currentmap)

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
	
	screen.fill(GREEN)

	
	all_sprites.update()
	map_sprites.draw(screen)
	all_sprites.draw(screen)
	
	pygame.display.update()
	clock.tick(30)
	
pygame.quit()
quit()