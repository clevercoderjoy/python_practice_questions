row1 = int(input("Enter row 1: \n"))
col1 = int(input("Enter col 1: \n"))
m1 = [[int(i) for i in input().split()] [ : col1] for j in range(row1)]

print("m1: \n")
for row in m1:
    print(row)

ans = []
for i in range(col1):
    temp = []
    for j in range(row1):
        temp.append(0)
    ans.append(temp)

print("ans: \n")
for row in ans:
    print(row)

for i in range(col1):
    for j in range(row1):
        ans[i][j] = m1[j][i]

print("ans: \n")
for row in ans:
    print(row)