my_key = 77

f = open("text_crypted.txt", "r")
f1 = f.read()
f1 = f1.strip()

alp = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h',
        'I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q',
        'R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z', 
        '#','.',',','<','>','/','?',"'",'@','"','£','$','1','2','3','4','5','6',
        '7','8','9','0','%','^','&','*','(',')','_','-','=','+','[',']','{','}',
        ';',':', ' ', '!']

# ., < > / ? ' @ " £ $ 1 2 3 4 5 6 7 8 9 0 % ^ & * ( ) _ - = + [ ] { } ; : ` ¬   ,~ ,| !


alpnums = { }


for n in range(len(alp)):
    alpnums[alp[n]] = n

num = ''
out = ''

for n in f1:
    if n != ' ':
        num += n
    else:
        out += alp[int(int(num) / my_key)]
        my_key += 3
        num = ''
out += alp[int(int(num) / my_key)]

f = open("text_encrypted.txt", "w")
f.write(out)
