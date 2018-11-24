import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('hi')

clock = pygame.time.Clock()
crashed = False

black = (0,0,0)
white = (255,255,255)
playerImg = pygame.image.load('player.png')

def player(x,y):
	gameDisplay.blit(playerImg, (x,y))

x = display_width*.45
y = display_height*.8
vx = 0
vy = 0
ax = 0
ay = 0

leftKey = pygame.K_a
rightKey = pygame.K_d
upKey = pygame.K_w
downKey = pygame.K_s
friction = .25
horacc = .3
terminalv = 3
floorv = .2
veracc = horacc

keysPressed = [0,0,0,0] #W, A, S, D (or up, left, down, right)

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

				
	
		#print(event)
	
	ax = 0
	ay = 0
	if keysPressed[1] == 1:
		ax -= horacc
	if keysPressed[3] == 1:
		ax += horacc
	if keysPressed[0] == 1:
		ay -= veracc
	if keysPressed[2] == 1:
		ay += veracc
	
	vx += ax
	vy += ay
	
	#implement fiction
	if vx > 0: ax -= friction
	if vx < 0: ax += friction
	if vy > 0: ay -= friction
	if vy < 0: ay += friction
	
	vx += ax
	vy += ay
	
	if vx > terminalv: vx = terminalv
	if vx < -terminalv: vx = -terminalv
	if vy > terminalv: vy = terminalv
	if vy < - terminalv: vy = -terminalv
	
	#floor velocity
	if abs(vx) < floorv: vx = 0
	if abs(vy) < floorv: vy = 0
	
	x += vx
	y += vy
	
	gameDisplay.fill(white)
	player(x,y)
	
	pygame.display.update()
	clock.tick(60)
	
pygame.quit()
quit()