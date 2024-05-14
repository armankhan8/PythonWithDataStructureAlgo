def display_func(arr):
    for num in arr:
        print(num, end=" ")

def insertion_sort(arr):
    for i in range(1, len(arr)):
        flag = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > flag:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = flag

def main():
    arr = [23, 1, 4, 5, 2, 11, 3]
    print("\nBefore Sort : ", end="")
    display_func(arr)
    insertion_sort(arr)
    print("\nAfter Sort : ", end="")
    display_func(arr)

if __name__ == "__main__":
    main()
