print(' *** Divisible number ***')
num = int(input('Enter a positive number : '))
test = 1
each = 1

if num <= 0:
    print(num,'is OUT of range !!!')
else:
    print('Output ==>',end = ' ')
    for i in range(num):
        if (num%test) == 0 and num != test:
            print(test,end = ' ')
            test+=1
            each += 1
        elif num == test:
            print(num)
        else:
            test+=1
        
            
    print('Total ==>', each)
         
    