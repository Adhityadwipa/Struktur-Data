def selectionsort(list_bilangan):
    for pos_tujuan in range(len(list_bilangan) -1, 0, -1):
        pos_max = 0
        for x in range(1,pos_tujuan +1):
            max_sementara = list_bilangan[pos_max]
            if max_sementara < list_bilangan[x]:
                pos_max = x
        #list_bilangan[pos_max],list_bilangan[pos_tujuan] = list_bilangan[pos_tujuan],list_bilangan[pos_max]
        #
        temp = list_bilangan[pos_max]
        list_bilangan[pos_max] = list_bilangan[pos_tujuan]
        list_bilangan[pos_tujuan] = temp
    
list_bilangan = [10,3,2,5,7,4,9,6,8,1]
selectionsort(list_bilangan)
print("Urutannya : ")
print(list_bilangan)
        
