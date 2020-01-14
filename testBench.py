# testBench file for programmers_coding_practice

import time
import copy
from inspect import signature

class TestCases:
    tl = list()
    tal = list()
    al = list()
    st = list()
    bl = 60

    tl_tal_al_st = list()

    pa = None

    def addCase(tc, a):
        TestCases.tl.append(tc)
        TestCases.al.append(a)

    def solve(solution):
        # solution 함수의 인자를 리스트로 받아옴
        TestCases.pa = list(signature(solution).parameters)
        tl = copy.deepcopy(TestCases.tl)

        for tc in tl:
            # 타이머를 0으로 세트
            sol = time.time()

            # solution 함수의 인자의 갯수에 따라서 전달을 다르게 구현
            if len(TestCases.pa) > 1:
                ta = solution(*tc)
            else:
                ta = solution(tc)

            # solution 실행 후의 타이머를 ms 단위로 체크
            sol = 1000 * (time.time() - sol)

            # 테스트 결과와 걸린 시간을 각각 결과 리스트에 추가
            TestCases.tal.append(ta)
            TestCases.st.append(sol)

    @staticmethod
    def isStrPrint(s):
        if isinstance(s, str):
            print("'" + s + "'", end="\t")
        else:
            print(s, end="\t")


    def printResult():
        # 모든 정보를 하나로 묶음.
        zipper = zip(TestCases.tl, TestCases.tal, TestCases.al, TestCases.st)

        for i, (tc, ta, a, st) in enumerate(zipper):
            if i == 0:
                print("=" * TestCases.bl)

            print("#### Case", i + 1, "\t| %6f ms" % st)
            print("-" * TestCases.bl)

            print("# TEST_CASE \t| ", end="")
            # 전달되는 인자를 구분하여 표현
            if len(TestCases.pa) > 1:
                for i, p in enumerate(TestCases.pa):
                    print(p, "= ", end="")
                    
                    TestCases.isStrPrint(tc[i])

                    if i != len(TestCases.pa) - 1:
                        print("| ", end="")
            else:
                print(*TestCases.pa, "= ", end="")
                TestCases.isStrPrint(tc)

            print("\n", end="")

            print("# TEST_ANSWER \t| ", end="")

            TestCases.isStrPrint(ta)

            print("\n", end="")
            print("-" * TestCases.bl)

            print("# REAL_ANSWER \t| ", end="")

            TestCases.isStrPrint(a)

            print("\n", end="")
            print("-" * TestCases.bl)

            print("# RESULT \t| %s" % "SUCCES" if ta == a else "FAIL")

            print("=" * TestCases.bl)

