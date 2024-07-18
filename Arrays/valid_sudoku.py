'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''

# Beats 99.5% in runtime, 37% in memory
# Self Note: Keep in mind whether it elems are ints/strings, 
# n^2 is okay for sodoku as n=9, so it's kinda like constant time

from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows = {}
        # cols = {}
        # grids = {}
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)] 
        numbers = ["1","2","3","4","5","6","7","8","9"]
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if board[i][j] in numbers:
                    grid_id = (i//3)*3 + (j//3)
                    if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in grids[grid_id]:
                        return False
                    else:
                        rows[i].add(board[i][j])
                        cols[j].add(board[i][j])
                        grids[grid_id].add(board[i][j])
                else:
                    continue
        return True




        