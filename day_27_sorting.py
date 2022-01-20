#implemention of simple sorting algos

#selection sort
'''
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray. 
'''

arr = [54, 23, 1, 26, 38]

print(f"Unsorted arrar: {arr}")

#traverse though all array element
for i in range(len(arr)):
    #find the min element in remaining unsorted array
    min_index = i

    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j

    
    #swap the found minimum element with the first element
    arr[i], arr[min_index] = arr[min_index], arr[i]


print(f"Sorted array: {arr}") # done in O(n**2)


#Bubble Sort
'''
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
'''

def bubble_sort(arr):
    n = len(arr)

    #traverse array elements
    for i in range(n):

        #last i elements are already in place
        for j in range(0, n-i-1):
            #traverse the array in the range
            #swap if the element is found reater than the next
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


arr = [64, 34, 25, 12, 22, 11, 90]

print(f"Unsorted arr: {arr}")
bubble_sort(arr)
print(f"Sorted array: {arr}")

