# 0115(0112) 1336
# 0115(0112) FAILED
# 정수 제곱근 판별 
import math

def solution(n):
    answer = 0

    for i in range(1, int(math.sqrt(n)) + 1):
        if n // i == i: 
            answer = (i + 1) ** 2

    if n == 0:
        answer = 1

    if answer == 0:
        answer = -1

    return answer

testCases = list()
testCases.append(121)
testCases.append(3)
testCases.append(1)
testCases.append(0)

if __name__ == '__main__':
    for t in testCases:
        print(solution(t))
