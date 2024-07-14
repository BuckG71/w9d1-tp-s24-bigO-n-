"""A program to practice concepts related to time complexity."""

def linear_search(arr, target):
    """Linear search function"""
    if target not in arr:
        return -1
    return arr.index(target)

# Sample Test Cases
ARRAY1 = [10, 23, 45, 70, 11, 15]
TARGET1 = 70
print("Linear search test cases")
print(f"Index of {TARGET1}: {linear_search(ARRAY1, TARGET1)}")  # Output: 3

TARGET2 = 11
print(f"Index of {TARGET2}: {linear_search(ARRAY1, TARGET2)}")  # Output: 4

TARGET3 = 99
print(f"Index of {TARGET3}: {linear_search(ARRAY1, TARGET3)}")  # Output: -1

def optimized_lin_srch(arr, target):
    """Optimized linear search function
    Uses enumerate to be more pythonic
    Ensures the array is only traversed a single time"""
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

# Sample Test Cases for Optimized Linear Search
print("Optimized linear search test cases")
print(f"Index of {TARGET1}: {optimized_lin_srch(ARRAY1, TARGET1)}")  # Output: 3

print(f"Index of {TARGET2}: {optimized_lin_srch(ARRAY1, TARGET2)}")  # Output: 4

print(f"Index of {TARGET3}: {optimized_lin_srch(ARRAY1, TARGET3)}")  # Output: -1

# Bubble sort function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Sample Test Cases
print("Bubble sort test cases")
ARRAY3 = [64, 34, 25, 12, 22, 11, 90]
print(f"Sorted array 1: {bubble_sort(ARRAY3)}")  # Output: [11, 12, 22, 25, 34, 64, 90]

ARRAY4 = [5, 1, 4, 2, 8]
print(f"Sorted array 2: {bubble_sort(ARRAY4)}")  # Output: [1, 2, 4, 5, 8]uns_array = [33, 29, 30, 2, 19, 7]

def optimized_bubble_sort(arr):
    """Added in a flag to test if elements were swapped, this saves one traversal of the array that would otherwise be run after the array was sorted"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Optimized bubble sort sample Test Cases
print("Optimized bubble sort test cases")
print(f"Sorted array 1: {bubble_sort(ARRAY3)}")  # Output: [11, 12, 22, 25, 34, 64, 90]

print(f"Sorted array 2: {bubble_sort(ARRAY4)}")  # Output: [1, 2, 4, 5, 8]uns_array = [33, 29, 30, 2, 19, 7]
