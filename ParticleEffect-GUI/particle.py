import pygame
from settings import *
from random import uniform	

class Particle: 
	gravity = 0.02


	''' loc-(location) timer-(lifespan) velocity and a type-(id) 
	the particles 'type' is what indicates each particles responsibility or action. '''
	def __init__(self, loc, velocity, timer, p_type): 
		pygame.init()
		self.velocity = velocity
		self.timer = timer
		self.type = p_type

		''' particle's location is the cursor's (x,y) if particle type is "mouse",
		otherwise loc is determined as a parameter '''
		self.loc = loc if p_type != 'mouse' else self.get_mouse_pos()

		''' 90% white - 10% red '''
		self.color = white if uniform(0,1) < 0.9 else red


	''' getter for mouse(x,y) '''
	def get_mouse_pos(self): 
		return [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]]

	''' setter for particle type '''
	def set_type(self, type): 
		self.type = type
	
	''' default: decrease particle y by 1 '''
	def shoot(self, screen): 
		self.loc[1] -= 1
		
	''' draw particle method -- size of particle and lifespan are relative '''
	def draw(self, screen):	

		pygame.draw.circle(screen, self.color, self.loc, self.timer)

	''' update method, handles all particle responsibility -- called every frame'''
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
