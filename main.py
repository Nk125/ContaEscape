import pygame
from classes.const import const as Constants
from classes.controller import controller as Control

#milliClock = pygame.time.Clock()

screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))

controller = Control()

screen.fill((0, 0, 0))

pygame.display.set_caption("ContaEscape")

running = True
while running:
	screen.blit(controller.surf, controller.rect)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN:
			keyPressed = event.key
			
			if keyPressed == pygame.K_DOWN:
				controller.update(controller.states.DOWN)

			elif keyPressed == pygame.K_RIGHT:
				controller.update(controller.states.RIGHT)

			elif keyPressed == pygame.K_UP:
				controller.update(controller.states.UP)

			elif keyPressed == pygame.K_LEFT:
				controller.update(controller.states.LEFT)

		if event.type == Constants.RESET_CONTROLLER:
			controller.update(controller.states.NONE)

	pygame.display.update()

pygame.init()