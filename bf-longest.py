import timeit

def lcp(arr):
    prefix = '' #inisialisasi prefix awal string kosong
    if(len(arr) == 0):
        return prefix
        #jika panjang array 0, maka di return string kosong
    
    for i in range(len(arr[0])):
        #loop ini adalah loop dalam array ke pertama yang dijadikan patokan pembanding
        character = arr[0][i]
        #character disini mengandung array ke 0 huruf ke i, dimana i < 5 sesuai panjang array ke 0
        for j in range(len(arr)):
        #loop ini untuk menelusuri keseluruhan isi array yang dibandingan dengan huruf di aray 0
            if(arr[j][i] != character):
                return prefix
            #if conditional jika array ke j dan huruf ke i tidak sama dengan character, maka akan direturn nilai prefixnya
        prefix = prefix + character
        #prefix ketika nilai array j huruf ke i sama dengan character, maka akan di assign ulang ke prefix
    return prefix

    #mengembalikan nilai prefix

starttime = timeit.default_timer()
print("The start time is :",starttime)
arr = ["asdasd", "test" , "se23", "westtt", "ss", "dasd"]
final_answer = lcp(arr)
print("\nHasil  eksekusi dari program ini adalah", final_answer , "dan waktunya" , timeit.default_timer() - starttime)



