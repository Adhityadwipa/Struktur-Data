def searchIter(arr, x):
    for i in range(len(arr)):
        if x == arr[i]:
            return i
    return -1 #jika data tidak ada
    
arr = [2,4,1,5,7,9]
x = 1
print("jadi, data yang dicari berada pada index ke-", searchIter(arr, x))