def delete_element(arr, key):
    if key not in arr:
        print("Element not found in the list.")
    else:
        arr.remove(key)
        print("Element", key, "deleted from the list.")
    return arr

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
new_list = delete_element(my_list, 3)
print("Updated list:", new_list)
