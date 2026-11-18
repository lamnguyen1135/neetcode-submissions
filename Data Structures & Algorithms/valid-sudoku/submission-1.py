class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowLen = len(board)
        columnLen = len(board[0])
        
        
        
        nineBoxCache = {}
        for row in range(3):
            for column in range(3):
                nineBoxCache[(row, column)] = set()
        
        for i in range(rowLen):
            rowCache = []
            columnCache = []
            for j in range(columnLen):
                if board[i][j] != ".":
                    if board[i][j] in rowCache:
                        print("row")
                        return False
                    else:
                        rowCache.append(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in columnCache:
                        print("column")
                        return False
                    else:
                        columnCache.append(board[j][i])
                    
                rowIndex = i//3
                columnIndex = j//3

                if board[i][j] != ".":
                    if board[i][j] not in nineBoxCache[(rowIndex,columnIndex)]:
                        nineBoxCache[(rowIndex,columnIndex)].add(board[i][j])
                    else:
                        print(nineBoxCache)
                        print("Nine")
                        return False

        
                
                
        return True