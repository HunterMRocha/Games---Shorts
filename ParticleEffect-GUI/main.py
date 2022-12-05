import pygame 
from random import randint, choice, uniform

from button import Button
from particleEffect import ParticleEffect
from settings import *

pygame.init()

screen = pygame.display.set_mode((screen_w, screen_h))

clock = pygame.time.Clock()

particleEffect = ParticleEffect()
particles = particleEffect.particles

regular_button = Button(150, screen_h//2 + button_gap_h, "particles spraying")
gravity_button = Button(150, screen_h//2, "particle gravity effect")
usemouse_button = Button(150, screen_h//2 + button_gap_h*2, "use mouse")
shoot_button = Button(150, screen_h//2 + button_gap_h*3, "shoot")


def main():
	running = True 
	while running: 

		screen.fill(black)

		gravity_button.update(screen)
		regular_button.update(screen)
		usemouse_button.update(screen)
		shoot_button.update(screen)

		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				running = False

			elif event.type == pygame.KEYDOWN: 
				if event.key == pygame.K_ESCAPE:
					particleEffect.reset()
				elif event.key == pygame.K_UP:
					particleEffect.set_gravity(-0.03)
				elif event.key == pygame.K_DOWN: 
					particleEffect.set_gravity(0.03)
				elif event.key == pygame.K_SPACE: 
					particleEffect.can_shoot = True
				
			elif event.type == pygame.MOUSEBUTTONDOWN:
				# check gravity button click
				if gravity_button.rect.collidepoint((event.pos[0], event.pos[1])):
					particleEffect.set_type('gravity')
				
				# check regular button click
				elif regular_button.rect.collidepoint((event.pos[0], event.pos[1])):
					particleEffect.set_type('default')

				# use mouse to move the particle
				elif usemouse_button.rect.collidepoint((event.pos[0], event.pos[1])):
					particleEffect.set_type('mouse')

				# use space bar to shoot particles
				elif shoot_button.rect.collidepoint((event.pos[0], event.pos[1])):
					particleEffect.set_type('shoot')
			
			
		particleEffect.update(screen)


		pygame.display.update()
		clock.tick(FPS)

	pygame.quit()


main()