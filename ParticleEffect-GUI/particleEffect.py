# import pygame 
import numpy as np
from random import randint
from particle import Particle

class ParticleEffect: 
	can_shoot = False
	def __init__(self, p_type='default', count=400): 
		self.x, self.y = (450, 300)
		self.count = count
		self.particles = []
		self.type = p_type
		self.fill()
		self.len = len(self.particles)
		self.gravity = 0.02


	''' method used to fill numpy list with particles '''
	def fill(self): 
		for i in range(self.count):
			# particle attributes
			pos = [randint(440, 445), randint(300, 305)]
			velocity_xy = [randint(0, 20) / 10 - 1, 2]
			time = randint(5, 8)

			# create and add particle
			new_particle = Particle(pos, velocity_xy, time, self.type)
			self.particles.append(new_particle)

	def reset(self): 
		if self.type == 'shoot':
			self.can_shoot = True
		else: 
			self.can_shoot = False

		self.particles.clear()
		self.gravity = 0.02
		self.fill()

	def get_particle(self):
		return Particle([self.x, self.y], [randint(0, 20) / 10 - 1, 2],  randint(10, 15), self.type)

	def set_gravity(self, force):
		Particle.gravity += force

	def set_type(self, p_type): 
		self.type = p_type
		self.reset()

	def update(self, screen): 
		if self.len <= self.count:
			new_particle = self.get_particle()
			self.particles.append(new_particle)
		
		if self.type != 'shoot':
			for particle in self.particles[::]:
				particle.update(screen, self)
		else: 
			for particle in self.particles[::]:
				particle.shoot(screen)

			
