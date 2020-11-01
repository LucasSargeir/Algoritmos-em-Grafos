memo = {}

def findSub(s1, s2, size_01, size_02):
	if size_01 == 0 or size_02 == 0: return ""

	global memo
	key = str(size_01) + "|" + str(size_02)
	if key in memo: return memo[key]

	if s1[size_01 - 1] == s2[size_02 - 1]:
		memo |= {key: findSub(s1, s2, size_01 - 1, size_02 - 1) + str(s1[size_01 - 1])}
		return memo[key]
	
	decreasing_str_01 = findSub(s1, s2, size_01 - 1, size_02)
	decreasing_str_02 = findSub(s1, s2, size_01, size_02 - 1)

	if len(decreasing_str_01) > len(decreasing_str_02):
		memo |= {key: decreasing_str_01}
	else:
		memo |= {key: decreasing_str_02}
	return memo[key]


sub_01 = input('Entre com uma subsequencia:')
sub_02 = input('Entre com outra subsequencia:')
print(findSub(sub_01, sub_02, len(sub_01), len(sub_02)))