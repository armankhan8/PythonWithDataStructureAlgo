def display_func(arr):
    for num in arr:
        print(num, end=" ")

def merge_sort(arr, low, mid, high):
    temp_arr = [0] * (high - low + 1)
    i = low
    j = mid + 1
    k = 0

    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            k += 1
            j += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= high:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    for i in range(low, high + 1):
        arr[i] = temp_arr[i - low]

def merge(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge(arr, low, mid)
        merge(arr, mid + 1, high)
        merge_sort(arr, low, mid, high)

# Main function
if __name__ == "__main__":
    arr = [2, 5, 1, 3, 7, 4, 9, 1, 40, 60]
    n = len(arr)
    print("Before Sorting:")
    display_func(arr)
    merge(arr, 0, n - 1)
    print("\nAfter Sorting:")
    display_func(arr)
