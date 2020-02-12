# Due           0209
# Solving in    0210(1309)
# Solved in     0210()
# 땅따먹기

from testBench import *

def make_path(rows):
    paths = []

    for f in range(0, 4):
        path_1 = [f]
        path_2 = [f]
        path_3 = [f]

        for i in range(1, rows):
            select = [0, 1, 2, 3]
            select.remove(path[i - 1])
            path_1.append(selec)






def solution(lands):
    answer = 0

    for first in range(0, 4):
        for land in lands:
            
        

    return answer

TestCases.addCase([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]], 16)
TestCases.solve(solution)
TestCases.printResult()



