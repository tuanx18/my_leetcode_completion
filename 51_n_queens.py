class Solution(object):
    @staticmethod
    def solveNQueens(n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []

        path = []
        dia1 = set()
        dia2 = set()
        used = set()
        
        def backtrack(row):
            if row == n:
                res.append(path[:])
                return
            
            for col in range(n):
                if col in used:
                    continue
                if row - col in dia1:
                    continue
                if row + col in dia2:
                    continue

                path.append(col)
                used.add(col)
                dia1.add(row - col)
                dia2.add(row + col)

                backtrack(row + 1)
                path.pop()
                used.remove(col)
                dia1.remove(row - col)
                dia2.remove(row + col)
        backtrack(0)

        board = []
        for pos in res: # [1, 3, 0, 2]
            board_path = []
            for p in pos:
                place = ''
                for ll in range(n):
                    if ll == p:
                        place += 'Q'
                    else:
                        place += '.'
                board_path.append(place)
            board.append(board_path)
        return board

n = 4
sol = Solution.solveNQueens(n)
print(sol)