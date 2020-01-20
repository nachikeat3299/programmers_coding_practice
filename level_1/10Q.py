# 0106 1202
# 0106 1209
# 두 정수 사이의 합 
def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    else:
        for i in range(min(a, b), max(a, b) + 1):
            answer += i

    return answer

testCases = list()
t1 = [3, 5]
t2 = [3, 3]
t3 = [5, 3]
testCases.append(t1)
testCases.append(t2)
testCases.append(t3)
if __name__ == '__main__':
    for t in testCases:
        print(solution(t[0], t[1]))

