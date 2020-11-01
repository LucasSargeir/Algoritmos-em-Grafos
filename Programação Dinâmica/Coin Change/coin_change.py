import math

infinity = math.inf
coins = [1, 5, 6, 8]
memo = [-1] * 2020

def coin_change(value: int, memo):
	if value < 0: return infinity
	if value == 0: return 0

	if memo[value] != -1: return memo[value]

	min = infinity
	opt = [-1] * len(coins)

	for i in range(0, len(opt)):
		opt[i] = coin_change(value-coins[i], memo) + 1
		if(min > opt[i]):
			min = opt[i]
	
	memo[value] = min
	return min
	

value = int(input("Entre com o valor: "))
print(coin_change(value, memo))