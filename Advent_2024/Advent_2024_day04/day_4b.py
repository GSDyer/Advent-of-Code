file_path = "input2024_4.txt"

wordsearch = open(file_path).read().splitlines()
target_word = "MAS"

columns = len(wordsearch[0])
rows = len(wordsearch)

def is_valid_position(x, y):
    """Checks whether the coordinate passed in is still within our wordsearch"""
    return 0 <= x < columns and 0 <= y < rows

def check_for_target_word(x, y):
    """From the target position, we check to see if the four diagonals are in
    a suitable combination to achieve our target "word"."""
    count = 0
    directions = [(1, 1), #Down-Right
                  (1, -1), #Down-Left
                  (-1, 1), #Up-Right
                  (-1, -1)] #Up-Left
    candidate_solution = ""
    solutions = ["MMSS", "MSMS", "SMSM", "SSMM"]
    for dy, dx in directions:
        if is_valid_position(x + dx, y + dy):
            candidate_solution += wordsearch[y + dy][x + dx]
    if candidate_solution in solutions:
        count += 1
    return count

"""Every time we find the middle letter of target word (here it is A) in 
wordsearch we use check_target_word to see if there are any valid words from
this position."""
total_target_words = 0
for y in range(rows):
    for x in range(columns):
        if wordsearch[y][x] == target_word[1]:
            total_target_words += check_for_target_word(x, y)

print(total_target_words)
#Correct Answer: 1807