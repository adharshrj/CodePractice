# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

class WordSearch:
    def exists(self, board, word):
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if ((r,c) in path or r >= rows or c >= cols or r < 0 or c < 0 or word[i] != board[r][c]):
                return False
            
            path.add((r,c))
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            path.remove((r,c))
        
            return res

        for r in range(rows):
            for c in range(cols):
                if (dfs(r, c, 0)):
                    return True
        
        return False

search = WordSearch()
print(search.exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))