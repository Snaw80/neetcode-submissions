from collections import Counter
import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                elt = board[row][col]
                if elt == '.':
                    continue
                square = (row // 3) * 3 + (col // 3)
                if elt in cols[col] or elt in rows[row] or elt in squares[square]:
                    return False
                
                cols[col].add(elt)
                rows[row].add(elt)
                squares[square].add(elt)
        
        return True

                