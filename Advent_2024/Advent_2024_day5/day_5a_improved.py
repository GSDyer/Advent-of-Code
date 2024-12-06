"""Previous 5a worked, but was very inefficient and hard to read. This attempt
will use sets to reduce lookup time, as well as try to remove the nested for 
loops which take way to long to run. Also by using the all function we remove
the need for multiple break statements in those loops, which was quite 
confusing to read.
Also by making these changes, it provides a better launch pad for trying to
solve part b which I still haven't got my head around yet and this is good
procrastination"""
import time
start_time = time.perf_counter()
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
                update_list.append(tuple(map(int, line.split(","))))
            else:
                continue    
    return instructions, update_list

def is_update_approved(update, instructions):
    return all(
        (update[j+1], update[i]) not in instructions
        for i in range(len(update) - 1)
        for j in range(i, len(update) -1)
        )

def calculate_middle_sum(approved_updates):
    return sum(
        update[int((len(update) -1)/2)]
        for update in approved_updates
        )

#Main code

instructions, update_list = read_file(file_name)

approved_updates = [
    update for update in update_list
    if is_update_approved(update, instructions)
    ]
middle_sums = calculate_middle_sum(approved_updates)
print(middle_sums)
#Correct answer 6505
end_time = time.perf_counter()
print(f"Run time was {end_time - start_time} seconds")
#It's roughly 130 times faster than attempt A (thanks chatGPT for your insight)