def print_spiral_matrix(arr, row, col):
    top = 0
    bottom = row - 1
    left = 0
    right = col - 1
    dir = 0
    while (top <= bottom and left <= right):
        if dir == 0:
            for i in range(left, right + 1):
                print(arr[top][i], end = " ")
            top += 1
            dir = 1
        elif dir == 1:
            for i in range(top, bottom + 1):
                print(arr[i][right], end = " ")
            right -= 1
            dir = 2
        elif dir == 2:
            for i in range(right, left - 1, -1):
                print(arr[bottom][i], end = " ")
            bottom -= 1
            dir = 3
        elif dir == 3:
            for i in range(bottom, top -1, -1):
                print(arr[i][left], end = " ")
            left += 1
            dir = 0

row = int(input())
col = int(input())
arr = [[int(ele) for ele in input().split()] [ : row] for i in range(col)]
print_spiral_matrix(arr, row, col)