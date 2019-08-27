import pygame
from board import Board
from chess_rules import ChessRules
from chess_ai import ChessAI 
from player import Player 

import os
import sys

# start_positions = [['B_rook','B_knight','B_bishop','B_queen','B_king','B_bishop','B_knight','B_rook'],
# 					   ['B_pawn']*8,
# 					   [0]*8,
# 					   [0]*8,
# 					   [0]*8,
# 					   [0]*8,
# 					   ['W_pawn']*8,
# 					   ['W_rook','W_knight','W_bishop','W_queen','W_king','W_bishop','W_knight','W_rook']]

YELLOW = (255,255,0)
RED = (255,0,0)
BLACK = (0,0,0)

data_path = 'data/'

WIDTH = 800
HEIGHT = 800

pygame.init()

class GUI:

	def __init__(self):
		# TODO: Check square size
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		self.clock = pygame.time.Clock()
		self.square_size = WIDTH//8
		self.caption = pygame.display.set_caption('Chess by Caff V0.1')
		self.background = pygame.image.load(os.path.join(data_path, 'chessboard.png'))
		self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
		self.running = True
		self.state = 'start'

		self.rules = ChessRules()
		self.human = Player()
		self.ai = ChessAI()
		self.board = Board()


		self.load_pieces()
		self.update_board()
		
		self.from_piece = None
		self.to_piece = None
		
	

	def load_pieces(self):
		# load piece images
		for piece in os.listdir(os.path.join(data_path, 'pieces')):
			piece_image = pygame.image.load(os.path.join(data_path + 'pieces/', piece))
			setattr(self, piece[0], piece_image)

	def update_board(self):
		self.screen.blit(self.background, [0, 0])
		b = self.square_size//4 # set the buffersize for each square
		for col in range(8):
			for row in range(8):
				if self.board.board[col][row].isalpha():
					piece = getattr(self, self.board.board[col][row])
					self.screen.blit(piece, (row*self.square_size+b, col*self.square_size+b))
		pygame.display.update()

	def run(self):	
		while self.running:
			if self.state == 'start':
				self.start_events()
				self.start_draw()
			elif self.state == 'playing':
				self.playing_events()
				self.update_board()
			else:
				self.running = False
	
			self.clock.tick(30)
		pygame.quit()
		sys.exit()

	def start_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				self.state = 'playing'

	def start_draw(self):
		self.screen.fill(BLACK)
		font = pygame.font.SysFont('arial black', 50)
		text = font.render('PUSH SPACE BAR TO START', False, YELLOW)
		# center text
		text_size = text.get_size()
		x = WIDTH//2 - text_size[0]//2
		y = HEIGHT//2 - text_size[1]//2
		self.screen.blit(text, (x, y))
		pygame.display.update()


	def playing_events(self):
		# initialize from/to coords as zeroes

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				from_x,from_y = pygame.mouse.get_pos()
				self.from_piece = (from_x, from_y)
			elif event.type == pygame.MOUSEBUTTONUP:
				to_x,to_y = pygame.mouse.get_pos()
				self.to_piece = (to_x, to_y)


			if self.from_piece and self.to_piece:
				# We divide by square size to change from number of pixels to rows/cols
				# and reverse as rules board is cols/row
				from_square = [i//self.square_size for i in self.from_piece[::-1]]
				to_square = [i//self.square_size for i in self.to_piece[::-1]]
				print(from_square, to_square)
				if self.rules.is_valid_move(from_square, to_square, self.board.board, 'White'):
					print("Move piece, from and to:", from_square, to_square)
					self.board.move_piece(from_square, to_square)
					self.update_board()
					if self.rules.is_check(self.board.board, 'White'):
						if self.rules.is_checkmate(self.board.board, 'White'):
							print("Checkmate!")
							self.running = False
						print("Check")
					# reset to and from piece variables
					self.from_piece = None
					self.to_piece = None

					# AI to make move
					AI_move = self.ai.depth_search(self.board.board, 'Black', 3)
					print(AI_move)
					self.board.move_piece(AI_move[0], AI_move[1])
					self.board.print_board()
			# if event.type == pygame.MOUSEMOTION:
			# 	rel_x = event.rel[0]
			# 	rel_y = event.rel[1]
			# 	# print(rel_x, rel_y)
	def move_piece(self):
		# TODO: Will be silmilar to playing_draw, combine?
		pass

	def playing_draw(self):
		pass

	


if __name__ == '__main__':


	gui = GUI()
	gui.run()


	
	

