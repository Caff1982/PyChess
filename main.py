import os
import sys
import time
import pygame

from board import Board
from chess_rules import ChessRules
from chess_ai import ChessAI
from player import Player

GRAY = (50,50,50)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)


DATA_PATH = 'data/'

WIDTH = 800
HEIGHT = 800

SQUARE_SIZE = WIDTH//8

pygame.init()


class App:
    """
    Main class to initialize pygame gui and manage game state.

    Once the 'Run' function is called it will cycle through
    game loop.
    """

    def __init__(self):

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.surface = pygame.Surface((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.square_size = SQUARE_SIZE
        self.caption = pygame.display.set_caption('PyChess by Caff v1.0')
        self.background = pygame.image.load(os.path.join(DATA_PATH, 'chessboard.png'))
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        self.running = True
        self.state = 'start'
        self.color = 'White'

        self.rules = ChessRules()
        # set human vs AI as default option
        self.player1 = Player()
        self.two_player = False
        self.ai = ChessAI()

        self.board = Board()
        self.load_pieces()
        self.update_board()
        self.from_piece = None
        self.to_piece = None

    def load_pieces(self):
        """
        Loads piece images as class attributes
        """
        for piece in os.listdir(os.path.join(DATA_PATH, 'pieces')):
            piece_image = pygame.image.load(os.path.join(DATA_PATH + 'pieces/', piece))
            setattr(self, piece[0], piece_image)

    def update_board(self):
        self.screen.blit(self.background, [0, 0])
        # b is the buffersize for each square
        b = self.square_size//4
        for col in range(8):
            for row in range(8):
                if self.board.board[col][row].isalpha():
                    piece = getattr(self, self.board.board[col][row])
                    self.screen.blit(piece, (row*self.square_size+b,
                                             col*self.square_size+b))
        pygame.display.update()

    def button(self, msg, x, y, width, height,
               inactive_clr, active_clr, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.screen, active_clr, (x, y, width, height))
            if click[0] == 1 and action is not None:
                action()
                pygame.draw.rect(self.screen, BLACK, (x, y, width, height))

        else:
            pygame.draw.rect(self.screen, inactive_clr, (x, y, width, height))

        smallText = pygame.font.SysFont('parchment', 30)
        TextSurf, TextRect = self.text_objects(msg, smallText)
        TextRect.center = ((x+(width/2)), y+(height/2))
        self.screen.blit(TextSurf, TextRect)

    def difficulty_button(self, msg, x, y, width, height,
                          inactive_clr, active_clr, depth):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.screen, active_clr, (x, y, width, height))
            if click[0] == 1:
                self.depth = depth
                pygame.draw.rect(self.screen, BLACK, (x, y, width, height))

        else:
            pygame.draw.rect(self.screen, inactive_clr, (x, y, width, height))

        smallText = pygame.font.SysFont('parchment', 30)
        TextSurf, TextRect = self.text_objects(msg, smallText)
        TextRect.center = ((x+(width/2)), y+(height/2))
        self.screen.blit(TextSurf, TextRect)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()

    def start_game(self):
        self.state = 'playing'

    def set_2player(self):
        self.two_player = True

    def stop_2player(self):
        self.two_player = False

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.update_board()
            elif self.state == 'gameover':
                self.end_events()
            else:
                self.running = False
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'

    def start_draw(self):
        self.screen.fill(GRAY)
        self.difficulty_button('Easy', 200, 250, 90, 50, WHITE, GREEN, 2)
        self.difficulty_button('Medium', 355, 250, 90, 50, WHITE, GREEN, 3)
        self.difficulty_button('Hard', 510, 250, 90, 50, WHITE, GREEN, 4)
        self.button('Human vs AI', 200, 350, 180, 50, WHITE, GREEN, self.set_2player)
        self.button('Human vs Human', 420, 350, 180, 50, WHITE, GREEN, self.set_2player)
        self.button('Press Spacebar to Start', 200, 450, 400, 50, WHITE, WHITE)
        self.button('Default play mode is Human vs AI.', 
                     100, 650, 600, 50, GRAY, GRAY)
        self.button('Default difficulty is Medium. Playing in Hard difficulty will take longer.',
                     100, 700, 600, 50, GRAY, GRAY)
        self.button('For more information please view the README file.', 
                     100, 750, 600, 50, GRAY, GRAY)
        pygame.display.update()

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                if self.from_piece is None:
                    from_x, from_y = pygame.mouse.get_pos()
                    self.from_piece = (from_x, from_y)
                else:
                    to_x, to_y = pygame.mouse.get_pos()
                    self.to_piece = (to_x, to_y)

            if self.from_piece:
                row, col = [i//self.square_size for i in self.from_piece[::-1]]
                piece = self.board.board[row][col]
                if piece is not '0':
                    sprite = getattr(self, piece)
                    x, y = pygame.mouse.get_pos()
                    self.screen.blit(sprite, (x-25, y-25))
                    pygame.display.update()

            if self.from_piece and self.to_piece:
                # Change from pixel values to board values
                from_square = [i//self.square_size for i in self.from_piece[::-1]]
                to_square = [i//self.square_size for i in self.to_piece[::-1]]
                self.from_piece = None
                self.to_piece = None
                # make sure move does not put player in check
                testboard = self.board.get_testboard(from_square, to_square, self.board)
                if self.rules.is_check(testboard, self.color):
                    self.button(f'Invalid move, {self.color} in check!',
                                200, 375, 300, 50, WHITE, WHITE)
                    pygame.display.update()
                    time.sleep(2)
                # make sure move is valid before moving pieces
                elif not self.rules.is_valid_move(from_square, to_square,
                                                  self.board, self.color):
                    self.button(f'That is not a valid move.',
                                200, 375, 300, 50, WHITE, WHITE)
                    pygame.display.update()
                    time.sleep(1.5)
                else:
                    self.board.move_piece(from_square, to_square)
                    if self.color == 'White':
                        self.color = 'Black'
                    else:
                        self.color = 'White'
                    # Now see if there is check or checkmate
                    if self.rules.is_check(self.board, self.color):
                        if self.rules.is_checkmate(self.board, self.color):
                            self.state = 'gameover'
                        self.button(f'{self.color} in check!',
                                    200, 375, 300, 50, WHITE, WHITE)
                        pygame.display.update()
                        time.sleep(1)

            elif self.color == 'Black' and not self.two_player:
                AI_move = self.ai.get_best_move(self.board, True, 3)
                self.board.move_piece(AI_move[0], AI_move[1])
                self.board.print_board()
                self.color = 'White'
                
    def end_events(self):
        self.button(f'Game Over! {self.color} wins', 200, 375, 400, 50,
                    WHITE, GREEN, self.start_game)
        pygame.display.update()
        time.sleep(3)
        self.board = Board()
        self.state = 'start'


if __name__ == '__main__':
    app = App()
    app.run()
