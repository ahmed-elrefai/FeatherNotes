def insertion_sort(arr):
    """
    Sorts the array in ascending order using the insertion sort algorithm.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# FILENAME: searching.py
def binary_search(arr, target):
    """
    Finds the index of a target element in the sorted array using a binary search algorithm.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Return -1 if the target element is not found

# FILENAME: main.py
from sorting import insertion_sort
from searching import binary_search

def main():
    arr = [4, 2, 3, 5, 1, 0]
    sorted_arr = insertion_sort(arr)
    target = int(input("Enter a target value: "))
    idx = binary_search(sorted_arr, target)
    if idx != -1:
        print("Index:", idx)
    else:
        print("Target element not found in the array")

if __name__ == "__main__":
    main()