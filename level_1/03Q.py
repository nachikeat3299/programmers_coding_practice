# 모의고사
# 푼 날짜 : 2019 - 1 - 2
# 걸린 시간 :

def solution(answers):
	answer = []
	aPerson = [1, 2, 3, 4, 5]
	bPerson = [2, 1, 2, 3, 2, 4, 2, 5]
	cPerson = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

	aScore = 0
	bScore = 0
	cScore = 0

	index = 0
	for key in answers:
		if key == aPerson[(index + 1) % len(aPerson) - 1]:
			aScore += 1
		if key == bPerson[(index + 1) % len(bPerson) - 1]:
			bScore += 1
		if key == cPerson[(index + 1) % len(cPerson) - 1]:
			cScore += 1
		index += 1

	if aScore == bScore:
		if aScore > cScore:
			answer.append(1)
			answer.append(2)
		elif aScore < cScore:
			answer.append(3)
		elif aScore == cScore:
			answer.append(1)
			answer.append(2)
			answer.append(3)
	elif bScore == cScore:
		if bScore > aScore:
			answer.append(2)
			answer.append(3)
		elif bScore < aScore:
			answer.append(1)
		elif bScore == aScore:
			answer.append(1)
			answer.append(2)
			answer.append(3)
	elif aScore == cScore:
		if aScore > bScore:
			answer.append(1)
			answer.append(3)
		elif aScore < cScore:
			answer.append(3)
		elif aScore == cScore:
			answer.append(1)
			answer.append(2)
			answer.append(3)
	else:
		maxPerson = max(aScore, bScore, cScore)
		if maxPerson == aScore:
			answer.append(1)
		elif maxPerson == bScore:
			answer.append(2)
		elif maxPerson == cScore:
			answer.append(3)

	return answer