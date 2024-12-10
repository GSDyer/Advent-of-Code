file_path = "Input2024_2.txt"

safe_reports = 0

def is_safe(data):
        is_increasing = True
        is_decreasing = True
        adjacent_safe = True
        for i in range(1, len(data)):
            if data[i] > data[i-1]:
                is_decreasing = False
            if data[i-1] > data[i]:
                is_increasing = False
            if not (1 <= abs(data[i] - data[i-1]) <= 3):
                adjacent_safe = False
        return adjacent_safe and is_increasing != is_decreasing

with open(file_path, "r") as file:
    for line in file:
        data = list(map(int, line.split()))       
        #checking whether original sequence works
        if is_safe(data):
            safe_reports += 1
            continue
        #remove one item at a time for unsafe lists to see if it works
        for i in range(len(data)):
            amended_data = data[:i] + data[i + 1:]
            if is_safe(amended_data):
                safe_reports += 1
                break
                 
print(safe_reports)

#Correct Answer: 465