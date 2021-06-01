#fungsi dibawah berfungsi untuk membadingkan isi arraynya satu sama lain
def findCommon(temp1, temp2): 
  
    result = "" #inisialisasi result awal kosong
    x, y = len(temp1), len(temp2) #masukkan panjang temp1 dan temp2 ke variabel x dan y 
    # print("hasil2 : ", temp2)

    i, j = 0, 0 # inisialisasi i dan j = 0 
  
    while i <= x - 1 and j <= y - 1: #while loop ketika i dan j berada pada kondisi i < x -1 dan j < y-1
        if temp1[i] != temp2[j]: 
            break # kondisi break terjadi jika tidak ada kesamaan hutuf lagi antara temp1 dan temp2, maka otomatis pencarian diberhentikan
        result += temp1[i] #menyimpan hasil yang cocok ke result
        i, j = i + 1, j + 1 #kondisi looping bertambah
      
    return result #mereturn nilai result
  

#fungsi dibawah berguna untuk memecah isi aray menjadi 2 sesuai konsep dari divide and conquer
def AwalanUmum(arr, low, high): 
    #high adalah sinilai akhir dari array.
    #low adalah nilai awal dari array.
    if low == high: #if conditional jika nilai dari awal akhir sama dengan nilai akhir dari array
        return arr[low] # maka akan direturn nilai array awal.
  
    if high > low: #if conditional jika nilai akhir array lebih gede nilainya dari nilai awalnya.
      
        mid = low + (high - low) // 2 #untuk mencari nilai tengah, maka menggunakan low dan highnya.

        temp1 = AwalanUmum(arr, low, mid) #temp1 variabel untuk menyimpan dmn konsepnya divide and conquer dari awal sampai tengah array.
    
        temp2 = AwalanUmum(arr, mid + 1, high) 
        print("hasil",temp2) #temp2 variabel untuk menyimpan dan konsepnya divide and conquere dari tengah+1 sampai dengan akhir array.
  
        return findCommon(temp1, temp2) #memanggil fungsi findCommon untuk membandingan temp1 dan temp2 apakah ada kesamaan huruf / kata.


arr = ["asdasd", "test" , "se23", "westtt", "ss", "dasd"]
array = len(arr)
jawab = AwalanUmum(arr, 0, array - 1) 
  
if len(jawab): 
    print("Awalan yang paling panjang adalah", jawab)
else:
    print("Tidak ada kata yang cocok") 