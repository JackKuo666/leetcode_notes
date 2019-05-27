# 法1. 回溯法，递归实现
 
# class Solution:
#     def solveSudoku(self, board):
#         self.board = board
#         self.solve()
 
#     def solve(self):  # 主递归函数
#         row, col = self.findUnassigned()  # 获取一个未被分配的方格
#         if row == -1 and col == -1:  # 没有找到，说明已经填好
#             return True
#         for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
#             if self.isSafe(row, col, num):  # 循环填入数字，并判断是否满足要求
#                 self.board[row][col] = num
#                 if self.solve():  # 递归进入下一个方格
#                     return True
#                 self.board[row][col] = '.'  # 后续不满足，那么现在要回复当前环境，并进行下一个数字试探
#         return False
 
#     def findUnassigned(self):  # 依次查找未被分配的方格
#         for row in range(9):
#             for col in range(9):
#                 if self.board[row][col] == '.':
#                     return row, col
#         return -1, -1
 
#     def isSafe(self, row, col, ch):  # 判断是否当前方格填入的数字是否满足要求
#         boxrow = row - row % 3  # 确定3x3小宫格的开始坐标，就是3x3小宫格第一个方格索引
#         boxcol = col - col % 3
#         if self.checkrow(row, ch) and self.checkcol(col, ch) and self.checksquare(boxrow, boxcol, ch):
#             return True
#         return False
 
#     def checkrow(self, row, ch):  # 检查一行是否符合条件
#         for col in range(9):
#             if self.board[row][col] == ch:
#                 return False
#         return True
 
#     def checkcol(self, col, ch):  # 检查一列是否符合条件
#         for row in range(9):
#             if self.board[row][col] == ch:
#                 return False
#         return True
 
#     def checksquare(self, row, col, ch):  # 检查3x3小宫格是否符合条件
#         for r in range(row, row + 3):
#             for c in range(col, col + 3):
#                 if self.board[r][c] == ch:
#                     return False
#         return True


# 法2.递归实现 优化版
class Solution:
    def solveSudoku(self, board):
        self.board = board
        self.val = self.PossibleVals()
        self.Solver()


    def PossibleVals(self):
        a = "123456789"
        d, val = {}, {}
        for i in range(9):
            for j in range(9):
                ele = self.board[i][j]
                if ele != ".":
                    d[("r", i)] = d.get(("r", i), []) + [ele]
                    d[("c", j)] = d.get(("c", j), []) + [ele]
                    d[(i // 3, j // 3)] = d.get((i // 3, j // 3), []) + [ele]
                else:
                    val[(i, j)] = []
        for (i, j) in val.keys():
            inval = d.get(("r", i), []) + d.get(("c", j), []) + d.get((i / 3, j / 3), [])
            val[(i, j)] = [n for n in a if n not in inval]
        return val


    def Solver(self):
        if len(self.val) == 0:
            return True
        kee = min(self.val.keys(), key=lambda x: len(self.val[x]))
        nums = self.val[kee]
        for n in nums:
            update = {kee: self.val[kee]}
            if self.ValidOne(n, kee, update):  # valid choice
                if self.Solver():  # keep solving
                    return True
            self.undo(kee, update)  # invalid choice or didn't solve it => undo
        return False


    def ValidOne(self, n, kee, update):
        self.board[kee[0]][kee[1]] = n
        del self.val[kee]
        i, j = kee
        for ind in self.val.keys():
            if n in self.val[ind]:
                if ind[0] == i or ind[1] == j or (ind[0] / 3, ind[1] / 3) == (i / 3, j / 3):
                    update[ind] = n
                    self.val[ind].remove(n)
                    if len(self.val[ind]) == 0:
                        return False
        return True


    def undo(self, kee, update):
        self.board[kee[0]][kee[1]] = "."
        for k in update:
            if k not in self.val:
                self.val[k] = update[k]
            else:
                self.val[k].append(update[k])
        return None

 
