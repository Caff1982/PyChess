import copy


class Board:
    """
    Class to keep track of chess board and move pieces.

    Board is initialized as starting board by default. Castling
    rights are stored as class attributes and updated in the
    move_piece function.
    """
    def __init__(self, board=None):
        if board is None:
            self.board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                          ['p']*8,
                          ['0']*8,
                          ['0']*8,
                          ['0']*8,
                          ['0']*8,
                          ['P']*8,
                          ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        else:
            self.board = board

        self.white_castleK = True
        self.white_castleQ = True
        self.black_castleK = True
        self.black_castleQ = True

    def print_board(self):
        print('    0    1    2    3    4    5    6    7')
        for i, row in enumerate(self.board):
            print(i, row)

    def get_testboard(self, from_square, to_square):
        testboard = copy.deepcopy(self)
        from_row = from_square[0]
        from_col = from_square[1]
        to_row = to_square[0]
        to_col = to_square[1]
        piece = self.board[from_row][from_col]
        testboard.board[from_row][from_col] = '0'
        testboard.board[to_row][to_col] = piece
        return testboard

    def move_piece(self, from_square, to_square):
        from_row = from_square[0]
        from_col = from_square[1]
        to_row = to_square[0]
        to_col = to_square[1]
        piece = self.board[from_row][from_col]

        # normal move to empty square
        if self.board[to_row][to_col] == '0':
            self.board[from_row][from_col] = '0'
            self.board[to_row][to_col] = piece
        # take piece
        elif (piece.isupper() and self.board[to_row][to_col].islower()) or \
                (piece.islower() and self.board[to_row][to_col].isupper()):
            self.board[from_row][from_col] = '0'
            self.board[to_row][to_col] = piece
        else:
            # castling
            if piece == 'k':
                if to_col == 0:
                    self.board[0][0] = '0'
                    self.board[0][1] = 'k'
                    self.board[0][2] = 'r'
                    self.board[0][3] = '0'
                elif to_col == 7:
                    self.board[0][4] = '0'
                    self.board[0][5] = 'r'
                    self.board[0][6] = 'k'
                    self.board[0][6] = '0'
            elif piece == 'K':
                if to_col == 0:
                    self.board[7][0] = '0'
                    self.board[7][1] = 'K'
                    self.board[7][2] = 'R'
                    self.board[7][3] = '0'
                elif to_col == 7:
                    self.board[7][4] = '0'
                    self.board[7][5] = 'R'
                    self.board[7][6] = 'K'
                    self.board[7][7] = '0'

        # update castling rights
        if piece.lower() == 'k':
            if from_row == 0:
                self.black_castleK = False
                self.black_castleQ = False
            else:
                self.white_castleK = False
                self.white_castleQ = False
        elif piece.lower() == 'r':
            if from_row == 0:
                if from_col == 0:
                    self.black_castleQ = False
                elif from_col == 7:
                    self.black_castleK = False
            elif from_row == 7:
                if from_col == 0:
                    self.black_castleQ = False
                elif from_col == 7:
                    self.black_castleK = False
        # pawn promotion
        if piece == 'p' and to_row == 7:
            self.board[to_row][to_col] = 'q'
        elif piece == 'P' and to_row == 0:
            self.board[to_row][to_col] = 'Q'
