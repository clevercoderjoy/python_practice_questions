# Highest Occuring Character

# For a given a string(str), find and return the highest occurring character.
# Example:
# Input String: "abcdeapapqarr"
# Expected Output: 'a'
# Since 'a' has appeared four times in the string which happens to be the highest frequency character, the answer would be 'a'.
# If there are two characters in the input string with the same frequency, return the character which comes first.
# Consider:
# Assume all the characters in the given string to be in lowercase always.
# Input Format:
# The first and only line of input contains a string without any leading and trailing spaces.
# Output Format:
# The only line of output prints the updated string. 
# Note:
# You are not required to print anything explicitly. It has already been taken care of.
# Constraints:
# 0 <= N <= 10^6
# Where N is the length of the input string.

# Time Limit: 1 second
# Sample Input 1:
# abdefgbabfba
# Sample Output 1:
# b
# Sample Input 2:
# xy
# Sample Output 2:
# x

def highest_occurring_character(given_string):
  if len(given_string) <= 2:
    return given_string[0]
  else:
    hocc = 0
    hoc = ""
    for i in range(len(given_string) - 1):
      if given_string[i] != given_string[i + 1]:
        if hocc < given_string.count(given_string[i]):
          hocc = given_string.count(given_string[i])
          hoc = given_string[i]
      else:
        given_string = given_string.replace(i, '')
  return hoc

given_string = input()
print(highest_occurring_character(given_string))