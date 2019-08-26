

class Board:
	def __init__(self):
		self.board =  [['r','n','b','q','k','b','n','r'],
					   ['p']*8,
					   ['0']*8,
					   ['0']*8,
					   ['0']*8,
					   ['0']*8,
					   ['P']*8,
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
			# piece taken
			self.board[to_row][to_col] = piece