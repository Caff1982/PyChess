from board import Board 
from chess_rules import ChessRules 
from gui import *
from player import Player 
from chess_ai import ChessAI

white_in_check = 	[['r', 'n', 'b', 'q', 'q', 'b', 'n',' r'],
					['0']*8,
					['0']*8,
					['0']*8,
					['0']*8,
					['0']*8,
					['0']*8,
					['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

black_in_check = 	[['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
					['0']*8,
					['0']*8,
					['0']*8,
					['0']*8,
					['0']*8,
					['0']*8,
					['R', 'N', 'B', 'Q', 'Q', 'B', 'N', 'R']]

black_kn_threatened = 	[['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
						 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
						 ['0']*8,
						 ['0']*8,
						 ['0']*8,
						 ['0']*8,
						 ['0', '0', 'n', '0', '0', '0', '0', '0'],
						 ['p', 'p', 'p', 'Q', '0', 'p', 'p', 'p'],
						 ['R', 'N', 'B', '0', 'K', 'B', 'N', 'R']]

black_kn_dont_attack =	[['r', '0', 'b', 'q', 'k', 'b', 'n', 'r'],
 						 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
 						 ['0', '0', '0', '0', '0', '0', '0', '0'],
 						 ['0', '0', '0', '0', '0', '0', '0', '0'],
 						 ['0', 'n', '0', 'P', 'P', '0', '0', '0'],
 						 ['0', '0', 'P', '0', '0', '0', '0', '0'],
 						 ['P', 'P', '0', '0', '0', 'P', 'P', 'P'],
 						 ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]






ai = ChessAI()
rules = ChessRules()

# assert rules.is_check(white_in_check, 'White')
# assert rules.is_check(black_in_check, 'Black')

# board = Board(black_in_check)
# move = ai.depth_search(board.board, 'Black', 2)
# print("Move should move get black out of check", move)
# board.move_piece(move[0][0], move[0][1])
# board.print_board()

# board = Board(black_kn_threatened)
# move = ai.depth_search(board.board, 'Black', 2)
# print("Move should move blacks vulnerable knight at c3", move)
# board.move_piece(move[0][0], move[0][1])
# board.print_board()

board = Board(black_kn_dont_attack)
move = ai.depth_search(board.board, 'Black', 3)
print("Black should move knight on b4 as it's under threat", move)
board.move_piece(move[0][0], move[0][1])
board.print_board()