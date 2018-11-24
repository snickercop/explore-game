import pygame

class Fist(pygame.sprite.DirtySprite):
	def __init__(self):
		pygame.sprite.DirtySprite.__init__(self)
	
class Chimp(pygame.sprite.DirtySprite):
	def __init__(self):
		pygame.sprite.DirtySprite.__init__(self)

# set up screen		
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('chimp')

#set up clock and crashed
clock = pygame.time.Clock()
crashed = False

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
	
	pygame.display.update()
	clock.tick(30)