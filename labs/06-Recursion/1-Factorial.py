def fact(n, num = None,sum = None):
    if n == 0:
        print('0! = 1')
    elif not num:
        num = n
        sum = 1
        fact(n,num,sum)
    elif n == 1:
        print(f'{num}! = {sum}')
    else:
        sum *= n
        fact((n-1),num,sum)
        
fact(int(input('Enter Number : ')))