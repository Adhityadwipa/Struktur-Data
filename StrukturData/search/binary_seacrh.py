def searchIter(arr, x):
    awal = 0
    tengah = 0
    akhir = len(arr)-1
    
    while awal <= akhir:
        tengah = (awal+akhir)//2
        if arr[tengah] < x:
            awal = tengah+1
        elif arr[tengah] > x:
            akhir = tengah-1
        else:
            return tengah
    return -1



#rekursif binary
def searchrekursif(arr, awal, akhir, x):
    if akhir >= awal:
        tengah = (awal+akhir)//2
        if arr[tengah] == x:
            return tengah
        elif arr[tengah] > x:
            return searchrekursif(arr, awal, tengah-1, x)
        else:
            return searchrekursif(arr, tengah+1, akhir, x)
    else:
        return -1



arr = [3,4,6,8,9,10]
x = 9
print("jadi, data yang dicari berada pada index ke-", searchIter(arr, x))
print("jadi, data yang dicari berada pada index ke-", searchrekursif(arr, 0, len(arr)-1, x))