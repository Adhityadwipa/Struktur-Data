def partition(jumlah_bilangan, kurang, lebih):
    pivot = jumlah_bilangan[lebih]
    i = kurang - 1
    for j in range(kurang, lebih):
        if jumlah_bilangan[j] <= pivot:
            i = i + 1
            (jumlah_bilangan[i], jumlah_bilangan[j]) = (jumlah_bilangan[j], jumlah_bilangan[i])
    (jumlah_bilangan[i + 1], jumlah_bilangan[lebih]) = (jumlah_bilangan[lebih], jumlah_bilangan[i + 1])
 
    return i + 1
 
def quickSort(jumlah_bilangan, kurang, lebih):
    if kurang < lebih:
        pi = partition(jumlah_bilangan, kurang, lebih)
        quickSort(jumlah_bilangan, kurang, pi - 1)
        quickSort(jumlah_bilangan, pi + 1, lebih)
 
 
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
 
size = len(data)
 
quickSort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)
