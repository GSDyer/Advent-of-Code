file_path = "input2024_4.txt"

wordsearch = open(file_path).read().splitlines()
target_word = "XMAS"

columns = len(wordsearch[0])
rows = len(wordsearch)

def is_valid_position(x, y):
    """Checks whether the coordinate passed in is still within our wordsearch"""
    return 0 <= x < columns and 0 <= y < rows

def check_for_target_word(x, y):
    """Finds what the words are in all 8 cardinal directions from input
    coordinates with same length to our target word, and if they are equal to
    target word increase count. Returns how many target words are found from
    the input coordinates."""
    count = 0
    directions = [(0, 1), #Right
                  (0, -1), #Left
                  (1, 0), #Down
                  (-1, 0), #Up
                  (1, 1), #Down-Right
                  (1, -1), #Down-Left
                  (-1, 1), #Up-Right
                  (-1, -1)] #Up-Left
    for dy, dx in directions:
        if is_valid_position(x + dx*(len(target_word)-1), y + dy*(len(target_word)-1)):
            candidate_solution = "".join(
                wordsearch[y + dy*i][x + dx*i] for i in range(len(target_word)))
            if candidate_solution == target_word:
                count += 1
    return count

"""Every time we find the first letter of target word in wordsearch we use
check_target_word to see if there are any valid words from this position."""
total_target_words = 0
for y in range(rows):
    for x in range(columns):
        if wordsearch[y][x] == target_word[0]:
            total_target_words += check_for_target_word(x, y)

print(total_target_words)
#Correct Answer: 2406