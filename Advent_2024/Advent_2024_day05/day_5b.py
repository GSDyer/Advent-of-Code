file_name = "input2024_5.txt"

def read_file(file_name):
    instructions = set()
    update_list = []
    
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if "|" in line:
                instructions.add(tuple(map(int, line.split("|"))))
            elif "," in line:
                update_list.append(list(map(int, line.split(","))))
            else:
                continue    
    return instructions, update_list

def is_update_approved(update, instructions):
    return all(
        (update[j+1], update[i]) not in instructions
        for i in range(len(update) - 1)
        for j in range(i, len(update) -1)
        )

def is_update_not_approved(update, instructions):
    return any(
        (update[j+1], update[i]) in instructions
        for i in range(len(update) - 1)
        for j in range(i, len(update) -1)
        )

def reorder_update(update, instructions):
    """Should have error handling to prevent cycling"""
    while(is_update_not_approved(update, instructions)):
        for i in range(len(update) - 1):
            for j in range(i, len(update) -1):
                if (update[j+1], update[i]) in instructions:
                    update[j+1], update[i] = update[i], update[j+1]
    return update

def calculate_middle_sum(corrected_updates):
    return sum(
        update[int((len(update) -1)/2)]
        for update in corrected_updates
        )

#Main code

instructions, update_list = read_file(file_name)

incorrect_updates = [
    update for update in update_list
    if is_update_not_approved(update, instructions)
    ]

corrected_updates = []
for update in incorrect_updates:
    corrected_updates.append(reorder_update(update, instructions))

middle_sums = calculate_middle_sum(corrected_updates)
print(middle_sums)
#Correct Answer: 6897
