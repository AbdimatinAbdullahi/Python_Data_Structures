arr = [5, 1, 4, 2, 6, 3]

# 1st Itrations: i = 0, j = 1, 1 5 4 2 6 3  
# 2nd Itrations: i = 0, j = 2, 1 4 5 2 6 3  
# 3rd Itrations: i = 0, j = 3, 1 4 2 5 6 3  
# 4th Itrations: i = 0, j = 4, 1 4 5 2 6 3  
# 5th Itrations: i = 0, j = 5, 1 4 5 2 3 6  
# 6th Itrations: i = 1, j = 2, 1 4 5 2 3 6  

def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

sorted_arr = bubble_sort(arr)
print(sorted_arr)