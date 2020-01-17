# 0121(0117) 1107
# 0121(0117) 1140
### 37. 비밀 지도

from testBench import *
def solution(n, arr1, arr2):
    answer = []

    for i, (j_1, j_2) in enumerate(zip(arr1, arr2)):
        arr1[i] = str(bin(j_1))[2:]
        arr2[i] = str(bin(j_2))[2:]

        if len(arr1[i]) < n:
            arr1[i] = "0" * (n - len(arr1[i])) + arr1[i]

        if len(arr2[i]) < n:
            arr2[i] = "0" * (n - len(arr2[i])) + arr2[i]

        code = ""

        for m_1, m_2 in zip(arr1[i], arr2[i]):
            if m_1 == "1" or m_2 == "1":
                code += "#"
            else:
                code += " "
        answer.append(code)
    
    return answer

TestCases.addCase([5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]], ["#####", "# # #", "### #", "#  ##", "#####"])
TestCases.addCase([6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]], ["######", "###  #", "##  ##", " #### ", " #####", "### # "])
TestCases.solve(solution)
TestCases.printResult()
