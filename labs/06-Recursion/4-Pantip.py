def pantip(k, n, arr, path):
    k-=n    
    if k==0:
        print(' '.join(path))
        return 1
    if arr==[] or k<0:
        return 0
    a=pantip(k, arr[0], arr[1:], path+[str(arr[0])])
    b=pantip(k, 0, arr[1:], path)
    return a+b

inp = input("Enter Input (Money, Product) : ").split('/')
arr = [int(i)for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))