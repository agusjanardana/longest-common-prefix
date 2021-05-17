def lcp(strs):
    prefix = '' #inisialisasi prefix awal string kosong
    if(len(strs) == 0):
        return prefix 
        #jika panjang array 0, maka di return string kosong
    
    for i in range(len(strs[0])):
        character = strs[0][i]
        for j in range(len(strs)):
            if(strs[j][i] != character):
                return prefix
        prefix = prefix + character
    return prefix

strs = ["apple", "application", "appti", "a"]
#a
# #ap
# #app
# #applepptis"] 
# print(strs[0][0])
ans = lcp(strs)
#a
#ap
#app
#apple

print(ans)


