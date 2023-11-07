from models.pieces_type import PieceType
from models.playing_piece import PlayingPiece
import zope.interface 

# @zope.interface.implementer(PlayingPiece)
class PieceX(PlayingPiece):
    def __init__(self) -> None:
        self.type: PieceType = PieceType.X
        # super().__init__(PieceType.X)