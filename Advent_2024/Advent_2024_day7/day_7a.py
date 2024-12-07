file_path = "input2024_7.txt"

with open(file_path, "r") as file:
    inputs = [(int(left.strip()), [int(x) for x in right.strip().split()])
              for left, right in (line.split(':') for line in file)]
    
def is_valid(answer, current, rest):
    if current > answer:
        return False
    if len(rest) == 0:
        return answer == current
    return (is_valid(answer, current + rest[0], rest[1:]) or
            is_valid(answer, current * rest[0], rest[1:]))

print(sum(answer for answer, numbers in inputs if is_valid(answer, numbers[0], numbers[1:])))
#Correct Answer: 12839601725877