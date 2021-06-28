# Ref link: https://www.youtube.com/watch?v=0DnG0Kc9M2E

def diagonal_matrix_traversal(mat, rows, cols):
    if not mat or not mat[0]:
        return []
    diagonals = [[] for i in range(rows + cols - 1)]
    for i in range(rows):
        for j in range(cols):
            diagonals[i + j].append(mat[i][j])
    res = diagonals[0]
    for i in range(1, len(diagonals)):
        if i % 2 != 0:
            res.extend(diagonals[i])
        else:
            res.extend(diagonals[i][ : : -1])
    return res

rows = int(input())
cols = int(input())
arr = [[int(i) for i in input().split()] [ : rows] for j in range(cols)]
print(*(diagonal_matrix_traversal(arr, rows, cols)))
