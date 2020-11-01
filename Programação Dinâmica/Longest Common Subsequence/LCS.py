memo = {}
def LCS(sub_01: str, sub_02: str, size_01: int, size_02):
	if size_01 == 0 or size_02 == 0: return 0

	global memo
	key = str(size_01) + "|" + str(size_02)
	if key in memo: return memo[key]

	if(sub_01[size_01 - 1] == sub_02[size_02 - 1]):
		memo |= {key: max(LCS(sub_01, sub_02, size_01 - 1, size_02 - 1),
						  LCS(sub_01, sub_02, size_01 - 1, size_02 - 1)) + 1}
	else:
		memo |= {key: max(LCS(sub_01, sub_02, size_01 - 1, size_02),
						  LCS(sub_01, sub_02, size_01, size_02 - 1))}
	return memo[key]


sub_01 = input('Entre com uma subsequencia:')
sub_02 = input('Entre com outra subsequencia:')
print(LCS(sub_01, sub_02, len(sub_01), len(sub_02)))