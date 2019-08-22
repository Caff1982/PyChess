import pygame


class ChessRules:
	def __init__(self):
		self.board =  [['r','n','b','q','k','b','n','r'],
					   ['p','p','p','p','p','p','p','p'],
					   ['0']*8,
					   ['0']*8,
					   ['0']*8,
					   ['0']*8,
					   ['P','P','P','P','P','P','P','P'],
					   ['R','N','B','Q','K','B','N','R']]

		self.empty_space = '0'
		self.white_rook = 'R'
		self.white_knight = 'N'
		self.white_bishop = 'B'
		self.white_queen = 'Q'
		self.white_king = 'K'
		self.white_pawn = 'P'
		self.black_rook = 'r'
		self.black_knight = 'k'
		self.black_bishop = 'b'
		self.black_queen = 'q'
		self.black_king = 'k'
		self.black_pawn = 'p'

	def print_board(self):
		print('    0    1    2    3    4    5    6    7')
		for i, row in enumerate(self.board):
			print(i, row)

	def move_piece(self, from_square, to_square):
		from_row = int(from_square[0])
		from_col = int(from_square[1])
		to_row = int(to_square[0])
		to_col = int(to_square[1])
		piece = self.board[from_row][from_col]
		self.board[from_row][from_col] = '0'
		if self.board[to_row][to_col] == '0':
			self.board[to_row][to_col] = piece
		else:
			print("Taken piece! ", self.board[to_row][to_col])
			self.board[to_row][to_col] = piece

	def is_clear_path(self, from_row, from_col, to_row, to_col):
		# Base case, if only moving one square path is clear
		
		if abs(from_row-to_row) <= 1 and abs(from_col-to_col) <= 1:
			return True
		else:
			if from_col == to_col and from_row < to_row: # rows+
				from_row +=1
			elif from_col == to_col and from_row > to_row: # rows-
				from_row -=1
			elif from_row == to_row and from_col < to_col: # cols+
				from_col +=1
			elif from_row == to_row and from_col > to_col: # cols-
				from_col -=1
			elif from_row < to_row and from_col < to_col: # diag SE
				from_row +=1
				from_col +=1
			elif from_row < to_row and from_col > to_col: # diag NE
				from_row +=1
				from_col -=1
			elif from_row > to_row and from_col > to_col: # diag NW
				from_row -=1
				from_col -=1
			elif from_row > to_row and from_col < to_col: # diag SW
				from_row -=1
				from_col +=1

		if self.board[from_row][from_col] != '0':
			return False
		else:
			return self.is_clear_path(from_row, from_col, to_row, to_col)

	def is_valid_move(self, from_square, to_square, player):
		from_row = int(from_square[0])
		from_col = int(from_square[1])
		to_row = int(to_square[0])
		to_col = int(to_square[1])
		from_piece = self.board[from_row][from_col]
		to_piece = self.board[to_row][to_col]

		if from_square == to_square:
			return False

		if from_piece == 'P':
			# normal move forward
			if to_row == from_row-1 and to_col == from_col and to_piece == '0':
				return True
			# move two squares at start
			elif to_row == from_row-2 and to_col == from_col and to_piece == '0' and from_row == 6: 
				if self.is_clear_path(from_row, from_col, to_row, to_col):
					return True
			# move diagonally to take
			elif to_row == from_row-1 and (to_col== from_col+1 or to_col == from_col-1) and to_piece.is_lower():
				return True

		elif from_piece == 'p': # black pawn
			if to_row == from_row+1 and to_col == from_col and to_piece == '0':
				return True
			elif to_row == from_row+2 and to_col == from_col and to_piece == '0' and from_row == 1: 
				if self.is_clear_path(from_row, from_col, to_row, to_col):
					return True
			elif to_row == from_row+1 and (to_col == from_col+1 or to_col == from_col-1) and to_piece.isupper():
				return True

		elif from_piece == 'R':
			if (from_row == to_row or from_col == to_col) and (to_piece == '0' or to_piece.islower()):
				if self.is_clear_path(from_row, from_col, to_row, to_col):
					return True
		elif from_piece == 'r':
			if (from_row == to_row or from_col == to_col) and (to_piece == '0' or to_piece.isupper()):
				if self.is_clear_path(from_row, from_col, to_row, to_col):
					return True

		elif from_piece == 'B':
			if abs(to_row - from_row) == abs(to_col - from_col) and (to_piece == '0' or to_piece.islower()):
				if self.is_clear_path(from_row, from_col, to_row, to_col):
					return True
		elif from_piece == 'b':
			if abs(to_row - from_row) == abs(to_col - from_col) and (to_piece == '0' or to_piece.isupper()):
				if self.is_clear_path(from_row, from_col, to_row, to_col):
					return True

		elif from_piece == 'n':
			if from_col-2 == to_col and (to_row == from_row+1 or to_row == from_row-1) and (to_piece == '0' or to_piece.isupper()):
				return True
			elif from_col+2 == to_col and (to_row == from_row+1 or to_row == from_row-1):
				return True
			elif from_row+2 == to_row and (to_col == from_col+1 or to_col == from_col-1):
				return True
			elif from_row-2 == to_row and (to_col == from_col+1 or to_col == from_col-1):
				return True
		elif from_piece == 'N':
			if from_col-2 == to_col and (to_row == from_row+1 or to_row == from_row-1) and (to_piece == '0' or to_piece.islower()):
				return True
			elif from_col+2 == to_col and (to_row == from_row+1 or to_row == from_row-1):
				return True
			elif from_row+2 == to_row and (to_col == from_col+1 or to_col == from_col-1):
				return True
			elif from_row-2 == to_row and (to_col == from_col+1 or to_col == from_col-1):
				return True

		elif from_piece == 'q':
			if (from_row == to_row or from_col == to_col) and (to_piece == '0' or to_piece.isupper()):
				if self.is_clear_path(from_row, from_col, to_row, to_col):
					return True
			elif abs(to_row - from_row) == abs(to_col - from_col) and (to_piece == '0' or to_piece.isupper()):
				if self.is_clear_path(from_row, from_col, to_row, to_col):
					return True
		elif from_piece == 'Q':
			if (from_row == to_row or from_col) == to_col and (to_piece == '0' or to_piece.islower()):
				if self.is_clear_path(from_row, from_col, to_row, to_col):
					return True
			elif abs(to_row - from_row) == abs(to_col - from_col) and (to_piece == '0' or to_piece.islower()):
				if self.is_clear_path(from_row, from_col, to_row, to_col):
					return True

		elif from_piece == 'k':
			if abs(from_row-to_row) <=1 and abs(from_col-to_col) <=1 and (to_piece == '0' or to_piece.isupper()):
				return True
		elif from_piece == 'K':
			if abs(from_row-to_row) <=1 and abs(from_col-to_col) <=1 and (to_piece == '0' or to_piece.islower()):
				return True

		return False

	def is_check(self, player):
		# First find player's king square
		if player == 'White':
			for i in range(8):
				for j in range(8):
					if self.board[i][j] == 'K':
						king_square = (i, j)
						break
		elif player == 'Black':
			for i in range(8):
				for j in range(8):
					if self.board[i][j] == 'k':
						king_square = (i, j)
						break

		if player == 'White':		
				for i in range(8):
					for j in range(8):
						if self.board[i][j].islower():
							if self.is_valid_move((i, j), king_square, 'Black'):
								return True
		if player == 'Black':		
				for i in range(8):
					for j in range(8):
						if not self.board[i][j].islower():
							if self.is_valid_move((i, j), king_square, 'White'):
								return True

	def is_checkmate(self, player):
		all_valid_moves = []
		if player == 'White':
			for i in range(8):
				for j in range(8):
					if self.board[i][j].islower():
						all_valid_moves.extend(list_valid_moves(((i,j), player)))
		if len(all_valid_moves) == 0:
			return True
		else:
			return False

	def list_valid_moves(self, from_square, player):
		#returns a list of moves as tuples in tuples
		valid_moves = []
		for i in range(8):
			for j in range(8):
				if self.is_valid_move(from_square, (i,j), player):
					valid_moves.append((from_square, (i, j)))
		return valid_moves

# if __name__ == '__main__':
# 	game = ChessRules()
# 	player = 'White'

# 	while True:
# 		game.print_board()

# 		if game.is_check(player):
# 			if game.is_checkmate():
# 				print("Checkmate!")
# 			else:
# 				print("Check!")

# 		print(player, 'player:')
# 		from_square = tuple(input("Which piece would you like to move? (Please give row and col ie: 73 is White Queen)\n"))
# 		to_square = tuple(input("Which square would you like to move to?\n"))

# 		if game.is_valid_move(from_square, to_square, player):
# 			game.move_piece(from_square, to_square)

# 			if player == 'White':
# 				player = 'Black'
# 			else:
# 				player = 'White'
# 		else:
# 			print("Invalid move please try again")



