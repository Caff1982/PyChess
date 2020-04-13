import os
import sys
import time
import pygame

from board import Board
from chess_rules import ChessRules
from chess_ai import ChessAI
from player import Player


LIGHT_GRAY = (150,150,150)
DARK_GRAY = (90,90,90)
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
        self.caption = pygame.display.set_caption('PyChess by Caff')
        self.background = pygame.image.load(os.path.join(DATA_PATH, 'chessboard.png'))
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        self.running = True
        self.state = 'start'
        self.color = 'White'

        self.rules = ChessRules()
        # TODO: Make AI able to play as white
        self.player1 = Player()
        self.two_player = False
        self.ai = ChessAI()
        self.depth = 3

        self.board = Board()
        self.load_pieces()
        self.update_board()
        self.from_piece = None
        self.to_piece = None

    def load_pieces(self):
        """
        Loads piece images and sets them as class attributes.
        """
        for piece in os.listdir(os.path.join(DATA_PATH, 'pieces')):
            piece_image = pygame.image.load(os.path.join(DATA_PATH + 'pieces/', piece))
            setattr(self, piece[0], piece_image)

    def print_move(self, a, b):
        """
        Prints move in terminal.
        format: (row, column)
        """
        print(f'Moved from: ({a//8},{a%8}) to: ({b//8},{b%8})')

    def update_board(self):
        self.screen.blit(self.background, [0, 0])
        # b is the buffersize for each square
        b = self.square_size//4
        for col in range(8):
            for row in range(8):
                idx = col * 8 + row
                if self.board.board[idx].isalpha():
                    piece = getattr(self, self.board.board[idx])
                    self.screen.blit(piece, (row*self.square_size+b,
                                             col*self.square_size+b))
        pygame.display.update()

    def button(self, msg, x, y, width, height,
               inactive_clr, active_clr, action=None):
        """
        Helper function for creating simple buttons
        """
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
        """
        Button used for setting difficulty/depth
        """
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

    def start_2player(self):
        self.two_player = True

    def stop_2player(self):
        self.two_player = False

    def start_game(self):
        self.state = 'playing'
        self.color = 'White'
        self.board = Board()

    def run(self):
        """
        Main loop used to control game state
        """
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.update_board()
            elif self.state == 'gameover':
                self.end_events()
                self.end_draw()
            else:
                self.running = False
            self.clock.tick(120)
        pygame.quit()
        sys.exit()

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'

    def start_draw(self):
        self.screen.fill(LIGHT_GRAY)
        self.difficulty_button('Easy', 200, 250, 90, 50, WHITE, DARK_GRAY, 2)
        self.difficulty_button('Medium', 355, 250, 90, 50, WHITE, DARK_GRAY, 3)
        self.difficulty_button('Hard', 510, 250, 90, 50, WHITE, DARK_GRAY, 4)
        self.button('Human vs AI', 200, 350, 180, 50, WHITE, DARK_GRAY, self.stop_2player)
        self.button('Human vs Human', 420, 350, 180, 50, WHITE, DARK_GRAY, self.start_2player)
        self.button('Press Spacebar to Start', 200, 450, 400, 50, WHITE, WHITE, self.start_game)
        self.button('Default play mode is Human vs AI.', 
                     100, 650, 600, 50, LIGHT_GRAY, LIGHT_GRAY)
        self.button('Default difficulty is Medium. Playing in Hard difficulty will take longer.',
                     100, 700, 600, 50, LIGHT_GRAY, LIGHT_GRAY)
        self.button('For more information please view the README file.', 
                     100, 750, 600, 50, LIGHT_GRAY, LIGHT_GRAY)
        pygame.display.update()

    def update_game_state(self):
        """
        Used to update state after each move.
        Changes player and looks for check, checkmate,
        stalemate.
        """
        if self.color == 'White':
            self.color = 'Black'
        else:
            self.color = 'White'

        if self.rules.is_check(self.board, self.color):
            if self.rules.is_checkmate(self.board, self.color):
                self.state = 'gameover'
            else:
                self.button(f'{self.color} in check!',
                            200, 375, 300, 50, WHITE, WHITE)
                pygame.display.update()
                time.sleep(1)
        elif self.rules.is_stalemate(self.board, self.color):
            self.state = 'gameover'

    def move_piece(self, from_idx, to_idx):
        self.board.move_piece(from_idx, to_idx)
        self.print_move(from_idx, to_idx)
        self.update_board()
        self.board.print_board()
        self.update_game_state()

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                if self.from_piece is None:
                    from_x, from_y = pygame.mouse.get_pos()
                    self.from_piece = (from_y//self.square_size, from_x//self.square_size)
                else:
                    to_x, to_y = pygame.mouse.get_pos()
                    self.to_piece = (to_y//self.square_size, to_x//self.square_size)

            if self.from_piece:
                idx = self.from_piece[0] * 8 + self.from_piece[1]
                piece = self.board.board[idx]
                if piece is not '0':
                    sprite = getattr(self, piece)
                    x, y = pygame.mouse.get_pos()
                    self.screen.blit(sprite, (x-25, y-25))
                    pygame.display.update()

            if self.from_piece and self.to_piece:
                # Convert pixel values to board values
                from_idx = self.from_piece[0] * 8 + self.from_piece[1]
                to_idx = self.to_piece[0] * 8 + self.to_piece[1]
                self.from_piece = None
                self.to_piece = None
                
                testboard = self.board.get_testboard(from_idx, to_idx)
                
                # Make sure move is valid before moving pieces
                if not self.rules.is_valid_move(from_idx, to_idx,
                                                  self.board, self.color):
                    self.button(f'That is not a valid move.',
                                200, 375, 300, 50, WHITE, WHITE)
                    pygame.display.update()
                    time.sleep(1.5)
                # Make sure move does not put player in check
                elif self.rules.is_check(testboard, self.color):
                    self.button(f'Invalid move, {self.color} in check!',
                                200, 375, 300, 50, WHITE, WHITE)
                    pygame.display.update()
                    time.sleep(2)
                else:
                    self.move_piece(from_idx, to_idx)

            if self.color == 'Black' and not self.two_player and self.state == 'playing':
                start = time.perf_counter()
                print('\nGenerating AI move...')
                from_idx, to_idx = self.ai.get_best_move(self.board, True, self.depth)
                end = time.perf_counter()
                print(f'Took {round(end-start, 2)}secs to generate AI move')
                self.move_piece(from_idx, to_idx)

    def end_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.start_game()

    def end_draw(self):                   
        if self.rules.is_check(self.board, self.color):
            if self.color == 'White':
                winner = 'Black'
            else:
                winner = 'White'
            self.button(f'Checkmate! {winner} wins', 250, 450, 300, 50,
                        WHITE, WHITE)
        else:
            self.button(f'Game Over! Stalemate', 250, 450, 300, 50,
                        WHITE, WHITE)

        self.button('Press Spacebar to Start', 250, 550, 300, 50,
                    WHITE, LIGHT_GRAY, self.start_game)
        pygame.display.update()


if __name__ == '__main__':
    app = App()
    app.run()
