def display_func(arr):
    for num in arr:
        print(num, end=" ")

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def main():
    arr = [23, 1, 3, 2, 5, 66, 7]
    print("\nBefore sorted! : ", end="")
    display_func(arr)
    selection_sort(arr)
    print("\nAfter sorted! : ", end="")
    display_func(arr)

if __name__ == "__main__":
    main()
