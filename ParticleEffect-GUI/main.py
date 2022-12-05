import pygame 
from random import randint, choice, uniform

from button import Button
from particleEffect import ParticleEffect
from settings import *

pygame.init()

screen = pygame.display.set_mode((screen_w, screen_h))

# ''' clock object -- handles FPS '''
clock = pygame.time.Clock()

# ''' create particle effect object '''
particleEffect = ParticleEffect()

# ''' get a numpy list of particles '''
particles = particleEffect.particles

# ''' create buttons '''
regular_button = Button(150, screen_h//2 + button_gap_h, "particles spraying")
gravity_button = Button(150, screen_h//2, "particle gravity effect")
usemouse_button = Button(150, screen_h//2 + button_gap_h*2, "use mouse")
shoot_button = Button(150, screen_h//2 + button_gap_h*3, "shoot")

# ''' main method '''
def main():
	running = True 

	# ''' GUI LOOP '''
	while running: 

		# ''' black background '''
		screen.fill(black)

		# ''' update buttons '''
		gravity_button.update(screen)
		regular_button.update(screen)
		usemouse_button.update(screen)
		shoot_button.update(screen)

		# ''' event handler '''
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				running = False

			# ''' manipulate particle gravity '''
			elif event.type == pygame.KEYDOWN: 
				if event.key == pygame.K_ESCAPE:
					particleEffect.reset()
				elif event.key == pygame.K_UP:
					particleEffect.set_gravity(-0.03)
				elif event.key == pygame.K_DOWN: 
					particleEffect.set_gravity(0.03)
				elif event.key == pygame.K_SPACE: 
					particleEffect.can_shoot = True

			# ''' button clicks '''
			elif event.type == pygame.MOUSEBUTTONDOWN:	
				if gravity_button.rect.collidepoint((event.pos[0], event.pos[1])):
					particleEffect.set_type('gravity')
				elif regular_button.rect.collidepoint((event.pos[0], event.pos[1])):
					particleEffect.set_type('default')
				elif usemouse_button.rect.collidepoint((event.pos[0], event.pos[1])):
					particleEffect.set_type('mouse')
				elif shoot_button.rect.collidepoint((event.pos[0], event.pos[1])):
					particleEffect.set_type('shoot')

		# ''' update particleEffect engine '''
		particleEffect.update(screen)

		# ''' update screen '''
		pygame.display.update()
		clock.tick(FPS)

	pygame.quit()


if __name__ == "__main__":
	main()