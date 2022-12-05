import pygame
from settings import *
from random import uniform	

class Particle: 
	gravity = 0.02
	
	def __init__(self, loc, velocity, timer, p_type): 
		pygame.init()
		self.velocity = velocity
		self.timer = timer
		self.type = p_type
		self.loc = loc if p_type != 'mouse' else self.get_mouse_pos()

		self.color = white if uniform(0,1) < 0.9 else red

	def get_mouse_pos(self): 
		return [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]]

	def set_type(self, type): 
		self.type = type
	
	def shoot(self, screen): 
		self.loc[1] -= 1
		
	def draw(self, screen):	
		pygame.draw.circle(screen, self.color, self.loc, self.timer)


	def update(self, screen, PE): 
		# draw the particle
		self.draw(screen)
		
		# move the particle
	
		self.loc[0] += self.velocity[0]
		self.loc[1] -= self.velocity[1]
		
		# update particle size/timer
		self.timer -= 0.08

		# check types
		if self.type == 'gravity':
			self.velocity[1] -= self.gravity

		elif self.type == 'shoot': 
			self.velocity[0] -= self.velocity[0]
			self.velocity[1] -= self.gravity
