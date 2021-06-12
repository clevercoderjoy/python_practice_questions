def check_array_rotation(arr, size):
    if size == 0:
        return 0
    min = 0
    for i in range(1, size):
        if arr[i] < arr[min]:
            min = i
    return min

size = int(input())
arr = [int(element) for element in input().split()] [ : size]
print(check_array_rotation(arr, size))
