# merge two sorted array

def merge(arr1, size1, arr2, size2):
    a = []
    i = 0
    j = 0
    while (i < size1) and (j < size2):
        if arr1[i] < arr2[j]:
            a.append(arr1[i])
            i += 1
        else:
            a.append(arr2[j])
            j += 1
    while i < size1:
        a.append(arr1[i])
        i += 1
    while j < size2:
        a.append(arr2[j])
        j += 1
    return a

size1 = int(input())
arr1 = [int(element) for element in input().split()] [ : size1]
size2 = int(input())
arr2 = [int(element) for element in input().split()] [ : size2]
print(*(merge(arr1, size1, arr2, size2)))