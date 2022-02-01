'''
Linear search
Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
If x matches with an element, return the index.
If x doesn't match with any of the elements, return -1.

'''

def search(arr, x):

    for i in range(0, len(arr)):
        if arr[i] == x:
            return i

    return -1


#driver code
arr = [1,2,3,4,5,6,7]
x = 6

result = search(arr,x)

if result == -1 :
    print('Element not found')
else:
    print("Element is present at index", result)



'''
Binary Search -
Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.
'''

def binary_search(arr, l, r, x):

    if r >= 1:
        #divide list into 2
        mid = l + (r-1) // 2

        #check if the mid point is x
        if arr[mid] == x:
            return mid

        #if x is smaller than the mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid-1, x)

        #if x is bigger than the mid
        else:
            return binary_search(arr, l, mid+1, x)

    #not found
    else:
        return -1


arr = [2,4,6,3,2,10]
x= 2

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")

