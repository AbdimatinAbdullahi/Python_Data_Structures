arr = [3, 6, 8, 7, 1, 2, 1]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  #7
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot] 
        right = [x for x in arr if x > pivot] 
        return quick_sort(left) + middle + quick_sort(right)


sorted_arr = quick_sort(arr)
print(sorted_arr)