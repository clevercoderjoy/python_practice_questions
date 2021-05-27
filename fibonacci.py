#taking number of terms to print as an input from the user
n=int(input())
#since the first and second terms are always 0 and 1
num1=0
num2=1
sum=0
#printing the first 2 terms
print(num1,end=" ")
print(num2,end=" ")
#looping over the rest of the terms
for i in range(n-2):
    #next number is always the sum of the previous 2 numbers
    sum=num1+num2
    #printing the next number
    print(sum,end=" ")
    #changing the numbers as the next terms are derived by previous terms
    num1=num2
    num2=sum
print()
#printing the nth term
print(sum)