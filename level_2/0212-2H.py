# Due           0212
# Solving in    0212(1205)
# Solved in     0212(1259)
# 행렬의 곱셈

from testBench import *

def transpose(arr):
    tarr = []
    for i in range(len(arr[0])):
        line = []
        for j in range(len(arr)):
            line.append(arr[j][i])
        tarr.append(line)
    return tarr

def solution(arr1, arr2):
    answer = []
    tarr2 = transpose(arr2)
    mul = lambda x: x[0] * x[1]
    for i in range(len(arr1)):
        result = []
        for j in range(len(tarr2)):
            r = sum(map(mul, zip(arr1[i], tarr2[j])))
            result.append(r)
        answer.append(result)
    return answer

TestCases.addCase([[[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]], [[15, 15], [15, 15], [15, 15]])
TestCases.addCase([[[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]], [[22, 22, 11], [36, 28, 18], [29, 20, 14]])
TestCases.solve(solution)
TestCases.printResult()



