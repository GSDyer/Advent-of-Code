file_path = "Input2024_2.txt"

safe_reports = 0

with open(file_path, "r") as file:
    for line in file:
        data = list(map(int, line.split()))        
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
        if adjacent_safe is True and is_increasing != is_decreasing:
            safe_reports += 1
            
print(safe_reports)

#Correct Answer: 411