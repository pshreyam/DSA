def linear_search(arr, key):
    for i in arr:
        if i == key:
            return True
    return False

array = [1, 20, 40, 60, 120]
print(linear_search(array, 30))
print(linear_search(array, 40))
