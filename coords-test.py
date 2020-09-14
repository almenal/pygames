#!/usr/bin/python

# Load modules
import numpy as np
import sys, pygame
from pygame.locals import *

screen_dimensions = 500,500
colors = [(255,0,0), (0,255,0), (0,0,255)]

def main():
	"""Main function"""
	fps = 10
	pygame.init()
	fpsClock = pygame.time.Clock()

	mainsurface = pygame.display.set_mode(screen_dimensions)
	mainsurface.fill((0,0,0))
	pygame.display.set_caption('Coords test')
	
	color_id = 0
	x = 0
	y = 0

	game_running = True
	while game_running:
		
		for ev in pygame.event.get():
			if ev.type == QUIT:
				game_running = False

		if x == screen_dimensions[0]:
			x = 0
			y += 20
		
		color = colors[color_id % 3]
		pygame.draw.rect(mainsurface, color, ((x,y), (20,20)))

		# Font object
		fontObj = pygame.font.Font('freesansbold.ttf', 8)
		textSurfaceObj = fontObj.render(str(str(x) + ',' + str(y)), True, (255,255,255))
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (x + 10, y + 10)

		mainsurface.blit(textSurfaceObj, textRectObj)
		
		color_id += 1 
		x += 20

		pygame.display.update()
		fpsClock.tick(fps)

	pygame.quit()


if __name__ == '__main__': main()



