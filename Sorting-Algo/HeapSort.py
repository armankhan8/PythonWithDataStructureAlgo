def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # Check if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child of root exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Heapify the root.
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
print("Before Sorting:", arr)
heap_sort(arr)
print("After Sorting:", arr)
