# This file is for tic tac toe ll example.
from models.board import Board
from models.player import Player
from models.piece_O import PieceO
from models.piece_X import PieceX
import logging
from collections import deque

class TicTacToeGame:
    players: deque
    game_board: Board

    def __init__(self) -> None:

        self.players: deque = deque([])
        PieceO_obj = PieceO()
        player_1: Player = Player("Santosh", PieceO_obj)

        PieceX_obj = PieceX()
        player_2: Player = Player("Ramesh", PieceX_obj)

        self.players.appendleft(player_1)
        self.players.appendleft(player_2)

        self.game_board = Board(3)

    def start_game(self):
        no_winner = True

        while(no_winner):
            player = self.players.pop()
            self.game_board.print_board()

            if len(self.game_board.get_free_cells()) <= 0 :
                no_winner = False
                continue

            in_row_col = input(f"Player enter your row and columns.")
            in_row, in_col = list(map(lambda x: int(x), in_row_col.split(",")))
            #place the piece
            piece_added_sucessfully = self.game_board.add_piece(in_row, in_col, player.piece)

            if not piece_added_sucessfully:
                print("Incorrect postion. Please try again")
                self.players.append(player)
                continue

            self.players.appendleft(player)
            
            
        # break






def main():
    logging.basicConfig(level=logging.DEBUG)
    tic_tac_toe_game_obj = TicTacToeGame()
    tic_tac_toe_game_obj.start_game()
    



if __name__ == "__main__":
    main()

