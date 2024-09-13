text1,text2 = input('*** String Rotation ***\nEnter 2 strings : ').split(' ')
temp1,temp2,copy1,copy2,time='','',text1,text2,1
while not (temp1 == copy1 and temp2 == copy2):
    temp1,temp2= text1[-2:] + text1[:-2] , text2[3:] + text2[:3]
    text1,text2 = temp1,temp2
    if time <= 5:
        print(f'{time} {temp1} {temp2}')
    time += 1   
print(f' . . . . .\n{time-1} {temp1} {temp2}\nTotal of  {time-1} rounds.') if time > 5 else  print(f'Total of  {time-1} rounds.')