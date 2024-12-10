import re

file_path = "input2024_3.txt"

def mul(x, y):
    return x * y

with open(file_path, "r") as file:
    memory = file.read()
    
pattern = r"mul\(\d{1,3},\s?\d{1,3}\)"
#searches for mul( followed by a 1-3 digit number, followed by a "," and 
#optional space, followed by a 1-3 digit number, follow by a ")"

valid_calls = re.findall(pattern, memory)

mul_additions = 0

for i in valid_calls:
    mul_additions += eval(i)  #run all the functions in the valid_calls list

print(mul_additions)

#Correct answer: 161289189