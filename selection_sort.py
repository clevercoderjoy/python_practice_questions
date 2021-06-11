# selection sort code:

# in selection sort, we find the minimum element and swap it with ith element.
# the first loop goes up to (the last index of the arr - 1) to avoid index out of range error in the second loop.
# we will take a min variable and set it's value to i.
# the second loop starts from (i + 1) and goes up to the last index of the array.
# if we start the second loop from ith index then in the first iteration we will be to comparing the same elements which makes no sense.
# we search for the minimum element from the array then set the index of minimum element to min variable
# we swap the ith value with the index in the min variable and sort the array.
# the smallest element keeps moving towards the start of the array after each iteration
# sorting takes place from front to back

# function for selection sort
def selection_sort(arr, size):
    # first loop to pick elements to compare one by one
    for i in range(size - 1):
        # setting the ith index to min
        min = i
        # second loop to traverse through the array and compare with ith element
        for j in range(i + 1, size):
            # comparison
            if arr[j] < arr[min]:
                # setting the jth index to be min if condition if true
                min = j
        # swapping the elements in order to sort the array at every iteration
        arr[i], arr[min] = arr[min], arr[i]
    return arr

# main function
size = int(input())
arr = list(map(int, input().split())) [ : size]
print(*(selection_sort(arr, size)))