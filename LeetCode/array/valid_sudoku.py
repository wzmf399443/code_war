class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            row = [i for i in row if i != "."]
            if len(row) != len(set(row)):
                return False

        colnums = list(zip(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))
        for colnum in colnums:
            colnum = [i for i in colnum if i != "."]
            if len(colnum) != len(set(colnum)):
                return False

        c = 0
        for _ in range(3):
            square = []
            for i, v in enumerate(zip(board[0 + c], board[1 + c], board[2 + c])):
                square += list(v)
                if (i + 1) % 3 == 0:
                    square = [i for i in square if i != "."]
                    if len(square) != len(set(square)):
                        return False
                    square = []
            c += 3

        return True

    # Others Answer
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [{str(i): 0 for i in range(1, 10)} for j in range(9)]
        cols = [{str(i): 0 for i in range(1, 10)} for j in range(9)]
        boxes = [{str(i): 0 for i in range(1, 10)} for j in range(9)]
        for r in range(n):
            for c in range(n):
                val = board[r][c]
                if val != '.':
                    if rows[r][val] > 0:
                        return False
                    rows[r][val] += 1

                    if cols[c][val] > 0:
                        return False
                    cols[c][val] += 1

                    idx = (r // 3) * 3 + c // 3
                    if boxes[idx][val] > 0:
                        return False
                    boxes[idx][val] += 1
        return True


print(Solution().isValidSudoku([[".", ".", ".", ".", ".", ".", "5", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], ["9", "3", ".", ".", "2", ".", "4", ".", "."], [
      ".", ".", "7", ".", ".", ".", "3", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "3", "4", ".", ".", ".", "."], [".", ".", ".", ".", ".", "3", ".", ".", "."], [".", ".", ".", ".", ".", "5", "2", ".", "."]]))


"""
[[".",".",".",".","5",".",".","1","."],
 [".","4",".","3",".",".",".",".","."],
 [".",".",".",".",".","3",".",".","1"],
 ["8",".",".",".",".",".",".","2","."],
 [".",".","2",".","7",".",".",".","."],
 [".","1","5",".",".",".",".",".","."],
 [".",".",".",".",".","2",".",".","."],
 [".","2",".","9",".",".",".",".","."],
 [".",".","4",".",".",".",".",".","."]]
"""
