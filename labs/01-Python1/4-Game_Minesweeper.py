def num_grid(lst):
    # temp = lst[:] # copy list
    for e in range(len(lst)):
        for i in range(len(lst[e])):
            if lst[e][i] == '-' :
                lst[e][i] = 0

    for e in range(len(lst)):
        for i in range(len(lst[e])):
            if lst[e][i] == '#':
                bomb(lst,e,i)
    
    for e in range(len(lst)):
        for i in range(len(lst[e])):
            if lst[e][i] != '#':
                lst[e][i] = str(lst[e][i])
            
             
    return lst

def bomb(lst,e,i):
    
    if e-1 >= 0 and i-1 >= 0 :
        if lst[e-1][i-1] != '#':
            lst[e-1][i-1] +=1
            
    if e-1 >= 0 and i+1 <= 4 :
        if lst[e-1][i+1] != '#':
            lst[e-1][i+1] +=1
            
    if e+1 <= 4 and i-1 >= 0 :
        if lst[e+1][i-1] != '#':
            lst[e+1][i-1] +=1
            
    if e+1 <= 4 and i+1 <= 4 :
        if lst[e+1][i+1] != '#':
            lst[e+1][i+1] +=1
    
    if e-1 >=0:
        if lst[e-1][i] != '#':
            lst[e-1][i] +=1
    
    if e+1 <= 4:
        if lst[e+1][i] != '#':
            lst[e+1][i] +=1
    
    if i-1 >= 0 :
        if lst[e][i-1] != '#':
            lst[e][i-1] +=1
            
    if i+1 <= 4 :
        if lst[e][i+1] != '#':
            lst[e][i+1] +=1


lst_input = []


print('*** Minesweeper ***')

input_list = input('Enter input(5x5) : ').split(",")

for e in input_list:
  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")
print("\n",*num_grid(lst_input),sep = "\n")