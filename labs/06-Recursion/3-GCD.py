def gcd(first, second):
    if not second:
        return first
    if first%second == 0:
        return second
    else:
        return gcd(second, first%second)
    
inp = input('Enter Input : ').split(' ')
num = gcd(abs(max(int(inp[0]),(int(inp[-1])))), abs(min(int(inp[0]),(int(inp[-1])))))
if not int(inp[0]) and not int(inp[-1]):
    print('Error! must be not all zero.')
else:
    print(f'The gcd of {max(int(inp[0]),(int(inp[-1])))} and {min(int(inp[0]),(int(inp[-1])))} is : {num}')