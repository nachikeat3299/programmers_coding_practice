# Due           0126
# Solving in    0127(1610) FAILED
# 

from testBench import *



def solution(arrangement):
    answer = 0

    # 레이저의 모양을 ()에서 *로 바꾼다. 2문자에서 1문자로 바꿈
    arrangement.replace("()", "*")

    for c in arrangement:


    return answer

TestCases.addCase(["()(((()())(())()))(())"], 17)
TestCases.solve(solution)
TestCases.printResult()


