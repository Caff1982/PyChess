import copy


class Board:
    """
    Class to keep track of chess board and move pieces.

    Castling rights are stored as class attributes and
    updated in the move_piece function.
    """
    def __init__(self, board=None):
        if board is None:
            self.board = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'] + \
                         ['p']* 8 + \
                         ['0']* 32 + \
                         ['P']* 8 + \
                         ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        else:
            self.board = board

        self.white_can_castle = True
        self.black_can_castle = True

    def print_board(self):
        print('\n  0 1 2 3 4 5 6 7')
        for i in range(8):
            print(i, ' '.join(self.board[i*8:i*8+8]))

    def get_testboard(self, from_idx, to_idx):
        """
        Returns a copy of the Board object 
        with piece moved
        """
        testboard = copy.deepcopy(self)
        piece = self.board[from_idx]
        testboard.board[from_idx] = '0'
        testboard.board[to_idx] = piece
        return testboard

    def move_piece(self, from_idx, to_idx):
        piece = self.board[from_idx]
        to_piece = self.board[to_idx]

        # King cannot be take
        if to_piece in ('k', 'K'):
            pass
        # Pawn promotion
        elif piece == 'p' and to_idx // 8 == 7:
            self.board[to_idx] = 'q'
            self.board[from_idx] = '0'
        elif piece == 'P' and to_idx // 8 == 0:
            self.board[to_idx] = 'Q'
            self.board[from_idx] = '0'
        # Check for castling
        elif piece == 'k':
            if to_idx == 0 and self.black_can_castle:
                self.board[0] = '0'
                self.board[1] = 'k'
                self.board[2] = 'r'
                self.board[4] = '0'
            elif to_idx == 7 and self.black_can_castle:
                self.board[4] = '0'
                self.board[5] = 'r'
                self.board[6] = 'k'
                self.board[7] = '0'
            else:
                # Normal move to empty square
                self.board[from_idx] = '0'
                self.board[to_idx] = piece
            # Update castling rights
            self.black_can_castle = False
        elif piece == 'K':
            if to_idx == 56 and self.white_can_castle:
                self.board[56] = '0'
                self.board[57] = 'K'
                self.board[58] = 'R'
                self.board[60] = '0'
            elif to_idx == 63 and self.white_can_castle:                
                self.board[60] = '0'
                self.board[61] = 'R'
                self.board[62] = 'K'
                self.board[63] = '0'
            else:
                self.board[from_idx] = '0'
                self.board[to_idx] = piece
            self.white_can_castle = False
        else:
            # Normal move to empty square
            self.board[from_idx] = '0'
            self.board[to_idx] = piece
        

