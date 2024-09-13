def find_max(lst, cur, end):
    if cur == end:
        return cur
    
    max_digit = find_max(lst, cur+1, end)
    return cur if lst[cur] > lst[max_digit] else max_digit    
        
def swap(lst,end=None):
    if end is None:
        end = len(lst) - 1
    
    bignum = find_max(lst,0, end)
    
    if end == 0 :
        return lst
    elif lst[end] == lst[bignum] :
        return swap(lst, end-1)
    else:
        lst[end], lst[bignum] = lst[bignum], lst[end]
        print(f'swap {lst[bignum]} <-> {lst[end]} : {lst}')
        return swap(lst, end-1)


print(swap([int(i) for i in input('Enter Input : ').split(' ')]))