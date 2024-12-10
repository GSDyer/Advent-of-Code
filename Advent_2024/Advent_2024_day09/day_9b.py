file_name = "input2024_9.txt"

def calc_solution(disk_file):
    solution = 0
    for index, data in enumerate(disk_file):
        if data != 0:
            solution += (data - 1) * (index)
    return solution

disk_file = []
with open(file_name, "r") as file:
    for index, char in enumerate(file.read()):
        if index%2 == 0:
            disk_file.append((int(index/2) + 1, int(char)))
        else:
            disk_file.append((0, int(char)))

additions = []
for index, (data, size) in enumerate(disk_file[::-1]):
    if data != 0:
        for zero_index, (zero_data, zero_size) in enumerate(disk_file):
            if zero_data == 0 and zero_size >= size and zero_index < len(disk_file) - 1 - index:
                disk_file[len(disk_file) - 1 - index] = (zero_data, size)
                disk_file[zero_index] = (zero_data, zero_size - size)
                additions.append((zero_index, (data, size)))
                break
        continue

sorted_additions = sorted(additions, key=lambda x: x[0])

for index, (data, size) in sorted_additions[::-1]:
    disk_file.insert(index, (data, size))

expanded_disk = []
for data, size in disk_file:
    for i in range(size):
        expanded_disk.append(data)

print(calc_solution(expanded_disk))
#Correct Answer: 6363913128533
#Inefficient during nested for loops, currently O(n^2) but could be reduced
#Also using just one list containing data, size for both numbers and '.' was a mistake