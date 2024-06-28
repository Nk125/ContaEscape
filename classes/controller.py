from pygame import sprite, locals, time
import pygame.image as PGImage
from enum import Enum
from os import path
from classes.image import image
from classes.const import const as Constants

class controller(sprite.Sprite):
	class states(Enum):
		LEFT = "left"
		RIGHT = "right"
		UP = "up"
		DOWN = "down"
		NONE = ""

	pathPrefix = path.join(image.pathPrefix, "controller")

	def __init__(self):
		super(controller, self).__init__()
		self.update()
		self.surf.set_colorkey((255, 255, 255), locals.RLEACCEL)
		self.rect = self.surf.get_rect(
			center = (
				abs(Constants.WIDTH - 50), abs(Constants.HEIGHT - 50)
			)
		)
	
	def update(self, direction : states = states.NONE) -> None:
		self.surf = PGImage.load(
			path.join(path.dirname(path.abspath(__file__)), self.pathPrefix, f"steamdeck_dpad_{direction}{image.pathSuffix}")
		).convert()

		if direction != self.states.NONE:
			time.set_timer(Constants.RESET_CONTROLLER, 80, 1)