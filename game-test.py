import pygame

def main():
	pygame.init()
	screen = pygame.display.set_mode((700,400))
	screen.fill((10,10,10))


	pygame.draw.circle(screen, (255, 255, 255), (350,200), 10)

	surff = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)	
	screen.blit(surff, (0,0))
	pygame.display.update()
