from chess_rules import ChessRules
from piece_tables import transposition_dict


class ChessAI:
    """
    Class used for generating AI chess moves

    Uses mini-max with alpha-beta pruning to get best move available.
    For now the AI only works as Black player.

    The evaluation function uses piece-tables to get a heuristic score as
    well as piece-value score. Recommended depth is 3, anything above this
    takes a long time to return a move.
    """

    def __init__(self):
        self.rules = ChessRules()
        self.color = 'Black'

    def get_best_move(self, board, is_maximizing, depth):
        """
        Gets all available moves and iterates through these to
        find the best move by calling the 'minimax' function.
        """
        best_move = -99999
        best_move_final = None
        for move in self.rules.get_all_possible_moves(board, 'Black'):
            testboard = board.get_testboard(move[0], move[1])
 
            value = max(best_move, self.minimax(testboard, float('-inf'), float('inf'),
                                                not is_maximizing, depth-1))
            if value > best_move:
                if not self.rules.is_check(testboard, 'Black'):
                    # print('Best score', best_move)
                    # print('Best move:', best_move_final)
                    best_move = value
                    best_move_final = (move[0], move[1])

        return best_move_final

    def minimax(self, board, alpha, beta, is_maximizing, depth):
        """
        Uses recursion to search for best move. Alpha-beta pruning used
        to improve efficiency.
        """
        if depth == 0:
            return self.get_evaluation(board, is_maximizing)

        if is_maximizing:
            moves = self.rules.get_all_possible_moves(board, 'Black')
            best_move = -99999
            for move in moves:
                testboard = board.get_testboard(move[0], move[1])
                best_move = max(best_move, self.minimax(testboard, alpha, beta,
                                                        False, depth-1))
                alpha = max(alpha, best_move)
                if alpha >= beta:
                    return best_move
            return best_move
        else:
            moves = self.rules.get_all_possible_moves(board, 'White')
            best_move = 99999
            for move in moves:
                testboard = board.get_testboard(move[0], move[1])
                best_move = min(best_move, self.minimax(testboard, alpha, beta,
                                                        True, depth-1))
                beta = min(beta, best_move)
                if alpha >= beta:
                    return best_move
            return best_move

    def get_board_value(self, board):
        board_value = 0
        for i, cell in enumerate(board):
            if cell.isalpha():
                board_value += transposition_dict[cell][i]

        return board_value

    def get_evaluation(self, board, is_maximazing):
        evaluation = 0
        # get heuristic values of board first
        evaluation += self.get_board_value(board.board)
        # then get piece values
        for i in range(64):
                evaluation += self.get_piece_value(board.board[i])
        return evaluation

    def get_piece_value(self, piece):
        if piece == '0':
            return 0
        elif piece == 'P':
            return -1000
        elif piece == 'p':
            return 1000
        elif piece == 'N':
            return -3000
        elif piece == 'n':
            return 3000
        elif piece == 'B':
            return -3100
        elif piece == 'b':
            return 3100
        elif piece == 'R':
            return -4750
        elif piece == 'r':
            return 4750
        elif piece == 'Q':
            return -9000
        elif piece == 'q':
            return 9000
        elif piece == 'K':
            return -90000
        elif piece == 'k':
            return 90000
  