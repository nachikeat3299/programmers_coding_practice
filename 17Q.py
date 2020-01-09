# 0110(0109) 1416
# 0110(0109) 1420
# 수박수박수박수박수박수?

def solution(n):
    answer = ''
    for i in range(0, n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer


testCases = list()
testCases.append(3)
testCases.append(4)

if __name__ == "__main__":
    for t in testCases:
        print(solution(t))


