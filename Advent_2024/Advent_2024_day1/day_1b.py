from collections import Counter

file_path = "input2024_1.txt"

###Day 1b###

left_list = []
right_list = []

with open(file_path, "r") as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
        
similarity_score = 0
#create dictionary with each value in right list with number of times it appears
right_count = Counter(right_list)

for i in left_list:
    similarity_score += i * right_count.get(i, 0)

print(similarity_score)

#Correct Answer: 21142653