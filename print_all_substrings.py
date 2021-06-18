# All substrings
# Difficulty: EASY
# Problem Statement
# For a given input string(str), write a function to print all the possible substrings.
# Substring
# A substring is a contiguous sequence of characters within a string. 
# Example: "cod" is a substring of "coding". Whereas "cdng" is not as the characters taken are not contiguous
# Input Format:
# The first and only line of input contains a string without any leading and trailing spaces.
# All the characters in the string would be in lower case.
# Output Format:
# Print all the substrings possible, where every substring is printed on a separate line.
# Note:
# The order in which the substrings are printed does not matter.
# Constraints:
# 0 <= N <= 10^6
# Where N is the length of the input string.

# Time Limit: 1 second
# Sample Input 1:
# abc
# Sample Output 1:
# a 
# ab 
# abc 
# b 
# bc 
# c 
# Sample Input 2:
# co
# Sample Output 2:
# c 
# co 
# o

def substrings(string):
    for i in range(len(string)):
        temp = ""
        for j in range(i, len(string)):
            temp += string[j]
            print(temp)

string = input()
substrings(string)