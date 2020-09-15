#!/usr/bin/python
import pygame
from pygame.locals import *
import numpy as np

# Constants
screen_width = 1280
screen_height = 720

# Colors
yellow = (250,250,5)

# define main character class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.algo == ''


def main():
    pygame.init()
    # load and set the logo
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    
    mainsurface = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("4 elements")

    show_start_screen(surface=mainsurface)


def show_start_screen(surface):
	"""Show main menu: initial animation + buttons: 
	new game, load game, options, exit"""

	showing_main_menu = True
	
	# Calculate layout grid
	left_grid_x = screen_width//3
	mayor_grid_y = [i*(screen_height/3) for i in (1,2,3)]
	midcenter, bottomcenter = np.mean(mayor_grid_y[:2]), np.mean(mayor_grid_y[1:])
	space_for_buttons = (bottomcenter - midcenter)/4
	starts = [midcenter + i*space_for_buttons for i in range(4)]	

	# Draw buttons
	new_game = pygame.draw.rect(surface, yellow, (left_grid_x, starts[0], left_grid_x, space_for_buttons-10), 0)
	load_game = pygame.draw.rect(surface, yellow, (left_grid_x, starts[1], left_grid_x, space_for_buttons-10), 0)
	options = pygame.draw.rect(surface, yellow, (left_grid_x, starts[2], left_grid_x, space_for_buttons-10), 0)
	exit = pygame.draw.rect(surface, yellow, (left_grid_x, starts[3], left_grid_x, space_for_buttons-10), 0)

	# Draw text in buttons
	main_font = pygame.font.Font('Elementary_Gothic_Scaled.ttf', 20)
	new_game_surface = main_font.render('New game', True, (0,0,0,0))
	load_game_surface = main_font.render('Load game', True, (0,0,0,0))
	options_surface = main_font.render('Options', True, (0,0,0,0))
	exit_surface = main_font.render('Exit', True, (0,0,0,0))

	# Align centers
	new_game_rect = new_game_surface.get_rect()
	new_game_rect.center = new_game.center
	load_game_rect = load_game_surface.get_rect()
	load_game_rect.center = load_game.center
	options_rect = options_surface.get_rect()
	options_rect.center = options.center
	exit_rect = exit_surface.get_rect()
	exit_rect.center = exit.center

	# Blit text in buttons
	surface.blit(new_game_surface, new_game_rect)
	surface.blit(load_game_surface, load_game_rect)
	surface.blit(options_surface, options_rect)
	surface.blit(exit_surface, exit_rect)
	
	pygame.display.update()

    # main loop
	while showing_main_menu:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				showing_main_menu = False
				pygame.quit()
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				mouseClicked = True

def run_game(level=1):
	pass

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__": main()
