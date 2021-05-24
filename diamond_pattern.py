#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

#for taking input from user
n=int(input())
#first half of diamond
#loop for colunmn on upper diamond pattern
for i in range(1,n+1):
    #loop for printing the spaces on the top left quadrant
    for j in range(n-i):
        print(" ",end="")
    #loop to print "*" on the top left quadrant
    for k in range(i):
        print("*",end="")
    #loop to print "*" on top right quadrant
    for l in range(i-1):
        print("*",end="")
    #to move to the next line
    print()

#second half of diamond pattern
#decresing the value of n since the number or rows will be decreased by 1 for bottom half od diamond pattern
n2=n-1
#loop for colunmn on bottom diamond pattern
for i in range(n2):
    #loop for printing the spaces on the bottom left quadrant
    for j in range(i+1):
        print(" ",end="")
    #loop to print "*" on the top left quadrant
    for k in range(n2,0,-1):
        print("*",end="")
    #loop to print "*" on top right quadrant
    for k in range(n2-1):
        print("*",end="")
    #decresing the value of n2 by 1 to work with negative indexes on for loop
    n2-=1
    #to move to the next line
    print()