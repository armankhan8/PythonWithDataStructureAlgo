def insert_element(arr, index, value):
    arr.insert(index, value)
    print("Element", value, "inserted at index", index)
    return arr

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
new_list = insert_element(my_list, 2, 10)
print("Updated list:", new_list)
