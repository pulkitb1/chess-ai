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
    
    def makeMove(self,move):
        self.board[move.startRow][move.startColumn] = "--"
        self.board[move.endRow][move.endColumn] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove

class Move(): 
    ranksToRows = {"1":7, "2":6, "3":5, "4":4, "5":3, "6":2, "7":1, "8":0}
    rowsToRanks = {v: k for k, v in  ranksToRows.items()}
    filestoCols = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}
    colsToFiles = {v: k for k, v in filestoCols.items()}
    
    def __init__(self,startSq,endSq,board):
        self.startRow = startSq[0]
        self.startColumn = startSq[1]
        self.endRow = endSq[0]
        self.endColumn = endSq[1]
        self.pieceMoved = board[self.startRow][self.startColumn]
        self.pieceCaptured = board[self.endRow][self.endColumn]
    
    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startColumn) + self.getRankFile(self.endRow, self.endColumn)
    def getRankFile(self,r,c):
        return self.colsToFiles[c]+self.rowsToRanks[r]