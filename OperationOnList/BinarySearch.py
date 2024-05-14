def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage:
my_list = [1, 2, 3, 4, 5]
key = 3
result = binary_search(my_list, key)
if result != -1:
    print("Element", key, "found at index", result)
else:
    print("Element", key, "not found in the list.")
