import math

#model => [value, weight]
items = [(8, 1), (4, 2), (0, 3), (5, 2), (3, 2)]
memo = {}
infinity = math.inf

def bag_01(capacity: int, id_item = 0)->int:
	if capacity < 0: return -infinity
	if id_item == len(items): return 0

	global memo
	key = str(id_item) + "|" + str(capacity)
	if key in memo:return memo[key]
	
	value = max(bag_01(capacity, id_item + 1), bag_01(capacity - items[id_item][1], id_item + 1) + items[id_item][0])
	memo |= {key: value}

	return memo[key]

capacity = int(input("Entre com a capacidade: "))
print(bag_01(capacity, 0))