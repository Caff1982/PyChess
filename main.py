import pygame
import os

pygame.init()
pygame.font.init()

display_width = 900
display_height = 900

size = (display_width, display_height)
screen = pygame.display.set_mode(size)

clock_tick_rate = 20

data_path = 'data/'

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Chess by Caff V0.1')

background_image = pygame.image.load(os.path.join(data_path, 'chessboard.jpg'))
background_image = pygame.transform.scale(background_image, (900, 900))

clock = pygame.time.Clock()

class State():
	def __init__(self):
		# TODO: Check square size
		self.square_size = 50
		self.load_pieces

	def load_pieces(self):
		for piece in os.listdir(os.path.join(data_path, 'pieces')):
			piece_name = piece[:-3]		
			self.piece_name = pygame.image.load(os.path.join(data_path + 'pieces/', piece))



if __name__ == '__main__':
	gui = GUI()
	gui.get_board_grid()
	gui.load_pieces()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		screen.blit(background_image, [0, 0])


		pygame.display.update()
		clock.tick(clock_tick_rate)

		