# 1=>

# # Ref link: https://www.youtube.com/watch?v=0DnG0Kc9M2E

# def diagonal_matrix_traversal(mat, rows, cols):
#     if not mat or not mat[0]:
#         return []
#     diagonals = [[] for i in range(rows + cols - 1)]
#     for i in range(rows):
#         for j in range(cols):
#             diagonals[i + j].append(mat[i][j])
#     res = diagonals[0]
#     for i in range(1, len(diagonals)):
#         if i % 2 != 0:
#             res.extend(diagonals[i])
#         else:
#             res.extend(diagonals[i][ : : -1])
#     return res

# rows = int(input())
# cols = int(input())
# arr = [[int(i) for i in input().split()] [ : rows] for j in range(cols)]
# print(*(diagonal_matrix_traversal(arr, rows, cols)))

# 2=>

# Last Substring in Lexicographical Order
# Hard

# Given a string s, return the last substring of s in lexicographical order.

# Example 1:

# Input: s = "abab"
# Output: "bab"
# Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
# Example 2:

# Input: s = "leetcode"
# Output: "tcode"

# Constraints:
# 1 <= s.length <= 4 * 105
# s contains only lowercase English letters.

# def lg_order(string):
#     maxChar = 'a'
#     index = []
#     for i in range(len(string)):
#         if (string[i] >= maxChar):
#             maxChar = string[i]
#             index.append(i)
#     maxString = ""
#     for i in range(len(index)):
#         if (string[index[i] : len(string)]) > maxString:
#             maxString = string[index[i] : len(string)]
#     return maxString

# string = input()
# print(lg_order(string))

# 3=>


import random

print(random.randint(1,2))