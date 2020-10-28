tasks = [{"name": "A", "limit": 2, "price":100},
		 {"name": "B", "limit": 1, "price":19},
		 {"name": "C", "limit": 2, "price":27},
		 {"name": "D", "limit": 1, "price":25},
		 {"name": "E", "limit": 3, "price":15}]

tasks = sorted(tasks, key=lambda task: task["price"], reverse = True)
timeline = [-1] * (len(tasks))

max_task_time = tasks[0]["limit"] - 1
timeline[max_task_time] = 0

for i in range(1, len(tasks)):
	max_task_time = tasks[i]["limit"] - 1
	for j in range(0, max_task_time + 1):
		if(timeline[j] == -1):
			timeline[j] = i
			break

for i in timeline:
	if(i != -1):
		print(tasks[i])