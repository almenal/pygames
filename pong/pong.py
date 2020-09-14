#!/usr/bin/python

# Load modules
import numpy as np
import sys, pygame
from pygame.locals import *

# Constants & Global variables
screen_dimensions = 700,400
box_dimensions = (15, 75) # Width, height
score = {'Player1':0, 'Player2':0}
white = 255,255,255
black = 0,0,0
background = 50,50,50

class Ball(pygame.sprite.Sprite):
	def __init__(self, *groups):
		super().__init__(*groups)
		self.surf = pygame.Surface((15,15)).convert_alpha()
		self.surf.fill((0,0,0,0))
		self.rect = pygame.draw.rect(self.surf, white, (0,0,15,15), 0)
		self.pos = (screen_dimensions[0]//2, screen_dimensions[1]//2)
		self.dir = np.random.uniform(-2*np.pi, 2*np.pi)
		self.speed = 5.0
		self.touched_bar = False

	def move(self):
		self.pos = (self.pos[0] + self.speed * np.cos(self.dir),
				  self.pos[1] + self.speed * np.sin(self.dir))
		self.rect.center = (self.pos[0], self.pos[1])
		self.speed += .15
		if self.speed >= 25:
			self.speed = 25
	
	def restart(self):
		self.pos = (screen_dimensions[0]//2, screen_dimensions[1]//2)
		self.dir = np.random.uniform(-2*np.pi, 2*np.pi)
		self.speed = 5.0

class Bar(pygame.sprite.Sprite):
	def __init__(self, *groups):
		super().__init__(*groups)
		self.surf = pygame.Surface(box_dimensions)
		self.rect = pygame.draw.rect(self.surf, white, ((0,0), box_dimensions))
		self.is_running = False


	def moveup(self):
		self.rect.y -= 20
		if self.rect.top <= 20:
			self.rect.top = 20
		
	def movedown(self):
		self.rect.y += 20
		if self.rect.bottom >= screen_dimensions[1]:
			self.rect.y = screen_dimensions[1] - box_dimensions[1]
		



def main():
	"""Main function"""
	fps = 30
	pygame.init()
	fpsClock = pygame.time.Clock()
	
#	global mainsurface
	mainsurface = pygame.display.set_mode(screen_dimensions)
	mainsurface.fill(background)
	pygame.display.set_caption('Pong')

	# run_game()

	ball = Ball()
	bar1 = Bar()
	bar2 = Bar()
	bar1.rect.centerx = 20
	bar2.rect.centerx = screen_dimensions[0] - 20

	global fontObj
	fontObj = pygame.font.Font('SFAlienEncountersSolid.ttf', 20) # Font object for score
	
	game_running = True
	while game_running:
		"""1. Event handling
		2. Update game state (points)
		3. Draw frame"""

		# 1. Event handling
		for ev in pygame.event.get():
			if ev.type == QUIT:
				game_running = False
			elif ev.type == KEYDOWN and ev.key == K_w:
				bar1.is_running = 'up'
			elif ev.type == KEYDOWN and ev.key == K_s:
				bar1.is_running = 'down'
			elif ev.type == KEYUP and (ev.key == K_w or ev.key == K_s):
				bar1.is_running = False
			if ev.type == KEYDOWN and ev.key == K_UP:
				bar2.is_running = 'up'
			elif ev.type == KEYDOWN and ev.key == K_DOWN:
				bar2.is_running = 'down'
			elif ev.type == KEYUP and (ev.key == K_UP or ev.key == K_DOWN):
				bar2.is_running = False
			if ev.type == KEYDOWN and ev.key == K_r:
				ball.restart()
				score['Player1'] = 0
				score['Player2'] = 0
			if ev.type == KEYDOWN and ev.key == K_b:
				ball.restart()

			if ev.type == KEYDOWN and ev.key == K_ESCAPE:
				pause_game(surface=mainsurface)


		# 2. Update game state
		# Move bar according to barX.is_running state
		if bar1.is_running:
			if bar1.is_running == 'up':
				bar1.moveup()
			elif bar1.is_running == 'down':
				bar1.movedown()
		if bar2.is_running:
			if bar2.is_running == 'up':
				bar2.moveup()
			elif bar2.is_running == 'down':
				bar2.movedown()
		
		ball.move()

		# Is the ball hitting a wall? -> bounce
		if ball.rect.top <= 0 or ball.rect.bottom >= screen_dimensions[1]:
			ball.dir = -ball.dir

		# Is the ball touching a bar? -> bounce
		if ball.touched_bar:
			ball.touched_bar = False

		if pygame.sprite.collide_rect(ball, bar1) and not ball.touched_bar:
			ball.touched_bar = True
			# ball.rect.x += 50
			ball.dir = np.random.uniform(np.pi/3, -np.pi/3)
		if pygame.sprite.collide_rect(ball, bar2) and not ball.touched_bar:
			ball.touched_bar = True
			# ball.rect.x -= 50
			ball.dir = np.random.uniform(2*np.pi/3, 4*np.pi/3)
			
		if ball.rect.centerx <= 0:
			score['Player2'] += 1
			ball.restart()
		if ball.rect.centerx >= screen_dimensions[0]:
			score['Player1'] += 1
			ball.restart()

		# 3. Draw
		# Display score
		score_text = 'Player 1: ' + str(score['Player1']) + ' '*15 + 'Player 2: ' + str(score['Player2'])
		score_surface = fontObj.render(score_text, True, (255,255,255))
		score_rect = score_surface.get_rect()
		score_rect.center = (screen_dimensions[0]//2, 10)

		# Draw background, grid & score
		mainsurface.fill(background)
		draw_grid(surface=mainsurface)
		mainsurface.blit(score_surface, score_rect)

		# Draw sprites
		mainsurface.blit(bar1.surf, bar1.rect.topleft)
		mainsurface.blit(bar2.surf, bar2.rect.topleft)
		mainsurface.blit(ball.surf, ball.rect.topleft)

		# Draw frame
		pygame.display.update()
		fpsClock.tick(fps)

	pygame.quit()

def pause_game(surface):

	score_surface = fontObj.render('PAUSE', True, (255,255,255))
	score_rect = score_surface.get_rect()
	score_rect.center = (screen_dimensions[0]//2, screen_dimensions[1]//2 - 60)
	surface.blit(score_surface, score_rect)

	pygame.draw.rect(surface, white, (screen_dimensions[0]//2 - 60, screen_dimensions[1]//2 - 40, 40, 120), 0)	
	pygame.draw.rect(surface, white, (screen_dimensions[0]//2 + 20, screen_dimensions[1]//2 - 40, 40, 120), 0)
	pygame.display.update()
	game_paused = True
	while game_paused:
		for ev in pygame.event.get():
			if ev.type == QUIT:
				pygame.quit()
			elif ev.type == KEYDOWN and ev.key == K_ESCAPE:
				game_paused = False

def draw_grid(surface):
	pygame.draw.line(surface, white, (0,17), (screen_dimensions[0], 17), 2)	
	x_midscreen = screen_dimensions[0]//2
	start_points = [i*10 for i in range(400//10) if i%3==0]
	for y in start_points:
		pygame.draw.line(surface, white, (x_midscreen, y), (x_midscreen, y+10), 4)

if __name__ == '__main__': main()
