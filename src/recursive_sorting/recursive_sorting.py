# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []
    # TO-DO
    
    i, j = 0, 0
    while i < len(arrA) or j < len(arrB):
      if i == len(arrA):
        merged_arr = merged_arr + arrB[j:]
        break
      elif j == len(arrB):
        merged_arr = merged_arr + arrA[i:]
        break
      elif arrA[i] < arrB[j]:
        merged_arr.append(arrA[i])
        i += 1
      else:
        merged_arr.append(arrB[j])
        j += 1    
      
    return merged_arr

print(merge([2, 3, 5, 7, 9, 12, 45, 67, 89], [4, 6, 8, 13, 16, 26, 35]))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
      return arr
    pivot = len(arr) // 2
    left = merge_sort(arr[:pivot])
    right = merge_sort(arr[pivot:])

    
    return merge(left, right)

print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
