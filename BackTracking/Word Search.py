class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        path = set()

        def define_word(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) \
                    or board[i][j] != word[k] or (i, j) in path:
                return False

            path.add((i, j))
            res = (define_word(i + 1, j, k + 1) or define_word(i - 1, j, k + 1) or
                   define_word(i, j + 1, k + 1) or define_word(i, j - 1, k + 1))
            path.remove((i, j))

            return res


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if define_word(i, j, 0):
                        return True

        return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(Solution().exist(board, word))
