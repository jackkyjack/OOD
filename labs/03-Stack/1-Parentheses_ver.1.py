symbol =  list(input('Enter Input : '))
dict = {'(':0,')':0,'[':0,']':0}
for i in range(len(symbol)):
    if symbol[-1] in dict.keys():
        dict[symbol[-1]] += 1
        symbol.pop()
num = abs((dict['('])-(dict[')'])) + abs((dict['['])-(dict[']']))
print(f'{num}\nPerfect ! ! !') if num == 0 else print(num)