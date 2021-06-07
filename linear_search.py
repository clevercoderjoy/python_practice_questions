# code linear search

def linear_search(arr, size, x):
    for element in range(size):
        if arr[element] == x:
            return element + 1
    return "Element not found."

size = int(input("Enter the size of the array: \n"))
arr = list(map(int, input().split())) [ : size]
x = int(input("Enter the element to be searched from the list: \n"))
print(linear_search(arr, size, x))