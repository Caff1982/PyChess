from chess_rules import ChessRules
from player import Player
from board import Board

import copy
import time
import random

class ChessAI:

	def __init__(self, color='Black'):
		# color set to black for debugging
		self.rules = ChessRules()
		self.color = color

	def depth_search(self, board, color, depth):
		# my_move = None, 0
		best_move = -99999
		best_move_final = None
		moves = self.get_possible_moves(board, color)
		if color == 'Black':
			is_maximizing = True
		else:
			is_maximizing = False

		for move in moves:
			testboard = self.get_testboard(move[0], move[1], board)
			# if color == 'Black':
			# 	best_reply = -1000000
			# 	best_reply = self.minimax(testboard, float('-inf'), float('inf'), depth=depth-1, False)
			# else:
			# 	best_reply = 1000000
			# 	best_reply = self.minimax(testboard, float('inf'), float('-inf'),depth=depth-1, True)
			
			value = max(best_move, self.minimax(testboard, float('-inf'), float('inf'), not is_maximizing, depth=depth-1))
			if value > best_move:
				print('Best score', best_move)
				print('Best move:', best_move_final)
				best_move = value
				best_move_final = move

		return best_move_final

		# 	# DEBUGGING
		# 	print(move, best_reply)
		# 	# b = Board(testboard)
		# 	# b.print_board()
		# 	if my_move[1] < -best_reply and not self.rules.is_check(testboard, color):
		# 		my_move = move, -best_reply
		# # if no best move found return last move checked
		# if my_move[0] is not None:
		# 	return my_move
		# if not self.rules.is_check(testboard, color):
		# 	return move, 0
		# else:
		# 	print("Checkmate!")
		# 	return my_move


	def minimax(self, board, alpha, beta, is_maximizing, depth):
		# set base case
		if depth == 0:
			return -self.get_evaluation(board)
		# shuffle moves to add randomness
		moves = self.get_all_possible_moves(board)
		
		if is_maximizing:
			best_move = -99999
			for move in moves:
				testboard = self.get_testboard(move[0], move[1], board)
				best_move = max(best_move, self.minimax(testboard, alpha, beta, not is_maximizing, depth=depth-1))
				alpha = max(alpha, best_move)
				if beta <= alpha:
					return best_move
			return best_move
		else:
			best_move = 99999
			for move in moves:
				testboard = self.get_testboard(move[0], move[1], board)
				best_move = min(best_move, self.minimax(testboard, alpha, beta, not is_maximizing, depth=depth-1))
				beta = min(beta, best_move)
				if beta <= alpha:
					return best_move
			return best_move

	def get_evaluation(self, board):
		# scans through rows and cols and counts value of pieces
		evaluation = 0
		for i in range(8):
			for j in range(8):
				evaluation += self.get_piece_value(board[i][j])
		return evaluation

	def get_piece_value(self, piece):
		if piece == '0':
			return 0
		elif piece == 'P':
			return 1
		elif piece == 'p':
			return -1
		elif piece == 'N':
			return 3
		elif piece == 'n':
			return -3
		elif piece == 'B':
			return 3
		elif piece == 'b':
			return -3
		elif piece == 'R':
			return 5
		elif piece == 'r':
			return -5
		elif piece == 'Q':
			return 9
		elif piece == 'q':
			return -9
		elif piece == 'K':
			return 90
		elif piece == 'k':
			return -90
			
	def get_possible_moves(self, board, color):
		moves = []
		if color == 'White':
			for i in range(8):
				for j in range(8):
					if board[i][j].isupper():
						moves.extend(self.rules.list_valid_moves((i,j), board, color))
		if color == 'Black':
			for i in range(8):
				for j in range(8):
					if board[i][j].islower():
						moves.extend(self.rules.list_valid_moves((i,j), board, color))
		return moves

	def get_all_possible_moves(self, board):
		moves = []
		for i in range(8):
			for j in range(8):
				if board[i][j].isupper():
					moves.extend(self.rules.list_valid_moves((i,j), board, 'white'))
		for i in range(8):
			for j in range(8):
				if board[i][j].islower():
					moves.extend(self.rules.list_valid_moves((i,j), board, 'black'))
		return moves


	def get_testboard(self, from_square, to_square, board):
		testboard = copy.deepcopy(board)
		from_row = from_square[0]
		from_col = from_square[1]
		to_row = to_square[0]
		to_col = to_square[1]
		piece = board[from_row][from_col]
		testboard[from_row][from_col] = '0'
		testboard[to_row][to_col] = piece
		return testboard

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
