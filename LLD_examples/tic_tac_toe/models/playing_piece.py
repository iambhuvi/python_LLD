from abc import ABC
from models.pieces_type import PieceType
from zope.interface import Interface, Attribute

class PlayingPiece(ABC):
    # type: PieceType = Attribute("type")
    type: PieceType