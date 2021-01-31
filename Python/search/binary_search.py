from math import floor

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = floor((low + high) / 2)
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False

array = [1, 20, 40, 60, 120]
print(binary_search(array, 30))
print(binary_search(array, 40))
