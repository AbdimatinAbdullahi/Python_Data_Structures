arr = [38, 27, 43, 3, 9, 82, 10]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        right = arr[mid:]
        left = arr[:mid]

        #Recursilvely divide the Arrays
        merge_sort(right)
        merge_sort(left)

        merge(arr, left, right)
    return arr

def merge(arr, left, right):
    i = j = k = 0

    # i = 1, 2 j = 1, 2
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i <  len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j <  len(right):
        arr[k] = right[j]
        j += 1
        k += 1

sorted_arr = merge_sort(arr)
print(sorted_arr)