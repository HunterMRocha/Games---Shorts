import pygame
from settings import *

class Button: 
	def __init__(self, x, y, text=''):
		# button stuff
		self.x = x
		self.y = y
		self.text = text
		self.width = button_width
		self.height = button_height
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		self.rect.center = (self.x, self.y)

		# text stuff 
		self.font = pygame.font.Font(font, 20)
		self.text = self.font.render(self.text, True, white)
		self.text_rect = self.text.get_rect()
		self.text_rect.center = self.rect.center

	def draw(self, screen): 
		pygame.draw.rect(screen, red, self.rect)
		screen.blit(self.text, self.text_rect)

	def update(self, screen): 
		self.draw(screen)