from board import Board


class ChessRules:

	def is_clear_path(self, from_row, from_col, to_row, to_col, board):
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

		if board[from_row][from_col] != '0':
			return False
		else:
			return self.is_clear_path(from_row, from_col, to_row, to_col, board)

	def is_valid_move(self, from_square, to_square, board, player):
		from_row = int(from_square[0])
		from_col = int(from_square[1])
		to_row = int(to_square[0])
		to_col = int(to_square[1])
		from_piece = board[from_row][from_col]
		to_piece = board[to_row][to_col]
		if from_square == to_square:
			return False

		elif from_piece == 'P':
			# normal move forward
			if to_row == from_row-1 and to_col == from_col and to_piece == '0':
				return True
			# move two squares at start
			elif to_row == from_row-2 and to_col == from_col and to_piece == '0' and from_row == 6: 
				if self.is_clear_path(from_row, from_col, to_row, to_col, board):
					return True
			# move diagonally to take
			elif to_row == from_row-1 and (to_col== from_col+1 or to_col == from_col-1) and to_piece.islower():
				return True

		elif from_piece == 'p': # black pawn
			if to_row == from_row+1 and to_col == from_col and to_piece == '0':
				return True
			elif to_row == from_row+2 and to_col == from_col and to_piece == '0' and from_row == 1: 
				if self.is_clear_path(from_row, from_col, to_row, to_col, board):
					return True
			elif to_row == from_row+1 and (to_col == from_col+1 or to_col == from_col-1) and to_piece.isupper():
				return True

		elif from_piece == 'R':
			if (from_row == to_row or from_col == to_col) and (to_piece == '0' or to_piece.islower()):
				if self.is_clear_path(from_row, from_col, to_row, to_col, board):
					return True
		elif from_piece == 'r':
			if (from_row == to_row or from_col == to_col) and (to_piece == '0' or to_piece.isupper()):
				if self.is_clear_path(from_row, from_col, to_row, to_col, board):
					return True

		elif from_piece == 'B':
			if abs(to_row - from_row) == abs(to_col - from_col) and (to_piece == '0' or to_piece.islower()):
				if self.is_clear_path(from_row, from_col, to_row, to_col, board):
					return True
		elif from_piece == 'b':
			if abs(to_row - from_row) == abs(to_col - from_col) and (to_piece == '0' or to_piece.isupper()):
				if self.is_clear_path(from_row, from_col, to_row, to_col, board):
					return True

		elif from_piece == 'n':
			if from_col-2 == to_col and (to_row == from_row+1 or to_row == from_row-1) and (to_piece == '0' or to_piece.isupper()):
				return True
			elif from_col+2 == to_col and (to_row == from_row+1 or to_row == from_row-1) and (to_piece == '0' or to_piece.isupper()):
				return True
			elif from_row+2 == to_row and (to_col == from_col+1 or to_col == from_col-1) and (to_piece == '0' or to_piece.isupper()):
				return True
			elif from_row-2 == to_row and (to_col == from_col+1 or to_col == from_col-1) and (to_piece == '0' or to_piece.isupper()):
				return True
		elif from_piece == 'N':
			if from_col-2 == to_col and (to_row == from_row+1 or to_row == from_row-1) and (to_piece == '0' or to_piece.islower()):
				return True
			elif from_col+2 == to_col and (to_row == from_row+1 or to_row == from_row-1) and (to_piece == '0' or to_piece.islower()):
				return True
			elif from_row+2 == to_row and (to_col == from_col+1 or to_col == from_col-1) and (to_piece == '0' or to_piece.islower()):
				return True
			elif from_row-2 == to_row and (to_col == from_col+1 or to_col == from_col-1) and (to_piece == '0' or to_piece.islower()):
				return True

		elif from_piece == 'q':
			if (from_row == to_row or from_col == to_col) and (to_piece == '0' or to_piece.isupper()):
				if self.is_clear_path(from_row, from_col, to_row, to_col, board):
					return True
			elif abs(to_row - from_row) == abs(to_col - from_col) and (to_piece == '0' or to_piece.isupper()):
				if self.is_clear_path(from_row, from_col, to_row, to_col, board):
					return True
		elif from_piece == 'Q':
			if (from_row == to_row or from_col) == to_col and (to_piece == '0' or to_piece.islower()):
				if self.is_clear_path(from_row, from_col, to_row, to_col, board):
					return True
			elif abs(to_row - from_row) == abs(to_col - from_col) and (to_piece == '0' or to_piece.islower()):
				if self.is_clear_path(from_row, from_col, to_row, to_col, board):
					return True

		elif from_piece == 'k':
			if abs(from_row-to_row) <=1 and abs(from_col-to_col) <=1 and (to_piece == '0' or to_piece.isupper()):
				return True
		elif from_piece == 'K':
			if abs(from_row-to_row) <=1 and abs(from_col-to_col) <=1 and (to_piece == '0' or to_piece.islower()):
				return True

		elif self.is_check(board, player):
			return False

		return False

	def is_check(self, board, player):
		# First find player's king square
		if player == 'White':
			for i in range(8):
				for j in range(8):
					if board[i][j] == 'K':
						king_square = (i, j)
						break
		elif player == 'Black':
			for i in range(8):
				for j in range(8):
					if board[i][j] == 'k':
						king_square = (i, j)
						break
		# search through all pieces to find any valid moves
		if player == 'White':		
				for i in range(8):
					for j in range(8):
						if board[i][j]:
							if board[i][j].islower():
								if self.is_valid_move((i, j), king_square, board, 'Black'):
									return True
		if player == 'Black':		
				for i in range(8):
					for j in range(8):
						if board[i][j]:
							if board[i][j].isupper():
								if self.is_valid_move((i, j), king_square, board, 'White'):
									return True

	def is_checkmate(self, board, player):
		all_valid_moves = []
		if player == 'White':
			for i in range(8):
				for j in range(8):
					if board[i][j].islower():
						all_valid_moves.extend(self.list_valid_moves((i,j), board, player))
		elif player == 'Black':
			for i in range(8):
				for j in range(8):
					if board[i][j].isupper():
						all_valid_moves.extend(self.list_valid_moves((i,j), board, player))
		if len(all_valid_moves) == 0:
			return True
		else:
			return False

	def list_valid_moves(self, from_square, board, player):
		#returns a list of moves as tuples in tuples
		valid_moves = []
		for i in range(8):
			for j in range(8):
				if self.is_valid_move(from_square, (i,j), board, player):
					valid_moves.append((from_square, (i, j)))
		return valid_moves

# if __name__ == '__main__':
# 	game = ChessRules()
# 	board = Board()
# 	player = 'White'

# 	while True:
# 		board.print_board()
# 		if game.is_check(board.board, player):
# 			if game.is_checkmate():
# 				print("Checkmate!")
# 			else:
# 				print("Check!")

# 		print(player, 'player:')
# 		from_square = tuple(input("Which piece would you like to move? (Please give row and col ie: 73 is White Queen)\n"))
# 		to_square = tuple(input("Which square would you like to move to?\n"))

# 		if game.is_valid_move(from_square, to_square, board.board, player):
# 			board.move_piece(from_square, to_square)

# 			if player == 'White':
# 				player = 'Black'
# 			else:
# 				player = 'White'
# 		else:
# 			print("Invalid move please try again")



