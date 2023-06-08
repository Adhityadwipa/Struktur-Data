def insertionSort(angka):
    for i in range(1,len(angka)):
        key = angka[i]
        j = i-1
        
        print(i)
        print(key, " <- ", angka[j])
        
        while j >= 0 and key < angka[j]:
            angka[j+1] = angka[j]
            angka[j] = key
            j -= 1
            
            print('tukar')
            print(angka)
angka = ['AC', 'AE', 'AD', 'AF', 'AB', 'AG', 'BA']
#angka = [4, 5, 2, 7, 1, 6, 3]
insertionSort(angka)
print(angka)