def solution(a, b):
	dayName = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
	dayPerMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	totalDay = b - 1
	for i in range(a - 1):
		totalDay += dayPerMonth[i]
	totalDay %= 7
	index = 5 # dayName[index] = 'FRI'
	index += totalDay
	if index > len(dayName) - 1:
		index -= 7
	answer = dayName[index]
	return answer
