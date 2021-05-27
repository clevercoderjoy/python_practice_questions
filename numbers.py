#taking input from user
num=int(input())
#emrip number: number which is prime when read backwards and frontwards
#storing the number in a variable
n=num
#setting emrip to none initially
emrip=None
#a function to check if the number is prime before reversing it
def prime_check(n):
    #calling the global variables
    global emrip
    #loop to traverse through the numbers except for 1 and the number itself
    for i in range(2,n):
        #checking if any factor exists apart from1 and the number itself
        if n%i==0:
            #setting emrip to false if there a factor is found
            emrip=False
#a function to check if the number is an emrip number or not
def check(n):
    #calling the function to check if the number is prime or not
    prime_check(n)
    #checking if emrip is still false to check further condition
    if emrip is not False:
        #setting sum to 0
        sum=0
        #a loop to reverse the number entered by the user to check if it is a prime number or not
        while n!=0:
            sum=sum*10+(n%10)
            n//=10
        #calling the function to check prime again for the reversed number
        prime_check(n)
#main function
check(n)
#setting emrip to true if the number and it's reversed both are prime
if emrip is not False:
    emrip=True
#printing if the number is emrip or not
print("emrip: ", emrip)

#new line
print()

#Harshad/ Niven Number: an integer that is divisible by the sum of its digits

#storing the number in a variable
n=num
#storing the copy of the number in a variable
n2=num
s=0
#setting harshad to none initially
harshad=None
#function to get the sum of digits of the number entered by the user
def s_o_d(n):
    #calling global variables
    global s
    while n!=0:
        s=s+(n%10)
        n//=10
#function to check if the number is divisible by it's sum of digits
def check_divisible(n2):
    #calling global variables
    global harshad
    global s
    #setting harshad to true if the number is divisible by it's sum of digits
    if n2%s==0:
        harshad=True
#function to check harshad
def check_harshad(n2):
    s_o_d(n)
    check_divisible(n2)
#main function
check_harshad(n)
#setting harshad to false if the number is not divisible by the sum of it's digits
if harshad is not True:
    harshad=False
#printing if the number is harshad or not
print("harshad: ", harshad)

#new line
print()

#Disarum Number:if sum of its digits powered with their respective position is equal to the original number.

#storing the the number in a variable
n=num
#storing the copy of the number in a variable
n1=num
count=0
#counting the number of digits in the number entered
while n!=0:
    count+=1
    n=n//10
#setting sum to 0
sum=0
#adding each digit raised to the power of it's position
while n1!=0:
    sum=sum+((n1%10)**count)
    n1//=10
    #reducting the value of count after each iteration
    count-=1
#printing the result after checking if the the number is disarum or not
if sum==num:
    print("Disarm: ",True)
else:
    print("Disarm: ",False)

#new line
print()

#Automorphic Number:a number which is present in the last digit(s) of its square
#storing the the number in a variable
n=num
#squaring the number
sq=n**2
#checking if the last digit of squared number is equal to the number entered
if sq%10==n:
    print("Automorphic number: ",True)
else:
    print("Automorphic number: ",False)

#new line
print()

#storing the the number in a variable
n=num
#setting s to 0
s=0
#reversing the number
while n!=0:
    s=s*10+(n%10)
    n//=10
#checking if the number reversed is same as the original number or not
if s==num:
    print("Palindrone number: ",True)
else:
    print("Palindrone number: ",False)

#new line
print()

#Special Number:A number is said to be special number when the sum of factorial of its digits is equal to the number itself

#storing the the number in a variable
n=num
#setting sum to 0
sum=0
#loop to fetch the last digit
while n:
    r=n%10
    f=1
    #fetching factorial of last digit
    for i in range(1,r+1):
        f=f*i
    #adding the factorial to the sum
    sum+=f
    n=n//10
#checking if the number is a special number or not
if sum==num:
    print("special number: ",True)
else:
    print("special number: ",False)

#new line
print()

#A number is said to be a Neon Number if the sum of digits of the square of the number is equal to thenumber itself
#storing the the number in a variable
n=num
#setting sum to 0
sum=0
#squaring the number entered
sq=n**2
#loop to add each digit to sum
while sq!=0:
    sum=sum+(sq%10)
    sq//=10
#checking if the number is a neon number or not
if sum==n:
    print("neon number: ",True)
else:
    print("neon number: ",False)