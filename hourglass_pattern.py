# * * * * * * 
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *

#to take the number of columns as an input from the user
n=int(input())
#upper half of the hourglass pattern
#loop for rows in the upper half of the hourglass pattern
for i in range(1,n+1):
    #loop for rows in the upper half of the hourglass pattern
    for j in range(i-1):
        print(" ",end="")
    #for printing the "*" in the upper half of the hourglass pattern
    for k in range((n+1)-i):
        print("* ",end="")
    #for moving the pointer to the new line
    print()

#lower half of the hourglass pattern
#number of rows decrease by 1 for the lower half of the hourglass pattern
m=n-1
#loop for rows in the lower half of the hourglass pattern
for i in range(1,m+1):
    #loop for rows in the lower half of the hourglass pattern
    for j in range(1,(m-i)+1):
        print(" ",end="")
    #for printing the "*" in the lower half of the hourglass pattern
    for k in range(1,(i+2)):
        print("* ",end="")
    #for moving the pointer to the new line
    print()