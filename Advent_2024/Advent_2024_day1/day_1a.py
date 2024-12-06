file_path = "input2024_1.txt"

###Day 1a###

left_list = []
right_list = []

with open(file_path, "r") as file:
    for line in file:
        left, right = line.split()
        left_list.append(left)
        right_list.append(right)
        
left_list.sort()
right_list.sort()

total_distance = 0

for left, right in zip(left_list, right_list):
    total_distance += abs(int(left) - int(right))
    
print(total_distance)

#correct answer: 2285373