array_input = input('Enter Your List : ').split(' ')
if len(array_input) <= 2 : 
    print('Array Input Length Must More Than 2')
else :
    lst=[]
    for i in range(len(array_input)-2):
        for j in range(i+1,len(array_input)-1):
            for k in range(j+1,len(array_input)):
                if int(array_input[i]) + int(array_input[j]) + int(array_input[k]) == 5:
                    if sorted([int(array_input[i]), int(array_input[j]) ,int(array_input[k])]) not in lst:
                        lst.append(sorted([int(array_input[i]), int(array_input[j]) ,int(array_input[k])]))
    print(lst)