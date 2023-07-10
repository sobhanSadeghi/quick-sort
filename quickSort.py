def quickSort(arr):
    if len(arr)<=1:
        return arr

    pivot=arr[0]

    smaller=[x for x in arr[1:] if x <= pivot]
    greater=[x for x in arr[1:] if x> pivot]

    return quickSort(smaller)+[pivot]+quickSort(greater)



arr1=[6,3,8,2,11,1,9]

sorted_array=quickSort(arr1)

print(f'sorted array:{sorted_array}')



