# 0119(0115) 1155
# 0119(0115) 1233
### 33. 행렬의 덧셈
from testBench import *

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        c = []
        for j in range(len(arr1[i])):
            c.append(arr1[i][j] + arr2[i][j])
        answer.append(c)

    return answer


"""
if __name__ == "__main__":
    print(solution([[[1, 2], [2, 3]], [[3, 4], [5, 6]]], [[4, 6], [7, 9]]))
"""
TestCases.addCase([[[1, 2], [2, 3]], [[3, 4], [5, 6]]], [[4, 6], [7, 9]] )
TestCases.addCase([[[1], [2]], [[3], [4]]], [[4], [6]] )
TestCases.solve(solution)
TestCases.printResult()
