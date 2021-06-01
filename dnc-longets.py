# A Python3 Program to find the longest common prefix 
  
# A Utility Function to find the common 
# prefix between strings- str1 and str2 
def findCommon(temp1, temp2): 
  
    result = "" 
    x, y = len(temp1), len(temp2)
   
    print("hasil2 : ", temp2)

    i, j = 0, 0
  
    while i <= x - 1 and j <= y - 1: 
        if temp1[i] != temp2[j]: 
            break
        result += temp1[i]
        i, j = i + 1, j + 1
      
    return result
  

#fungsi dibawah berguna untuk memecah isi aray menjadi 2 sesuai konsep dari divide and conquer
def AwalanUmum(arr, low, high): 
    #high adalah sinilai akhir dari array.
    #low adalah nilai awal dari array.
    if low == high: #if conditional jika nilai dari awal akhir sama dengan nilai akhir dari array
        return arr[low] # maka akan direturn nilai array awal.
  
    if high > low: #if conditional jika nilai akhir array lebih gede nilainya dari nilai awalnya.
      
        mid = low + (high - low) // 2 #untuk mencari nilai tengah, maka menggunakan low dan highnya.

        temp1 = AwalanUmum(arr, low, mid) #temp1 variabel untuk menyimpan dmn konsepnya divide and conquer dari awal sampai tengah array.
        temp2 = AwalanUmum(arr, mid + 1, high)  #temp2 variabel untuk menyimpan dan konsepnya divide and conquere dari tengah+1 sampai dengan akhir array.
  
        return findCommon(temp1, temp2) #memanggil fungsi findCommon untuk membandingan temp1 dan temp2 apakah ada kesamaan huruf / kata.


arr = ["asdasd", "test" , "se23", "westtt", "ss", "dasd"]
array = len(arr)
ans = AwalanUmum(arr, 0, array - 1) 
  
if len(ans): 
    print("The longest common prefix is", ans)
else:
    print("There is no common prefix") 