# Code Binary Search

# We divide the array into half and check if the mid element is equal to the desired element or not.
# If x is not found and the mid value obtained is less than x then we increase the start by adding 1 to mid value.
# If x is not found and the mid value obtained is greater than x then we decrease the end by subtracting 1 to mid value.
# Eventually x will be found in the mid value obtained.
# If x is not found then return element not found

# function for binary search
def binary_search(arr, size, x):
    start = 0
    end = size - 1
    # element will be searched until start does not becomes greater than end
    while start <= end:
        # storing the value obtained by dividing the array into two parts
        mid = (start + end) // 2
        # checking if x is  greater than the mid element in the array
        if x > arr[mid]:
            # increasing start by mid + 1
            start = mid + 1
        # checking if x is  less than the mid element in the array
        elif x < arr[mid]:
            # decreasing start by mid - 1
            end = mid - 1
        # checking if mid element of the array is equal to the desired element
        elif x == arr[mid]:
            # returning the correct position of x
            return mid + 1
    return " Element not found."

size = int(input("Enter the size of the array: \n"))
arr = list(map(int, input().split()))
x = int(input("Enter the element to find from the array: \n"))
print(binary_search(arr, size, x))