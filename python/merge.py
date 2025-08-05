#!/usr/bin/env python3

def merge(arr1, arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # deal with remaining elements from first array
    # while i < len(arr1):
    #     result.append(arr1[i])
    #     i += 1
    result += arr1[i:]

    # deal with remaining elements from second array
    # while j < len(arr2):
    #     result.append(arr2[j])
    #     j += 1
    result += arr2[j:]

    return result


if __name__ == "__main__":
    lst1 = [1, 2, 3, 4, 5, 6]
    lst2 = [7, 8, 9, 10, 11, 12]

    merged = merge(lst1, lst2)
    print(merged)
