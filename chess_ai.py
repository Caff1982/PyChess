from chess_rules import ChessRules
from player import Player
from board import Board
from piece_tables import *

import time
import random


class ChessAI:

	def __init__(self, color='Black'):
		# color set to black for debugging
		self.rules = ChessRules()
		self.color = color

	def get_best_move(self, board, is_maximizing, depth):
		best_move = -99999
		best_move_final = None

		for move in self.get_possible_moves(board, 'Black'):
			testboard = board.get_testboard(move[0], move[1], board)
		
			value = max(best_move, self.minimax(testboard, float('-inf'), float('inf'), not is_maximizing, depth-1))
			if value > best_move:
				if not self.rules.is_check(testboard, 'Black'):
					print('Best score', best_move)
					print('Best move:', best_move_final)
					best_move = value
					best_move_final = move

		return best_move_final

	def minimax(self, board, alpha, beta, is_maximizing, depth):
		# set base case
		if depth == 0:
			return -self.get_evaluation(board.board)

		moves = self.get_all_possible_moves(board)
		
		if is_maximizing:
			best_move = -99999
			for move in moves:
				testboard = board.get_testboard(move[0], move[1], board)
				best_move = max(best_move, self.minimax(testboard, alpha, beta, not is_maximizing, depth-1))
				alpha = max(alpha, best_move)
				if beta <= alpha:
					return best_move
			return best_move
		else:
			best_move = 99999
			for move in moves:
				testboard = board.get_testboard(move[0], move[1], board)
				best_move = min(best_move, self.minimax(testboard, alpha, beta, not is_maximizing, depth-1))
				beta = min(beta, best_move)
				if beta <= alpha:
					return best_move
			return best_move

	def get_board_value(self, board, piece_type, table):
		# TODO: Should this be in a transposition tables class?
		white = 0
		black = 0
		for i in range(8):
			for j in range(8):
				piece = board[i][j]
				if piece == piece_type.lower():
					if piece.isupper():
						white += table[i][j]
					else:
						black += table[i][j]
		return white - black

	def get_evaluation(self, board):
		# scans through rows and cols and counts value of pieces
		evaluation = 0
		# get heuristic values of board first 
		evaluation += self.get_board_value(board, 'p', PAWN_TABLE)
		evaluation += self.get_board_value(board, 'n', KNIGHT_TABLE)
		evaluation += self.get_board_value(board, 'b', BISHOP_TABLE)
		evaluation += self.get_board_value(board, 'r', ROOK_TABLE)
		evaluation += self.get_board_value(board, 'q', QUEEN_TABLE)
		evaluation += self.get_board_value(board, 'k', KING_TABLE)

		for i in range(8):
			for j in range(8):
				evaluation += self.get_piece_value(board[i][j])
		return evaluation

	def get_piece_value(self, piece):
		if piece == '0':
			return 0
		elif piece == 'P':
			return 100
		elif piece == 'p':
			return -100
		elif piece == 'N':
			return 300
		elif piece == 'n':
			return -300
		elif piece == 'B':
			return 300
		elif piece == 'b':
			return -300
		elif piece == 'R':
			return 500
		elif piece == 'r':
			return -500
		elif piece == 'Q':
			return 900
		elif piece == 'q':
			return -900
		elif piece == 'K':
			return 9000
		elif piece == 'k':
			return -9000
			
	def get_possible_moves(self, board, color):
		moves = []
		# if color == 'White':
		# 	for i in range(8):
		# 		for j in range(8):
		# 			if board.board[i][j].isupper():
		# 				moves.extend(self.rules.list_valid_moves((i,j), board, color))
		if color == 'Black':
			for i in range(8):
				for j in range(8):
					if board.board[i][j].islower():
						moves.extend(self.rules.list_valid_moves((i,j), board, color))
		return moves

	def get_all_possible_moves(self, board):
		moves = []
		for i in range(8):
			for j in range(8):
				if board.board[i][j].isupper():
					moves.extend(self.rules.list_valid_moves((i,j), board, 'white'))
		for i in range(8):
			for j in range(8):
				if board.board[i][j].islower():
					moves.extend(self.rules.list_valid_moves((i,j), board, 'black'))
		return moves




# if __name__ == '__main__':
# 	# player1 is human for debugging
# 	player1 = Player()
# 	player2 = ChessAI()

# 	rules = ChessRules()
# 	board = Board()
# 	color = 'White'

# 	while True:
# 		board.print_board()
# 		if color == 'White':
# 			from_square, to_square = input("Print please enter the position you would like to move from then to.\n").split()

# 			if not rules.is_valid_move(from_square, to_square, board.board, color):
# 				print("Sorry that is not a valid move.")
# 			else:
# 				board.move_piece(from_square, to_square)
# 				if rules.is_check(board.board, color):
# 					print("Check!")
# 				elif rules.is_checkmate(board.board, color):
# 					print("Checkmate!")
# 				color = 'Black'
# 		else:
# 			start = time.time()
# 			move = player2.depth_search(board.board, color, 3)
# 			end = time.time()
# 			if rules.is_check(board.board, color):
# 				print("Check!")
# 			elif rules.is_checkmate(board.board, color):
# 					print("Checkmate!")	
# 			print("Move:", move)
# 			print("Time", end - start)
# 			board.move_piece(move[0][0], move[0][1])
# 			color = 'White'
