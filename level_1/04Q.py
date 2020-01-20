# K번째 수
# 푼 날짜 : 2019 - 1 - 2
# 걸린 시간 :
def solution(array, commands):
	answer = []
	for command in commands:

		start = command[0] - 1
		end = command[1]
		key = command[2] - 1

		sorted = array[start:end]
		sorted.sort()
		answer.append(sorted[key])

	return answer