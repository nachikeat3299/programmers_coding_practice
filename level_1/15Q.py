# 0109(0108) 2333
# 0109(0108) 2339
# 서울에서 김서방 찾기

def solution(seoul):
    kim_location = seoul.index('Kim')
    answer = "김서방은 " + str(kim_location) + "에 있다"
    return answer

testCases = list()
t1 = ["Jane", "Kim"]
testCases.append(t1)

if __name__ == "__main__":
    for t in testCases:
        print(solution(t))

