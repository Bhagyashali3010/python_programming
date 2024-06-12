s='hello WORLD bababab radara'
words = s.split()
arr=''
for word in words:
    # a=word.capitalize()
    # print(a)
    if word.isupper():
        arr+=word
        arr+=' '
    else:
        a=word.capitalize()
        arr+=a
        arr+=' '
print(arr)