my_key = 484





alp = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h',
        'I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q',
        'R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z', 
        '#','.',',','<','>','/','?',"'",'@','"','£','$','1','2','3','4','5','6',
        '7','8','9','0','%','^','&','*','(',')','_','-','=','+','[',']','{','}',
        ';',':', ' ', '!']

# ., < > / ? ' @ " £ $ 1 2 3 4 5 6 7 8 9 0 % ^ & * ( ) _ - = + [ ] { } ; : ` ¬   ,~ ,| !


alpnums = {

}


for n in range(len(alp)):
    alpnums[alp[n]] = n




def crypt(key):
    f = open("text.txt", "r")
    f1 = f.read()
    f1 = f1.strip()
    
    output = ''
    for n in f1:
        output += str(alpnums[n]*key) + " "
        key += 3
    return output




o = crypt(77)

f = open("text_crypted.txt", "w")
f.write(o)
  
