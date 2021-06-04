# Array Intersection

# You have been given two integer arrays/list(ARR1 and ARR2) of size M and N, respectively. You need to print their intersection; An intersection for this problem can be defined when both the arrays/lists contain a particular value or to put it in other words, when there is a common value that exists in both the arrays/lists.
# Note :
# Input arrays/lists can contain duplicate elements.

# The intersection elements printed would be in the order they appear in the first array/list(ARR1)


# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# First line of each test case or query contains an integer 'N' representing the size of the first array/list.

# Second line contains 'N' single space separated integers representing the elements of the first the array/list.

# Third line contains an integer 'M' representing the size of the second array/list.

# Fourth line contains 'M' single space separated integers representing the elements of the second array/list.
# Output format :
# For each test case, print the intersection elements in a row, separated by a single space.

# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^5
# 0 <= M <= 10^5
# Time Limit: 1 sec 
# Sample Input 1 :
# 2
# 6
# 2 6 8 5 4 3
# 4
# 2 3 4 7 
# 2
# 10 10
# 1
# 10
# Sample Output 1 :
# 2 4 3
# 10
# Sample Input 2 :
# 1
# 4
# 2 6 1 2
# 5
# 1 2 3 4 2
# Sample Output 2 :
# 2 1 2
# Explanation for Sample Output 2 :
# Since, both input arrays have two '2's, the intersection of the arrays also have two '2's.
# The first '2' of first array matches with the first '2' of the second array.
# Similarly, the second '2' of the first array matches with the second '2' if the second array.

def array_intersection(arr_1, arr_2, intersection_array):
    # taking index as -1 initially
    index=-1
    # iterating over the first array
    for element in arr_1:
        # checking if the element in the first array exists in the second array or not
        if element in arr_2:
            # appending the intersecting element to a different array
            intersection_array.append(element)
            # obtaining the index of first occurrance of the element
            index = arr_2.index(element)
            # changing the element at the index obtained to -1 to avoid the cases of duplicate occurrance of elements
            arr_2[index] = -1
    # checking and returning the 3rd array if intersecting elements exists
    if len(intersection_array) > 0:
        return intersection_array
    else:
        return "No intersecting elements present in the given arrays."

# taking length of array 1 as an input from the user
size_1 = int(input("Enter the size of list 1: \n"))
# taking input of elements of array 1 
arr_1 = list(map(int, input().split())) [ : size_1]
# taking length of array 2 as an input from the user
size_2 = int(input("Enter the size of list 2: \n"))
# taking input of elements of array 2 
arr_2 = list(map(int, input().split())) [ : size_2]
# 3rd array created to contain the intersecting elements
intersection_array = []
print(array_intersection(arr_1, arr_2, intersection_array))