def MergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        MergeSort(L)    
        MergeSort(R)
        i=0
        j=0
        k=0
        while i<len(L) and j<len(R):
            if L[i]>R[j]:
                arr[k]=R[j]
                j+=1
            else:
                arr[k]=L[i]
                i+=1
            k+=1
        while i<len(L) :
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
arr=[10,9,8,7,6,5,4,3,2,1]
MergeSort(arr)
print(arr)    

