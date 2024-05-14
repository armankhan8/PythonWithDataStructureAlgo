def count_sort(arr):
    # Find the maximum element in the array
    max_element = max(arr)
    
    # Create a count array to store the count of each element
    count = [0] * (max_element + 1)
    
    # Count the occurrences of each element in the array
    for num in arr:
        count[num] += 1
    
    # Update the count array to store the cumulative count of each element
    for i in range(1, max_element + 1):
        count[i] += count[i - 1]
    
    # Create a temporary array to store the sorted elements
    result = [0] * len(arr)
    
    # Place the elements in the sorted order using the count array
    for num in arr:
        result[count[num] - 1] = num
        count[num] -= 1
    
    # Copy the sorted elements back to the original array
    for i in range(len(arr)):
        arr[i] = result[i]

# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1]
print("Before sorting:", arr)
count_sort(arr)
print("After sorting:", arr)
