class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def sol(row,column,index):
            if board[row][column] != word[index]:
                return False 
            if index == len(word) - 1:
                return True
            temp = board[row][column]
            board[row][column] = "#"
            left,right,down,up = 0,0,0,0
            if row>0:
                up = sol(row-1,column,index+1)
            if row<len(board)-1:
                down = sol(row+1,column,index+1)
            if column>0:
                left = sol(row,column-1,index+1)
            if column<len(board[0])-1:
                right = sol(row,column+1,index+1)
            board[row][column] = temp
            return up or down or left or right
        row = 0
        while row < len(board):
            column = 0
            while column < len(board[0]):
                if sol(row,column,0):
                    return True
                column+=1
            row+=1
        return False
