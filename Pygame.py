'''
Pygame.py
Pygame study
From http://programarcadegames.com/python_examples/f.php?file=pygame_base_template.py
Base skeleton for pygame modules
'''
import pygame
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size) # Note the useage of pygame.display.  This creates a surface object
pygame.display.set_caption("My game")
done = False # Loop until close button is clicked
clock = pygame.time.Clock() # Manages screen objects
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill(WHITE)
	pygame.display.flip()
	clock.tick(60)
pygame.quit()