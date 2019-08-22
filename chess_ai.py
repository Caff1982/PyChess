from chess_rules import ChessRules 
from player import Player


class ChessAI:

	def __init__(self, color='Black'):
		self.rules = ChessRules()
		self.color = color

	def minimax(self, depth, board, color):
		if depth == 1:
			return self.get_best_move(self, board, color)

		moves = self.get_all_possible_moves()
		for move in moves:
			test = board.copy()
			test.move_piece(move[0], move[1])
			print(test)


	def get_best_move(self, board, color='Black'):
		pass

	def get_all_possible_moves(self, color='Black'):
		all_valid_moves = []
		if color == 'Black':
			for i in range(8):
				for j in range(8):
					if self.rules.board[i][j].islower():
						all_valid_moves.extend(rules.list_valid_moves((i,j), color))
		elif color == 'White':
			pass # TODO
		return all_valid_moves






if __name__ == '__main__':
	# player1 is human for debugging
	player1 = Player()
	player2 = ChessAI()

	rules = ChessRules()
	board = rules.board
	player = 'White'

	while True:
		rules.print_board()
		if player == 'White':
			from_square, to_square = input("Print please enter the position you would like to move from then to.\n").split()

			if not rules.is_valid_move(from_square, to_square, player):
				print("Sorry that is not a valid move.")
			else:
				rules.move_piece(from_square, to_square)
				player = 'Black'
		else:
			player2.minimax(2, board, player)

			player = 'White'

