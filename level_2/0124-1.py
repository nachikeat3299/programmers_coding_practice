# Due           0124
# Solving in    0121(FAILED)
# Solvein in(2) 0121(1353)
# Solved in     0121(1547)
# 스킬 트리

from testBench import *

def squeeze(skills, skill_tree):
    return ''.join([_skill for _skill in skill_tree if _skill in skills])


def generate(skills):
    generated_skill_tree = []

    for length in range(1, len(skills) + 1):
        generated_skill_tree.append(skills[0:length])
    generated_skill_tree.append('')
    return generated_skill_tree


def solution(skills, skill_trees):
    squeeze_trees = [squeeze(skills, skill_tree) for skill_tree in skill_trees]
    possible = generate(skills)
    # breakpoint()
    return len([squeeze_tree for squeeze_tree in squeeze_trees if squeeze_tree in possible])


TestCases.addCase(["CBD", ["BACDE", "CBADF", "AECB", "BDA"]], 2)
TestCases.addCase(["C", ["BACDE", "CBADF", "AEB", "BDA"]], 2)
TestCases.addCase(["ABCDEFGHIJKLMNOPQRSTUVWXYZ", ["ABC", "AF", "E", "Z"]], 1)
TestCases.solve(solution)
TestCases.printResult()



