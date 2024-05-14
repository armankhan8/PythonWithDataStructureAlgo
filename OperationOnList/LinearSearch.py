def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Example usage:
my_list = [1, 2, 3, 4, 5]
key = 3
result = linear_search(my_list, key)
if result != -1:
    print("Element", key, "found at index", result)
else:
    print("Element", key, "not found in the list.")
