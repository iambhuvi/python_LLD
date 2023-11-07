from models.playing_piece import PlayingPiece


class Board:
    size: int
    board: PlayingPiece

    def __init__(self, size) -> None:
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def add_piece(self, row, column, piece: PlayingPiece):
        if self.board[row][column] is not None:
            return False
        self.board[row][column] = piece

        return True
        
    def print_board(self):
        for i in range(self.size):
            row = ""
            for j in range(self.size):
                board_value = self.board[i][j]
                if j == 0:
                    row += "| "
                if board_value is not None:
                    row += self.board[i][j].type+" | "
                else:
                    row += " | "
            print(row)
    
    def get_free_cells(self):
        free_cells = []
        for i in range(self.size):
            for j in range(self.size):
                if(self.board[i][j] == None):
                    free_cells.append((i,j))
        
        return free_cells


                

