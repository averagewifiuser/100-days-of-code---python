#Insertion Sort

'''
The Algorithm
Iterate from arr[1] to arr[n] over the array.

Compare the current element (key) to its predecessor.

If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.
'''

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        #tracking predecessors
        j = i-1

        while j>=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


arr = [12, 11, 13, 5, 6]
print(f"Unsorted list: {arr}")

insertion_sort(arr)
print(f"Sorted list: {arr}")

