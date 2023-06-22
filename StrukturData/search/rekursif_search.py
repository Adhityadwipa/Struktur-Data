#perulangan dari belakang
def searchrekursif(arr, curr_idx, x):
    if curr_idx == -1:
        return -1
    if arr[curr_idx] == x:
        return curr_idx
    return searchrekursif(arr, curr_idx-1, x)
arr = [2,4,1,5,7,9]
x = 1
print("jadi, data yang dicari berada pada index ke-", searchrekursif(arr, len(arr)-1, x))




#perulangan dari depan
def searchrekursif(arr, curr_idx, x):
    if curr_idx == len(arr):
        return -1
    if arr[curr_idx] == x:
        return curr_idx
    return searchrekursif(arr, curr_idx+1, x)
arr = [2,4,1,5,7,9]
x = 1
print("jadi, data yang dicari berada pada index ke-", searchrekursif(arr, 0, x))