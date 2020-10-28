activities = [{"name": "A1", "starts": 0, "ends": 6},
			  {"name": "A2", "starts": 3, "ends": 4},
			  {"name": "A3", "starts": 1, "ends": 2},
			  {"name": "A4", "starts": 5, "ends": 9},
			  {"name": "A5", "starts": 5, "ends": 7},
			  {"name": "A6", "starts": 8, "ends": 9}]

activities = sorted(activities, key=lambda activity: activity["ends"]) 

selected_activities = []
is_first = True

for i in range(len(activities)):
	if is_first:
		selected_activities.append(activities[i])
		is_first = False
	else:
		last_inserted = selected_activities[-1]
		if(activities[i]["starts"] >= last_inserted["ends"]):
			selected_activities.append(activities[i])

print("Tarefas: \n" + str(selected_activities).replace('},', '}\n'))