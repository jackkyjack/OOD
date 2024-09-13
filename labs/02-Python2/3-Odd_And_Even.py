def odd_even(type, data, mode):
    if type == 'S':
        ans = ''
        for num,char in enumerate(data):
            if mode == 'Odd' and num %2  == 0:
                ans += char
            elif mode == 'Even' and num %2  != 0:
                ans += char
        return ans
    elif type == 'L':
        lst =[]
        for num,char in enumerate(data.split(' ')):
            if mode == 'Odd' and num %2  == 0:
                lst.append(char)
            elif mode == 'Even' and num %2  != 0:
                lst.append(char)
        return lst

    
            
        
    
    
    

print('*** Odd Even ***')
type,data,mode = input('Enter Input : ').split(',')
print(odd_even(type, data,mode))