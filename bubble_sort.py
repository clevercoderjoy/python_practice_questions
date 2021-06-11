# code bubble sort

# key points:
# For n elements we need (n - 1) rounds.
# At the end of each iteration we will have the largest element at the end of the array.
# We need (n - 1) rounds because we need to compare elements and also avoid the list index out of bound error.
# First look goes for (n - 1) rounds.
# The second loop will start from (i + 1) and go up to n rounds.
# At every iteration we will swap the (i + 1)th element with the ith element if (i + 1)th element will be smaller than the ith element on comparison.
# At every iteration compare and move the largest element at the end of the list.
# sorting takes place from back to front

def bubble_sort(arr, size):
    # first loop to traverse over the list
    for i in range(size - 1):
        # second loop to compare the elements with ith element
        for j in range((i + 1), size):
            # checking if jth element is smaller than the ith element
            if arr[j] < arr[i]:
                # swapping the jth and the ith element to move the larger element towards the ene of the list every iteration
                arr[j], arr[i] = arr[i], arr[j]
    return arr

size = int(input("Enter the size of array:\n"))
arr = list(map(int, input().split()))
print(bubble_sort(arr, size))