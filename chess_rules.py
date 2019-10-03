

class ChessRules:
    """
    Class containing main rules for chess.

    Used to make sure moves are valid, also for check, checkmate and list
    valid moves.
    """

    def is_clear_path(self, from_row, from_col, to_row, to_col, board):

        # Base case, if only moving one square path is clear
        if abs(from_row-to_row) <= 1 and abs(from_col-to_col) <= 1:
            return True
        else:
            if from_col == to_col and from_row < to_row: # rows+
                from_row += 1
            elif from_col == to_col and from_row > to_row: # rows-
                from_row -= 1
            elif from_row == to_row and from_col < to_col: # cols+
                from_col += 1
            elif from_row == to_row and from_col > to_col: # cols-
                from_col -= 1
            elif from_row < to_row and from_col < to_col: # diag SE
                from_row += 1
                from_col += 1
            elif from_row < to_row and from_col > to_col: # diag NE
                from_row += 1
                from_col -= 1
            elif from_row > to_row and from_col > to_col: # diag NW
                from_row -= 1
                from_col -= 1
            elif from_row > to_row and from_col < to_col: # diag SW
                from_row -= 1
                from_col += 1

        if board[from_row][from_col] != '0':
            return False
        else:
            return self.is_clear_path(from_row, from_col, to_row, to_col, board)

    def is_valid_move(self, from_square, to_square, board, player):
        from_row = from_square[0]
        from_col = from_square[1]
        to_row = to_square[0]
        to_col = to_square[1]
        from_piece = board.board[from_row][from_col]
        to_piece = board.board[to_row][to_col]

        if player == 'White' and from_piece.islower():
            return False
        elif player == 'Black' and from_piece.isupper():
            return False
        elif from_square == to_square:
            return False

        elif from_piece == 'P':
            # normal move forward
            if to_row == from_row-1 and to_col == from_col and to_piece == '0':
                return True
            # move two squares at start
            elif to_row == from_row-2 and to_col == from_col \
                    and to_piece == '0' and from_row == 6:
                if self.is_clear_path(from_row, from_col,
                                      to_row, to_col, board.board):
                    return True
            # move diagonally to take
            elif to_row == from_row-1 and (to_col == from_col+1 or to_col == from_col-1) \
                                      and to_piece.islower():
                return True

        elif from_piece == 'p':
            if to_row == from_row+1 and to_col == from_col and to_piece == '0':
                return True
            elif to_row == from_row+2 and to_col == from_col and \
                    to_piece == '0' and from_row == 1:
                if self.is_clear_path(from_row, from_col, to_row, to_col, board.board):
                    return True
            elif to_row == from_row+1 and (to_col == from_col+1 or to_col == from_col-1) \
                                      and to_piece.isupper():
                return True

        elif from_piece == 'R':
            if (from_row == to_row or from_col == to_col) and \
                    (to_piece == '0' or to_piece.islower()):
                if self.is_clear_path(from_row, from_col,
                                      to_row, to_col, board.board):
                    return True

        elif from_piece == 'r':
            if (from_row == to_row or from_col == to_col) and \
                    (to_piece == '0' or to_piece.isupper()):
                if self.is_clear_path(from_row, from_col,
                                      to_row, to_col, board.board):
                    return True

        elif from_piece == 'B':
            if abs(to_row - from_row) == abs(to_col - from_col) and \
                    (to_piece == '0' or to_piece.islower()):
                if self.is_clear_path(from_row, from_col,
                                      to_row, to_col, board.board):
                    return True
        elif from_piece == 'b':
            if abs(to_row - from_row) == abs(to_col - from_col) and \
                    (to_piece == '0' or to_piece.isupper()):
                if self.is_clear_path(from_row, from_col,
                                      to_row, to_col, board.board):
                    return True

        elif from_piece == 'n':
            if from_col-2 == to_col and (to_row == from_row+1 or to_row == from_row-1) \
                    and (to_piece == '0' or to_piece.isupper()):
                return True
            elif from_col+2 == to_col and (to_row == from_row+1 or to_row == from_row-1) \
                    and (to_piece == '0' or to_piece.isupper()):
                return True
            elif from_row+2 == to_row and (to_col == from_col+1 or to_col == from_col-1) \
                    and (to_piece == '0' or to_piece.isupper()):
                return True
            elif from_row-2 == to_row and (to_col == from_col+1 or to_col == from_col-1) \
                    and (to_piece == '0' or to_piece.isupper()):
                return True

        elif from_piece == 'N':
            if from_col-2 == to_col and (to_row == from_row+1 or to_row == from_row-1) \
                    and (to_piece == '0' or to_piece.islower()):
                return True
            elif from_col+2 == to_col and (to_row == from_row+1 or to_row == from_row-1) \
                    and (to_piece == '0' or to_piece.islower()):
                return True
            elif from_row+2 == to_row and (to_col == from_col+1 or to_col == from_col-1) \
                    and (to_piece == '0' or to_piece.islower()):
                return True
            elif from_row-2 == to_row and (to_col == from_col+1 or to_col == from_col-1) \
                    and (to_piece == '0' or to_piece.islower()):
                return True

        elif from_piece == 'q':
            if (from_row == to_row or from_col == to_col) and (to_piece == '0'
                                                        or to_piece.isupper()):
                if self.is_clear_path(from_row, from_col,
                                      to_row, to_col, board.board):
                    return True
            elif abs(to_row - from_row) == abs(to_col - from_col) and \
                    (to_piece == '0' or to_piece.isupper()):
                if self.is_clear_path(from_row, from_col,
                                      to_row, to_col, board.board):
                    return True

        elif from_piece == 'Q':
            if (from_row == to_row or from_col == to_col) and (to_piece == '0'
                                                        or to_piece.islower()):
                if self.is_clear_path(from_row, from_col,
                                      to_row, to_col, board.board):
                    return True
            elif abs(to_row - from_row) == abs(to_col - from_col) and \
                    (to_piece == '0' or to_piece.islower()):
                if self.is_clear_path(from_row, from_col,
                                      to_row, to_col, board.board):
                    return True

        elif from_piece == 'k':
            if abs(from_row-to_row) <= 1 and abs(from_col-to_col) <= 1 and \
                    (to_piece == '0' or to_piece.isupper()):
                return True
            elif board.black_castleK and (to_col == 7 and to_row == 0) and \
                self.is_clear_path(from_row, from_col, to_row, to_col, board.board) \
                    and not self.is_check(board, player):
                return True
            elif board.black_castleQ and (to_col == 0 and to_row == 0) and \
                self.is_clear_path(from_row, from_col, to_row, to_col, board.board) \
                    and not self.is_check(board, player):
                return True

        elif from_piece == 'K':
            if abs(from_row-to_row) <= 1 and abs(from_col-to_col) <= 1 and \
                    (to_piece == '0' or to_piece.islower()):
                return True
            elif board.white_castleK and (to_col == 7 and to_row == 7) and \
                self.is_clear_path(from_row, from_col, to_row, to_col, board.board) \
                    and not self.is_check(board, player):
                return True
            elif board.white_castleQ and (to_col == 0 and to_row == 7) and \
                self.is_clear_path(from_row, from_col, to_row, to_col, board.board) \
                    and not self.is_check(board, player):
                return True

        return False

    def is_check(self, board, color):
        """
        Takes board object and color as args and returns True/False
        """
        if color == 'White':
            king_piece = 'K'
        else:
            king_piece = 'k'
        # find player's king square
        for i in range(8):
            for j in range(8):
                if board.board[i][j] == king_piece:
                    king_square = (i, j)
                    break
        # Search for pieces which could attack the King
        if color == 'White':
            for i in range(8):
                for j in range(8):
                    if board.board[i][j].islower():
                        if self.is_valid_move((i, j), king_square,
                                               board, 'Black'):
                            return True
        elif color == 'Black':
            for i in range(8):
                for j in range(8):
                    if board.board[i][j].isupper():
                        if self.is_valid_move((i, j), king_square,
                                               board, 'White'):
                            return True
        else:
            return False

    def is_checkmate(self, board, color):
        possible_moves = self.get_all_possible_moves(board, color)
        for move in possible_moves:
            testboard = board.get_testboard(move[0], move[1], board)
            if not self.is_check(testboard, color):
                return False
        return True

    def list_valid_moves(self, from_square, board, color):
        """
        Returns a list of moves as list of tuples within tuples
        """
        valid_moves = []
        for i in range(8):
            for j in range(8):
                if self.is_valid_move(from_square, (i, j), board, color):
                    to_piece = board.board[i][j]
                    if to_piece not in {'k', 'K'}:
                        valid_moves.append((from_square, (i, j)))
        return valid_moves

    def get_all_possible_moves(self, board, color):
        moves = []
        if color == 'White':
            for i in range(8):
                for j in range(8):
                    if board.board[i][j].isupper():
                        moves.extend(self.list_valid_moves((i, j), board, color))
        if color == 'Black':
            for i in range(8):
                for j in range(8):
                    if board.board[i][j].islower():
                        moves.extend(self.list_valid_moves((i, j), board, color))
        return moves
