# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    
    index1, index2, merged_index = 0, 0, 0

    while index1 < len(arrA) and index2 < len(arrB):
        if arrA[index1] < arrB[index2]:
            merged_arr[merged_index] = arrA[index1]
            index1 += 1
        else:
            merged_arr[merged_index] = arrB[index2]
            index2 += 1

        merged_index += 1

    while index1 < len(arrA):
        merged_arr[merged_index] = arrA[index1]
        merged_index += 1
        index1 += 1
    while index2 < len(arrB):
        merged_arr[merged_index] = arrB[index2]
        merged_index += 1
        index2 += 1

    # Your code here
    

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    arr1 = merge_sort(arr[:middle])
    arr2 = merge_sort(arr[middle:])

    return merge(arr1, arr2)
   

    # return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

