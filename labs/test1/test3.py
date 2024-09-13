print(' *** String count ***')
string = [*input('Enter message : ')]
big = 0
small = 0
list_big = []
list_small = []

for i in string:
    if i.isupper():
        big+=1
        if i not in list_big:
            list_big.append(i)
    elif i.islower():
        small+=1
        if i not in list_small:
            list_small.append(i)
            
list_big.sort()
list_small.sort()
print('No. of Upper case characters :',big)
print('Unique Upper case characters :',"  ".join(list_big))
print('No. of Lower case Characters :',small)
print('Unique Lower case characters :',"  ".join(list_small))
