from models.playing_piece import PlayingPiece


class Player:
    name: str
    piece: PlayingPiece

    def __init__(self, name, piece) -> None:
        self.name = name
        self.piece = piece