'''
#Pattern 1:
# A
# B C
# C D E
# D E F G

#number of rows
n=int(input("Enter the number of rows: \n"))
i=1
#looping until user entered limit is reached
while i<=n:
    p=i
    j=1
    #looping until j is not eq to i
    while j<=i:
        #using chr to convert from ascii to character value and ord to convert from character to ascii value
        print(chr(ord('A')+p-1),end=" ")
        j+=1
        p+=1
    print()
    i+=1

#new line
print()

#Pattern 2:
# E 
# D E
# C D E
# B C D E
# A B C D E

#number of rows
n=int(input("Enter the number of rows: \n"))
i=1
p=n
#looping until user entered limit is reached
while i<=n:
    j=1
    #looping until j is not eq to i
    while j<=i:
        #using chr to convert from ascii to character value and ord to convert from character to ascii value
        print(chr(ord('A')+p-1),end=" ")
        p+=1
        j+=1
    print()
    p=n-i
    i+=1

#new line
print()

#Pattern 3:
# 1
# 1 1
# 2 0 2
# 3 0 0 3

#number of rows
n=int(input("Enter the number of rows: \n"))
print('1')
i=2
while i<=n:
    j=1
    while j<=i:
        if j==1 or j==i:
            print(i-1,end=" ")
        else:
            print(0,end=" ")
        j+=1
    i+=1
    print()

#new line
print()

#Pattern 4:
# 1
# 1 1
# 1 2 1
# 1 2 2 1

#number of rows
n=int(input("Enter the number of rows: \n"))
print(1)
i=2
while i<=n:
    j=1
    while j<=i:
        if j==i or j==1:
            print(1,end=" ")
        else:
            print(2,end=" ")
        j+=1
    print()
    i+=1

#new line
print()

#Pattern 5:
# 1 2 3 4 
# 1 2 3
# 1 2
# 1

#number of rows
n=int(input("Enter the number of rows: \n"))
i=n
while i>=1:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i-=1

#new line
print()

#Pattern 6:
#       1
#     2 3 2
#   3 4 5 4 3
# 4 5 6 7 6 5 4

#number of rows
n = int(input("Enter the number of rows: \n"))
row = 1
#for rows
while row <= n:
    #for spaces
    spaces = 1
    while spaces <= (n-row):
        print(" ", end = " ")
        spaces += 1
    #for values at left side
    col = 1
    value_to_print = row
    while col <= row:
        print(value_to_print, end = " ")
        col += 1
        value_to_print += 1
    #for values at the right side
    col = 1
    value_to_print = 2 * row - 2
    while col <= (row - 1):
        print(value_to_print, end = " ")
        col += 1
        value_to_print -= 1
    print()
    row += 1

#new line
print()

#Pattern 7:
# *
#  * *
#    * * *
#      * * * *
#    * * *
#  * *
# *

#limit
n = int(input("Enter the number of rows: \n"))
#for upper rows
row_up = 1
while row_up <= n:
    #for spaces
    col_up = 1
    while col_up <= (row_up-1):
        print(" ", end = " ")
        col_up += 1
    #for *
    col_up = 1
    while col_up <= row_up:
        print("* ", end = " ")
        col_up +=1
    print()
    row_up += 1
#for lower limit
m = n-1
row_down = 1
#for lower rows
while row_down <= m:
    #for lower spaces
    col_down = 1
    while col_down <= (m-row_down):
        print(" ", end = " ")
        col_down += 1
    #for lower *
    col_down = m - (row_down - 1)
    while col_down >= 1:
        print("* ", end = " ")
        col_down -= 1
    print()
    row_down += 1

#new line
print()

#Pattern 8:
# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444

#limit
n = int(input("Enter the number of rows: \n"))
#for rows
for row in range(1, 2 * n):
    value_to_print = n
    #for upper half of square
    if (row <= n):
        #for columns in the upper half
        for col_1 in range(1, 2 * n):
            print(value_to_print, end = " ")
            if (row > col_1):
                value_to_print -= 1
            elif ((row + col_1) >= (2 * n)):
                value_to_print += 1
    #for lower half of the square
    if (row > n):
        #for columns in the lower half
        for col_2 in range(1, 2 * n):
            print(value_to_print, end = " ")
            if ((row + col_2) < (2 * n)):
                value_to_print -= 1
            elif (col_2 >= row):
                value_to_print += 1
    print()
'''

#new line
print()

#limit
n = int(input("Enter the number of rows: \n"))

