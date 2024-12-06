import re

file_path = "input2024_3.txt"

def mul(x, y):
    return x * y

with open(file_path, "r") as file:
    memory = file.read()
    
pattern = r"mul\(\d{1,3},\s?\d{1,3}\)|do\(\)|don't\(\)"
#searches for mul( followed by a 1-3 digit number, followed by a "," and 
#optional space, followed by a 1-3 digit number, follow by a ")". Also searches
#for do() and don't() functions

valid_calls = re.findall(pattern, memory)

sum_multiplications = 0

enabled = True

for i in valid_calls:
    if i == "do()":
        enabled = True
    elif i == "don't()":
        enabled = False
    else:
        if enabled:
            sum_multiplications += eval(i)
            
print(sum_multiplications)

#Correct answer: 83595109
