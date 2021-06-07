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
arr = ["manasdasd", "mantest", "manse23", "manwesttt", "manss", "mandasd", "manaedes", "mansecre", "manbulletin", "manscudet", "manauto", "manual", "manades", "manfractual", "manterm", "mandesert", "manrush", "manbomb", "manolotov", "manjosh", "manpolish", "manantum", "manruk", "mankoja", "manaada", "manjoki", "manaplle", "mantafu", "mankofari", "manahbek", "mandaliu", "manjaad", "manjadawa", "mangulai", "manbaru", "mankiro", "manadawa", "manjenggot", "manjudi", "mankufqo", "manxerito", "manbuluk", "manqeri", "manvulan", "mankilo", "mandota", "mantan", "mangundul", "manbotak", "manrontok", "manpedang", "manwaktu", "manroko", "manvoli", "manbola", "mantennis", "manmabuk", "manmerci", "manlambo", "manforza", "manpursuit", "manlupa", "maningat", "manteuing", "manbuta", "mansurend", "mangelo", "mantugas", "manfullus", "mankisut", "mankeriput", "mantua", "manceli"]

final_answer = lcp(arr)
print("\nHasil  eksekusi dari program ini adalah", final_answer , "dan waktunya" , timeit.default_timer() - starttime)



