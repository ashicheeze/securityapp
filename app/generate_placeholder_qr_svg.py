import random

SIZE = 21
MODULE_SIZE = 10

# create blank matrix
matrix = [[0]*SIZE for _ in range(SIZE)]

def add_finder_pattern(r, c):
    pattern = [
        [1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1],
    ]
    for i in range(7):
        for j in range(7):
            matrix[r+i][c+j] = pattern[i][j]

# add finder patterns
add_finder_pattern(0,0)
add_finder_pattern(0,SIZE-7)
add_finder_pattern(SIZE-7,0)

# add timing patterns
for i in range(8, SIZE-8):
    matrix[6][i] = (i % 2)
    matrix[i][6] = (i % 2)

# fill remaining area randomly
for r in range(SIZE):
    for c in range(SIZE):
        if matrix[r][c] == 0:
            matrix[r][c] = random.randint(0,1)

# output SVG
print('<svg xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 {s} {s}">'.format(s=SIZE*MODULE_SIZE))
print('<rect width="100%" height="100%" fill="white"/>')
for r,row in enumerate(matrix):
    for c,val in enumerate(row):
        if val:
            x = c*MODULE_SIZE
            y = r*MODULE_SIZE
            print('<rect x="{}" y="{}" width="{}" height="{}" fill="black"/>'.format(x, y, MODULE_SIZE, MODULE_SIZE))
print('</svg>')
