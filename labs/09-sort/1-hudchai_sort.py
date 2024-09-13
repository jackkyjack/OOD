def insertion(l):
    
    for i in range(1, len(l)):
        iEle = l[i]
        for j in range(i, -1, -1):
            if iEle<l[j-1] and j > 0:
                l[j] = l[j-1]
                print('No')
                exit()
            else:
                l[j] = iEle
                break
    print('Yes')

inp = input('Enter Input : ').split()
lst = [int(i) for i in inp]
insertion(lst)