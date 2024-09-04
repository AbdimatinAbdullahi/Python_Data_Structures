arr = [29, 10, 14, 37, 13]

# [10, 29, 14, 37, 13]
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

sorted_arr = selection_sort(arr)
print(sorted_arr)