def solution(s):
	input_string_length = len(s)
	minimal_compressed_length = 1001
	minimal_compressed_string = ""

	for part_size in range(1, input_string_length + 1):
		key = 0
		compressed = ""

		while key < input_string_length:
			part = s[key: key + part_size]
			count = 1

			for index in range(key + part_size, input_string_length, part_size):
				compare_part = s[index: index + part_size]

				if part != compare_part:
					break

				elif part == compare_part:
					count += 1
			if count == 1:
				compressed += part

			elif count > 1:
				compressed += (str(count) + part)
			key += part_size * (count)

		if minimal_compressed_length > len(compressed):
			minimal_compressed_length = len(compressed)
			minimal_compressed_string = compressed      

	answer = minimal_compressed_length

	return answer


