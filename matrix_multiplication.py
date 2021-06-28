row1 = int(input("Enter row 1: \n"))
col1 = int(input("Enter col 1: \n"))
m1 = [[int(i) for i in input().split()] [ : col1] for j in range(row1)]
print("m1: \n")
for row in m1:
    print(row)

row2 = int(input("Enter row 2: \n"))
col2 = int(input("Enter col 2: \n"))
m2 = [[int(i) for i in input().split()] [ : col2] for j in range(row2)]
print("m2: \n")
for row in m2:
    print(row)

ans = []
for i in range(row1):
    temp = []
    for j in range(col2):
        temp.append(0)
    ans.append(temp)

print("ans: \n")
for row in ans:
    print(row)

for i in range(len(ans)):
    for j in range(len(ans[0])):
        for k in range(len(m2)):
            ans[i][j] += m1[i][k] * m2[k][j]

print("ans: \n")
for row in ans:
    print(row)