from chess_rules import ChessRules
from player import Player
from board import Board

import copy


class ChessAI:

	def __init__(self, color='Black'):
		self.rules = ChessRules()
		self.color = color

	def minimax(self, board, color, depth):
		my_move = (0, 0)
		if depth == 1:
			return self.get_evaluation(board)

		moves = self.get_all_possible_moves(board, color)

		for move in moves:
			testboard = self.get_testboard(move[0], move[1], board)
			if color == 'Black':
				best_reply = self.minimax(testboard, 'White', depth=depth-1)
			else:
				best_reply = self.minimax(testboard, 'Black', depth=depth-1)
			print("best reply", best_reply)
			if type(best_reply) == tuple:
				if my_move is None or my_move[1] < -best_reply[1]:
					my_move = move, -best_reply[1]
			else:
				if my_move is None or my_move[1] < -best_reply:
					my_move = move, -best_reply
		print("My move", my_move)
		return my_move

		
	def get_evaluation(self, board):
		# scans through rows and cols and counts value of pieces
		evaluation = 0
		for i in range(8):
			for j in range(8):
				evaluation += evaluation +self.get_piece_value(board[i][j])
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
			return 30
		elif piece == 'k':
			return -30


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

	def get_best_move(self, board, color='Black'):
		pass

	def get_all_possible_moves(self, board, color):
		all_valid_moves = []

		if color == 'White':
			for i in range(8):
				for j in range(8):
					if board[i][j].isupper():
						all_valid_moves.extend(rules.list_valid_moves((i,j), board, color))
		if color == 'Black':
			for i in range(8):
				for j in range(8):
					if board[i][j].islower():
						all_valid_moves.extend(rules.list_valid_moves((i,j), board, color))
		return all_valid_moves




if __name__ == '__main__':
	# player1 is human for debugging
	player1 = Player()
	player2 = ChessAI()

	rules = ChessRules()
	board = Board()
	color = 'White'

	while True:
		board.print_board()
		if color == 'White':
			from_square, to_square = input("Print please enter the position you would like to move from then to.\n").split()

			if not rules.is_valid_move(from_square, to_square, board.board, color):
				print("Sorry that is not a valid move.")
			else:
				board.move_piece(from_square, to_square)
				color = 'Black'
		
		move = player2.minimax(board.board, color, 2)
		print(move)
		board.move_piece(move[0][0], move[0][1])
		color = 'White'

