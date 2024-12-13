import re

file_name = "input2024_13.txt"

with open(file_name) as file:
    instructions = file.read()

token_total = 0

for line in instructions.split('\n\n'):
    a_text, b_text, prize_text = line.split('\n')
    button_a = [int(num) for num in re.findall(r'\d+', a_text)]
    button_b = [int(num) for num in re.findall(r'\d+', b_text)]
    prize = [int(num) for num in re.findall(r'\d+', prize_text)]
    prize[0], prize[1] = prize[0] + 10000000000000, prize[1] + 10000000000000
    a1, a2, b1, b2, c1, c2 = button_a[0], button_a[1], button_b[0], button_b[1], prize[0], prize[1]
    A = ((c1*b2) - (b1*c2)) / ((a1*b2) - (b1*a2))
    B = ((a1*c2) - (c1*a2)) / ((a1*b2) - (b1*a2))
    if A.is_integer() and B.is_integer():
        token_total += int(((A*3) + B))

print(token_total)
#Correct Answer: 94955433618919