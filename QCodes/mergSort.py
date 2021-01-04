def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        leftSub = arr[:mid]
        rightSub = arr[mid:]
        mergeSort(leftSub)
        mergeSort(rightSub)
            
        i=j=k =0
        while i <len(leftSub) and j < len(rightSub):
            if leftSub[i]<rightSub[j]:
                arr[k] = leftSub[i]
                i += 1
            else:
                arr[k] = rightSub[j]
                j += 1
            k += 1
            
        while i < len(leftSub):
            arr[k] = leftSub[i]
            i += 1
            k += 1
            
        while j < len(rightSub):
            arr[k] = rightSub[j]
            j += 1
            k += 1
            
            
arr = [5,3,4,9,6,1,2]
mergeSort(arr)
print(arr)