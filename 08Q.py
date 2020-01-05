# 0105 1906
# 0105 1943
# 같은 숫자는 싫어

def solution(arr):
    i = 0
    j = i + 1
    answer = []
    while i < len(arr):

        while j < len(arr):

            if arr[i] == arr[j]:
                j += 1

            elif arr[i] != arr[j]:
                answer.append(arr[i])
                i = j
                j = i + 1
                break
        if j == len(arr):
            answer.append(arr[i])
            break

    print('Hello Python')
    return answer

testCases = list()
t1 = [1, 1, 3, 3, 0, 1, 1]
t2 = [4, 4, 4, 3, 3]
testCases.append(t1)
testCases.append(t2)

if __name__ == '__main__':
    for t in testCases:
        print(solution(t))


