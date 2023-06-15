def mergesort(list_bilangan):
    jumlah_bilangan = len(list_bilangan)
    if jumlah_bilangan > 1:
        posisi_tengah = jumlah_bilangan//2
        potongan_kiri = list_bilangan[:posisi_tengah]
        potongan_kanan = list_bilangan[posisi_tengah:]
        mergesort(potongan_kiri)
        mergesort(potongan_kanan)
        jumlah_bagian_kiri = len(potongan_kiri)
        jumlah_bagian_kanan = len(potongan_kanan)
        c_kiri, c_kanan, c_all = 0, 0, 0
        while c_kiri < jumlah_bagian_kiri or c_kanan < jumlah_bagian_kanan:
            if c_kiri == jumlah_bagian_kiri:
                list_bilangan[c_all] = potongan_kanan[c_kanan]
                c_kanan += 1
            elif c_kanan == jumlah_bagian_kanan:
                list_bilangan[c_all] = potongan_kiri[c_kiri]
                c_kiri += 1
            #jika elemen kiri lebih kecil
            elif potongan_kiri[c_kiri] <= potongan_kanan[c_kanan]:
                list_bilangan[c_all] = potongan_kiri[c_kiri]
                c_kiri += 1
            #elemen kanan lebih kecil
            else :
                list_bilangan[c_all] = potongan_kanan[c_kanan]
                c_kanan += 1
            c_all += 1
            
list_bilangan = [10,3,2,4,6,1,9,7,8]
mergesort(list_bilangan)
print(list_bilangan)