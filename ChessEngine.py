'''
- Responsible for storing information about the current state of the game.
- Also responsible for determining valid moves and moves log.
'''

class GameState():
    def __init__(self):
        # Representing the chess board.
        # first intial alphabet denotes color: b-black, w-white
        # second initial alphabet denotes piece: p-pawn,R-Rook etc. 
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]

        self.whiteToMove = True
        self.moveLog = []