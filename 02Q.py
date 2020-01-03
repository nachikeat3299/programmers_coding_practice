def solution(participant, completion):
	lazyMan = ""
	completionDict = dict()
	completionSet = set(completion)
	for name in completionSet:
		completionDict[name] = 0
	for compMan in completion:
		completionDict[compMan] += 1
	for partMan in participant:
		if partMan in completionDict:
			if completionDict[partMan] != 0:
				completionDict[partMan] -= 1
			elif completionDict[partMan] == 0:
				lazyMan = partMan
				break
		else:
			lazyMan = partMan
			break

	answer = lazyMan
	return answer