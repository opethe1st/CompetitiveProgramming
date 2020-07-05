"""
Chef Ada is training her calculation skills. She wants to place a king and some obstacles on a chessboard
in such a way that the number of distinct cells the king can reach is exactly K.

Recall that a chessboard has 8 rows (numbered 1 through 8) and 8 columns (numbered 1 through 8);
let's denote a cell in row r and column c by (r,c).

In one move, a king can move to any adjacent cell which shares a side or corner with its current cell and does not
contain an obstacle. More formally, a king in a cell (r,c) can move to any cell (rn,cn) if (rn,cn) is a valid cell
of the chessboard which does not contain an obstacle and (r−rn)2+(c−cn)2≤2.

A cell (x,y) can be reached by a king if, after an arbitrary number of moves (including zero), the king is in the cell (x,y).

Help Ada find any valid configuration of the board such that the king can reach exactly K distinct cells.
It is guaranteed that such a configuration always exists. If there are multiple solutions, you may find any one.
"""


class Board:
    def __init__(self):
        self.rows = [['X' for _ in range(8)] for _ in range(8)]

    def __str__(self):
        return "\n".join("".join(row) for row in self.rows)

def solution(n):
    stack = [(0, 0)]
    board = Board()
    seen = set()
    while stack and len(seen) < n:
        x, y = stack.pop()
        seen.add((x, y))
        board.rows[x][y] = '.'
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if (x+dx) in range(8) and (y+dy) in range(8) and (x+dx, y+dy) not in seen:
                    stack.append((x+dx, y+dy))
    board.rows[0][0] = 'O'
    return board

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        board = solution(n)
        print(board)
