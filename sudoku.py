

import numpy as np
import pandas as pd

class SudoKu():
    
    def __init__(self,keyboard):
        self.keyboard = keyboard
    
    def find_next_cell(self, i, j):
        '''
        # 代填位置 
        '''
        # for x in range(i,9): # 减少暴力遍历
        #     for y in range(j,9):
        #         if self.keyboard[x][y] == 0:
        #             return x,y
        for x in range(0,9):
            for y in range(0,9):
                if self.keyboard[x][y] == 0:
                    return x,y
        return -1,-1

    def is_valid(self, i, j, element):
        '''
        # 直接输入 检查合法性
        '''
        if element not in self.keyboard[i]:
            for x in range(0,9):
                if element == self.keyboard[x][j]:
                    return False
            scope_x, scope_y = 3 *(i//3), 3 *(j//3) # 宫
            for x in range(scope_x, scope_x+3):
                for y in range(scope_y, scope_y+3):
                    if self.keyboard[x][y] == element:
                        return False
            return True
        return False

    def sudoku(self, i=0, j=0):
        i,j = self.find_next_cell(i, j)
        if i == -1:
            return True
        
        for element in range(1,10):
            if self.is_valid(i,j,element):
                # 创建现场
                self.keyboard[i][j] = element
                # 递归
                if self.sudoku(i, j):
                    return True
                # 恢复现场
                self.keyboard[i][j] = 0
        return False


    def calculate_sum(self,m=1,n=1):
        '''
        # m,n 大于 0
        '''
        total = 0
        for i in range(0,m):
            for j in range(0,n):
                total += self.keyboard[i][j]

        return total


if __name__ == '__main__':

    board = [[3,0,0,2,0,0,0,0,0],[0,0,0,1,0,7,0,0,0],[7,0,6,0,3,0,5,0,0],[0,7,0,0,0,9,0,8,0],[9,0,0,0,2,0,0,0,4],[0,1,0,8,0,0,0,5,0],[0,0,9,0,4,0,3,0,1],[0,0,0,7,0,2,0,0,0],[0,0,0,0,0,8,0,0,6]]
    s = SudoKu(board)
    s.sudoku()

    a = pd.DataFrame(np.array(s.keyboard).reshape(9,9), index=['','','','','','','','',''], columns=['','','','','','','','',''])
    print(a)
    print('------------------------------------------------------------------------------------')
    total = s.calculate_sum(1,3)
    print('the sum of the first three in the top row is {}'.format(total))
    total = s.calculate_sum(9,1)
    print('the sum of each puzzle is {}'.format(total))
    print('------------------------------------------------------------------------------------')
