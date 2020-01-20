# 체육복
# 푼 날짜 : 2019 - 1 - 3
# 걸린 시간 :

def solution(n, lost, reserve):
	clothes = [1 for i in range(n)]
	for i in lost:
		clothes[i - 1] -= 1
	for i in reserve:
		clothes[i - 1] += 1
	print("before", clothes)

	for i in range(len(clothes)):
		if clothes[i] == 0:
			if i == 0:
				if clothes[i + 1] > 1:
					clothes[i + 1] -= 1
					clothes[i] += 1

			elif i == len(clothes) - 1:
				if clothes[i - 1] > 1:
					clothes[i - 1] -= 1
					clothes[i] += 1
			else:
				if clothes[i - 1] > 1:
					clothes[i - 1] -= 1
					clothes[i] += 1

				elif clothes[i + 1] > 1:
					clothes[i + 1] -= 1
					clothes[i] += 1
	print("after", clothes)
	zeroCount = 0
	for i in range(len(clothes)):
		if clothes[i] == 0:
			zeroCount += 1

	answer = len(clothes) - zeroCount
	return answer