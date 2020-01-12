# 0114(0112) 1317
# 0114(0112) 1327
# 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = []
    s = str(n)
    for c in s:
        answer.append(int(c))
    answer.reverse()
    return answer

testCases = list()
testCases.append(12345)

if __name__ == '__main__':
    for t in testCases:
        print(solution(t))
