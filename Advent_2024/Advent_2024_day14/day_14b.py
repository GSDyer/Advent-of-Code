import re
import matplotlib.pyplot as plt

file_name = "input2024_14.txt"

def guards_image(guards):
    """Create image to look for easter egg image"""
    x_coords = [value[0] for value in guards.values()]
    y_coords = [value[1] for value in guards.values()]
    plt.figure(figsize=(8, 6))
    plt.scatter(x_coords, y_coords, color='blue')
    plt.xlim(0, x_len)
    plt.ylim(0, y_len)
    plt.title(iteration)
    plt.show()
    
#Grid size
x_len = 101
y_len = 103    
guards = dict()  # x, y, move_x, move_y

with open(file_name, "r") as file:
    for y, line in enumerate(file):
        guard = tuple(int(num) for num in re.findall(r'-?\d+', line))
        guards[y] = guard

iteration = 0
search_string = '#######'

for i in range(10000):
    iteration += 1 # Keep track of how many seconds passed
    for guard, stats in guards.items(): #Update guards moving
        x, y, mov_x, mov_y = stats
        new_stats = ((x + mov_x) % x_len, (y + mov_y) % y_len, mov_x, mov_y)
        guards[guard] = new_stats
        
    grid = [['.' for _ in range(x_len)] for _ in range(y_len)]
    for guard, stats in guards.items():
        x, y, mov_x, mov_y = stats
        grid[y][x] = '#'   # Create matrix representation of guards to look for pattern
        
    for row in grid:      # Whenever search pattern found, create an image.
        row_string = ''.join(row)
        if search_string in row_string:
            guards_image(guards)
#This prints 21 images. 3 are incorrect, but the other 18 are all of our easter egg on loop 7138.
#Correct Answer: 7138