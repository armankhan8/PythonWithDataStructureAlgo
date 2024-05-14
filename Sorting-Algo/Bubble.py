def display_func(arr):
    for num in arr:
        print(num, end=" ")

def bubble_sort(arr):
    n = len(arr)
    is_sorted = False
    for i in range(n):
        print("\nWorking on pass is", i + 1)
        is_sorted = True
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
        if is_sorted:
            return

def main():
    arr = [2, 8, 12, 43, 112, 333, 32, 54, 67]
    print("\nBefore Array: ", end="")
    display_func(arr)
    bubble_sort(arr)
    print("\nAfter Sorting: ", end="")
    display_func(arr)

if __name__ == "__main__":
    main()
