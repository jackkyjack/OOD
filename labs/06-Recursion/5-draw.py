def draw(n,i=1):
    if i>abs(n):return
    if n>0:
        print("_"*(n-i),end="")
        print("#"*i)
    else:
        print("_"*(i-1),end="")
        print("#"*(-1*n-(i-1)))
    draw(n,i+1)
    
draw(int(input("Enter Input : ")))