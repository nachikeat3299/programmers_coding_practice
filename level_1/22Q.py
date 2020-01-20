# 0113(0112) 1307
# 0113(0112) 1312
# 자릿수 더하기

def solution(n):
    answer = 0
    s = str(n)
    for i in range(len(s)):
        answer += int(s[i])

    return answer

testCases = list()
testCases.append(123)
testCases.append(987)

if __name__ == '__main__':
    for t in testCases:
        print(solution(t))



