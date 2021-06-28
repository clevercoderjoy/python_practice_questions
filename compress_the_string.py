# Compress the String

# Write a program to do basic string compression.
# For a character which is consecutively repeated more than once, replace consecutive duplicate occurrences with the count of repetitions.
# Example:
# If a string has 'x' repeated 5 times, replace this "xxxxx" with "x5".

# The string is compressed only when the repeated character count is more than 1.
# Note :
# Consecutive count of every character in the input string is less than or equal to 9.
# Input Format:
# The first and only line of input contains a string without any leading and trailing spaces.
# Output Format:
# The only line of output prints the updated string.
# Note:
# You are not required to print anything. It has already been taken care of.
# Constraints:
# 0 <= N <= 10^6
# Where N is the length of the input string.

# Time Limit: 1 second
# Sample Input 1:
# aaabbccdsa
# Sample Output 1:
# a3b2c2dsa
# Sample Input 2:
# aaabbcddeeeee
# Sample Output 2:
# a3b2cd2e5

def compress(given_string):
    if len(given_string) <= 1:
        return given_string
    else:
        start_index = 0
        end_index = 0
        ans = ""
        count = 0
        for i in range(len(given_string) - 1):
            if given_string[i] == given_string[i + 1]:
                end_index += 1
            elif given_string[i] != given_string[i + 1]:
                end_index += 1
                count = end_index - start_index
                if count > 1:
                    ans = ans + given_string[i] + str(count)
                else:
                    ans = ans + given_string[i]
                start_index = i
                end_index = i
    if given_string[-1] == given_string[-2]:
        return ans + given_string[i] + (str((end_index - start_index) + 1))
    else:
        return ans + given_string[-1]

given_string = input()
print(compress(given_string))