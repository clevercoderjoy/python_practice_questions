def push_zeroes_to_end(arr, size):
    i = 0
    k = 0
    while i < size:
        if arr[i] != 0:
            arr[i], arr[k] = arr[k], arr[i]
            i += 1
            k += 1
        else:
            i += 1
    return arr

size = int(input())
arr = [int(element) for element in input().split()] [ : size]
print(*(push_zeroes_to_end(arr, size)))
