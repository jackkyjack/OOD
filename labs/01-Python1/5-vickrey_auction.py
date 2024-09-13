lst = input('Enter All Bid : ').split()

def toInt(num):
    return int(num)

lst.sort(key=toInt)

if len(lst) <= 1:
    print("not enough bidder")
elif lst[-1] != lst[-2]:
    print(f'winner bid is {lst[-1]} need to pay {lst[-2]}')
elif lst[-1] == lst[-2]:
    print("error : have more than one highest bid")