

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

        if board[from_row * 8 + from_col] != '0':
            return False
        else:
            return self.is_clear_path(from_row, from_col, to_row, to_col, board)

    def is_valid_move(self, from_idx, to_idx, board, player):
        from_row = from_idx // 8
        from_col = from_idx % 8
        to_row = to_idx // 8
        to_col = to_idx % 8
        from_piece = board.board[from_idx]
        to_piece = board.board[to_idx]

        if player == 'White' and from_piece.islower():
            return False
        elif player == 'Black' and from_piece.isupper():
            return False
        elif from_idx == to_idx:
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
            elif board.black_castleK and from_idx == 4 and to_idx == 7 and \
                self.is_clear_path(from_row, from_col, to_row, to_col, board.board) \
                    and not self.is_check(board, player):
                return True
            elif board.black_castleQ and from_idx == 4 and to_idx == 0 and \
                self.is_clear_path(from_row, from_col, to_row, to_col, board.board) \
                    and not self.is_check(board, player):
                return True

        elif from_piece == 'K':
            if abs(from_row-to_row) <= 1 and abs(from_col-to_col) <= 1 and \
                    (to_piece == '0' or to_piece.islower()):
                return True
            elif board.white_castleK and from_idx == 60 and to_idx == 63 and \
                self.is_clear_path(from_row, from_col, to_row, to_col, board.board) \
                    and not self.is_check(board, player):
                return True
            elif board.white_castleQ and from_idx == 60 and to_idx == 56 and \
                self.is_clear_path(from_row, from_col, to_row, to_col, board.board) \
                    and not self.is_check(board, player):
                return True

        return False

    def is_check(self, board, color):
        """
        Takes board object and color as args and returns True/False
        """
        # Search for pieces which could attack the King
        if color == 'White':
            king_idx = board.board.index('K')
            for idx in range(64):
                if board.board[idx].islower():
                    if self.is_valid_move(idx, king_idx,
                                          board, 'Black'):
                            return True
        elif color == 'Black':
            king_idx = board.board.index('k')
            for idx in range(64):
                if board.board[idx].isupper():
                    if self.is_valid_move(idx, king_idx,
                                          board, 'White'):
                            return True
        else:
            return False

    def is_checkmate(self, board, color):
        possible_moves = self.get_all_possible_moves(board, color)
        for from_idx, to_idx in possible_moves:
            testboard = board.get_testboard(from_idx, to_idx)
            if not self.is_check(testboard, color):
                return False
        return True

    def is_stalemate(self, board, color):
        if len(self.get_all_possible_moves(board, color)) == 0:
            return True
        else:
            return False

    def list_valid_moves(self, from_idx, board, color):
        """
        Returns a list of moves as list of tuples within tuples
        """
        valid_moves = []
        for idx in range(64):
            if self.is_valid_move(from_idx, idx, board, color):
                testboard = board.get_testboard(from_idx, idx)
                if not self.is_check(testboard, color):
                    to_piece = board.board[idx]
                    if to_piece not in {'k', 'K'}:
                        valid_moves.append((from_idx, idx))
        return valid_moves

    def get_all_possible_moves(self, board, color):
        moves = []
        if color == 'White':
            for idx in range(64):
                if board.board[idx].isupper():
                    moves.extend(self.list_valid_moves(idx, board, color))
        elif color == 'Black':
            for idx in range(64):
                if board.board[idx].islower():
                    moves.extend(self.list_valid_moves(idx, board, color))
        return moves
