# 0118(0115) 1142
# 0118(0115) 1148
### 32. 핸드폰 번호 가리기
from testBench import *

def solution(phone_number):
    last_4_digit = phone_number[-4:]
    num_star = len(phone_number) - 4
    answer = "*" * num_star + last_4_digit
    return answer

TestCases.addCase("01033334444", "*******4444")
TestCases.addCase("027778888", "*****8888")
TestCases.solve(solution)
TestCases.printResult()
