# 0111(0110) 1305
# 0111(0110) 
# 약수의 합

def solution(n):
    answer = 0
    divisor = list()

    for d in range(1, n + 1):
        if d not in divisor:
            if n % d == 0:
                divisor.append(d)
                if d != n // d:
                    divisor.append(n // d)
    answer = sum(divisor)

    return answer

testCases = list()
testCases.append(12)
testCases.append(5)
testCases.append(9)

if __name__ == "__main__":
    for t in testCases:
        print(solution(t))
