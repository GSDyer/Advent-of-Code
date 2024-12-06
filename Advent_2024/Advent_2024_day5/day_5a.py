import time
start_time = time.time()
file_name = "input2024_5.txt"

instructions = []
update_list = []

with open(file_name, "r") as file:
    for line in file:
        line = line.strip()
        if "|" in line:
            instructions.append(tuple(map(int, line.split("|"))))
        elif "," in line:
            update_list.append(tuple(map(int, line.split(","))))
        else:
            continue

approved_updates = []

for update in range(len(update_list)):
    Flag_update = True
    for i in range(len(update_list[update]) - 1):
        if Flag_update == False:
            break
        for j in range(i, len(update_list[update]) -1):
            if (update_list[update][j+1], update_list[update][i]) in instructions:
                Flag_update = False
                break
    if Flag_update == True:
        approved_updates.append(update_list[update])
        
middle_sum = 0
for i in range(len(approved_updates)):
    middle_index = int((len(approved_updates[i]) - 1) / 2)
    middle_sum += approved_updates[i][middle_index]
    
print(middle_sum)
#Correct Answer 6505
end_time = time.time()
print(f"Run time was {end_time - start_time} seconds")