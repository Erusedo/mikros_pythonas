#how to create 2d list
number_grid = [       
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#how to print something from 2d list
print(number_grid[0][1])

#nested loops

for row in number_grid: #print col
    for col in row:
        print(col)

for row in number_grid: #print table as it is
    print(row)

# row & col