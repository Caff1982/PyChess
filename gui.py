import os
import sys
import time
import pygame

from board import Board
from chess_rules import ChessRules
from chess_ai import ChessAI 
from player import Player 
from settings import *

from test import *

pygame.init()


class GUI:

    def __init__(self):

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        self.square_size = SQUARE_SIZE
        self.caption = pygame.display.set_caption('Chess by Caff V0.1')
        self.background = pygame.image.load(os.path.join(DATA_PATH, 'chessboard.png')).convert()
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        self.running = True
        self.state = 'start'
        self.color = 'White'

        self.rules = ChessRules()
        # set human vs AI as only option for now
        self.player1 = Player()
        self.ai = ChessAI()

        self.board = Board(white_wins_one_move)
        self.load_pieces()
        self.update_board() 
        self.from_piece = None
        self.to_piece = None        

    def load_pieces(self):
        # load piece images from 'pieces' directory
        for piece in os.listdir(os.path.join(DATA_PATH, 'pieces')):
            piece_image = pygame.image.load(os.path.join(DATA_PATH + 'pieces/', piece))
            setattr(self, piece[0], piece_image)

    def update_board(self):
        self.screen.blit(self.background, [0, 0])
        b = self.square_size//4 # set the buffersize for each square
        for col in range(8):
            for row in range(8):
                if self.board.board[col][row].isalpha():
                    piece = getattr(self, self.board.board[col][row])
                    self.screen.blit(piece, (row*self.square_size+b, col*self.square_size+b))
        pygame.display.update()

    def button(self, msg,x,y,width,height,inactive_clr,active_clr, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
            
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.screen, active_clr, (x,y,width,height))
            # we pass the action as an arg and then call below using()
            if click[0] == 1 and action != None:
                action()
                pygame.draw.rect(self.screen, BLACK, (x,y,width,height))

        else:
            pygame.draw.rect(self.screen, inactive_clr, (x,y,width,height))

        smallText = pygame.font.Font('freesansbold.ttf',20)
        TextSurf, TextRect = self.text_objects(msg, smallText)
        TextRect.center = ( (x+(width/2)), y+(height/2) )
        self.screen.blit(TextSurf, TextRect)

    def difficulty_button(self, msg,x,y,width,height,inactive_clr,active_clr, depth):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.screen, active_clr, (x,y,width,height))
            if click[0] == 1:
                self.depth = depth
                pygame.draw.rect(self.screen, BLACK, (x,y,width,height))

        else:
            pygame.draw.rect(self.screen, inactive_clr, (x,y,width,height))

        smallText = pygame.font.Font('freesansbold.ttf',20)
        TextSurf, TextRect = self.text_objects(msg, smallText)
        TextRect.center = ( (x+(width/2)), y+(height/2) )
        self.screen.blit(TextSurf, TextRect)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()

    def start_game(self):
        self.state = 'playing'

    def set_player2(self):
        print("Not set up yet, can only play against AI")
        pass
        # if not self.player2:
        #     self.player2 = True
        # if self.player2:
        #     self.player2 = False

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
    
            self.clock.tick(30)
        pygame.quit()
        sys.exit()

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'

    def start_draw(self):
        self.screen.fill((50,50,50))
        self.difficulty_button('Easy',200,250,90,50,WHITE,GREEN, 2)
        self.difficulty_button('Medium',355,250,90,50,WHITE,GREEN, 3)
        self.difficulty_button('Hard',510,250,90,50,WHITE,GREEN, 4)
        self.button('Human vs AI',200,350,180,50,WHITE,GREEN,self.set_player2)
        self.button('Human vs Human',420,350,180,50,WHITE,GREEN,self.set_player2)
        self.button('Press Spacebar to Start',200,450,400,50,WHITE,GREEN,self.start_game)
        pygame.display.update()
        

    def playing_events(self):

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.from_piece == None:
                        from_x,from_y = pygame.mouse.get_pos()
                        self.from_piece = (from_x, from_y)
                    else:
                        to_x,to_y = pygame.mouse.get_pos()
                        self.to_piece = (to_x, to_y)

                
                if self.from_piece and self.to_piece:
                    if self.color == 'White':
                        # We divide by square size to change from number of pixels to rows/cols
                        # and reverse as  board matrix is cols/row
                        from_square = [i//self.square_size for i in self.from_piece[::-1]]
                        to_square = [i//self.square_size for i in self.to_piece[::-1]]
                        print(from_square, to_square)
                        self.from_piece = None 
                        self.to_piece = None
                        if not self.rules.is_valid_move(from_square, to_square, 
                                                        self.board, self.color):
                            print("That is not a valid move.")
                            
                        else:
                            print("Move piece, from and to:", from_square, to_square)
                            self.board.move_piece(from_square, to_square)           
                            # TODO: Find out if white or black in check
                            if self.rules.is_check(self.board, 'Black'):
                                if self.rules.is_checkmate(self.board, 'Black'):
                                    print("Checkmate! White wins")
                                    self.state = 'gameover'
                                    break
                                else:
                                    print("Black in check!")
                            self.color = 'Black'

                elif self.color == 'Black': # For now black is AI
                    start = time.time()
                    AI_move = self.ai.get_best_move(self.board, True, 3)
                    end = time.time()
                    print(AI_move)
                    print(end - start)
                    self.board.move_piece(AI_move[0], AI_move[1])
                    self.board.print_board()
                    self.color = 'White'





    def end_events(self):
        self.button(f'Game Over! {self.color} wins',200,450,400,50,WHITE,GREEN,self.start_game)
        pygame.display.update()
        time.sleep(3)
        self.board = Board()
        self.state = 'start'




if __name__ == '__main__':

    gui = GUI()
    gui.run()

