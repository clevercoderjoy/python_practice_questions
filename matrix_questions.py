def m_add(m):
    for i in m:
        ans = 0
        for j in i:
            ans += j
        print(ans, end = " ")

size_r = int(input())
size_c = int(input())
m = [[int(i) for i in input().split()][ : size_r] for j in range(size_c)]
m_add(m)

def m_sub(m):
    for i in m:
        ans = 0
        for j in i:
            ans -= j
        print(ans)

size_r = int(input())
size_c = int(input())
m = [[int(i) for i in input().split()] [ : size_r] for j in range(size_c)]
m_sub(m)

def add_2_mat(m1, m2):
    ans = []
    for i in range(len(m1)):
        s = []
        for j in range(len(m1[i])):
            s.append(m1[i][j] + m2[i][j])
        ans.append(s)
    return ans

size_r = int(input())
size_c = int(input())
m1 = [[int(i) for i in input().split()] [ : size_r] for j in range(size_c)]
m2 = [[int(i) for i in input().split()] [ : size_r] for j in range(size_c)]
output = add_2_mat(m1, m2)
print()
for i in range(len(m1)):
    for j in range(len(m1[i])):
        print(output[i][j], end = " ")
    print()

def sub_2_mat(m1, m2):
    ans = []
    for i in range(len(m1)):
        s = []
        for j in range(len(m1[i])):
            s.append(m1[i][j] - m2[i][j])
        ans.append(s)
    return ans

size_r = int(input())
size_c = int(input())
m1 = [[int(i) for i in input().split()] [ : size_r] for j in range(size_c)]
m2 = [[int(i) for i in input().split()] [ : size_r] for j in range(size_c)]
output = sub_2_mat(m1, m2)
print()
for i in range(len(m1)):
    for j in range(len(m1[i])):
        print(output[i][j], end = " ")
    print()

def c_add(m, size_r, size_c):
    ans = []
    for i in range(size_r):
        total = 0
        for j in range(size_c):
            total += m[i][j]
        ans.append(total)
    return ans

size_r = int(input())
size_c = int(input())
m = [[int(i) for i in input().split()][ : size_r] for j in range(size_c)]
print(c_add(m, size_r, size_c))

def find_largest(arr, rows, cols):
    index = -1
    largest = 0
    is_row = True
    for i in range(rows):
        row_sum = 0
        for j in range(cols):
            row_sum += arr[i][j]
        if row_sum > largest:
            largest = row_sum
            index = i
    for i in range(cols):
        col_sum = 0
        for j in range(rows):
            col_sum += arr[j][i]
        if col_sum > largest:
            largest = col_sum
            index = j
            is_row = False
    if is_row:
        return index, row_sum
    else:
        return index, col_sum

rows = int(input())
cols = int(input())
arr = [[int(i) for i in input().split()] [ : rows] for j in range(cols)]
print(find_largest(arr, rows, cols))