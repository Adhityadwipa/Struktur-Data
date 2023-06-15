def quicksort(jumlah_bilangan):
    
    kurang = []
    lebih = []
    sama = []
    if len(jumlah_bilangan) > 1:
        pivot = jumlah_bilangan[0]
        for i in jumlah_bilangan:
            if i < pivot:
                kurang.append(i)
            if i == pivot:
                sama.append(i)
            if i > pivot:
                lebih.append(i)
        return(quicksort(kurang) + sama + quicksort(lebih))
    else:
        return jumlah_bilangan

jumlah_bilangan = [10,3,4,6,7,2,1]
quicksort(jumlah_bilangan)
print(jumlah_bilangan)