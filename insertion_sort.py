# Insertion sort code
# we assume that out array is divided into two parts i.e. sorted and unsorted.
# the first (arr[0]) element in the array is considered to be sorted.
# the first for loop starts from (first index + 1) because we assume that the first element is already sorted.
# we put the element at the first index in a temp variable and set variable j as (i - 1).
# we set j as (i - 1) because we we want to compare the jth element with the element in the temp variable to sort the array.
# we use a while loop which keeps running until j >= 0 and the element in the jth index > element in the temp variable.
# once the condition fails we increase j by 1 and place the element in the temp variable at jth index.
# we increase j by 1 before placing the element at it's correct position because before the condition failed it decreased j by 1.
# because of this j becomes 1 less than the correct position which we compansate after increasing j by 1 to reach the correct position.
# the left part of the array is sorted and the right part is unsorted.
# we shift elements one by one until we reach the correct position to place the element.

# function for insertion sort
def insertion_sort(arr, size):
    # first for loop starting from index 1 since the first element (arr[0]) is considered as sorted
    for i in range(1, size):
        # placing the element at ith index in a temporary variable
        temp = arr[i]
        # setting j as i - 1 to so as to compare the elements for sorting
        j = i - 1
        # second while loop to check if index j is not negative after decrement and the element in the jth index is greater than the element in the temp variable.
        while j >= 0 and arr[j] > temp:
            # copying the element in jth index to (j + 1)th index
            arr[j + 1] = arr[j]
            # decreasing j by 1 to move to the previous index
            j -= 1
        # increasing j by 1 and placing the element in temp variable (j + 1)th index
        arr[j + 1] = temp
    return arr

# main function
size = int(input())
arr = [int(element) for element in input().split()] [ : size]
print(*(insertion_sort(arr, size)))