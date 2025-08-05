#!/usr/bin/env python3

def heapify(arr, i=0):
    length = len(arr)
    left_index = 2 * i + 1
    right_index = 2 * i + 2

    if i < length:
        root = arr[i]
        print(f"root: {root}")

    if left_index < length:
        left_leaf = arr[left_index]
        print(f"left leaf of {root}: {left_leaf}")

    if right_index < length:
        right_leaf = arr[right_index]
        print(f"right leaf of {root}: {right_leaf}")

    if left_index < length:
        heapify(arr, left_index)

    if right_index < length:
        heapify(arr, right_index)


arr = [10, 9, 8, 3, 4, 5, 1, 2, 7, 6]
heapify(arr)
