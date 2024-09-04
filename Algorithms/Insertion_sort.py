arr = [10, 3, 8, 9, 1, 5, 7]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1    

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    
    return arr

sorted_arr = insertion_sort(arr)
print(sorted_arr)