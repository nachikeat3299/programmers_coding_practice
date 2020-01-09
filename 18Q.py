# 0110(0109) 1421
# 0110(0109) 1438
# 문자열을 정수로 바꾸기
def solution(s):
    answer = int(s)
    return answer

def solution_2(s):
    answer = 0
    plus_minus = +1
    start = 0
    if s[0] == '-':
        plus_minus = -1
        start = 1

    for i in range(start, len(s)):
        current = 10 ** (len(s) - i - 1)
        # print("len(s), i, current =", len(s), i, current)
        answer += 10 ** (len(s) - i - 1) * int(s[i])
    return answer * plus_minus


testCases = list()
testCases.append("1234")
testCases.append("-1234")

if __name__ == "__main__":
    for t in testCases:
        print("S1\n", t, "to", solution(t))
    for t in testCases:
        print("S2\n", t, "to", solution_2(t))


