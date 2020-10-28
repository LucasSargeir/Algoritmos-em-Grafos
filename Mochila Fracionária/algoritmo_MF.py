bag_size = 50
bag_index = 0 
bag_used = 0 
score = 0
items = [{"weight":10, "points":60}, 
		 {"weight":30, "points":120}, 
		 {"weight":20, "points":100}]

for item in items:
	item |= {"ratio": (item["points"] / item["weight"])}

items = sorted(items, key=lambda item: item["ratio"], reverse=True) 

while((items[bag_index]["weight"] + bag_used) < bag_size):
	bag_used += items[bag_index]["weight"]
	score += items[bag_index]["points"]
	bag_index +=1

bag_missing_ratio = (bag_size - bag_used) / items[bag_index]["weight"]
score += items[bag_index]["points"] * bag_missing_ratio

print("Max: " + str(score))