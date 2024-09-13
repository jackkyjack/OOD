def bon(w):
    for i in range(len(w)):
        for j in range(i+1,len(w)):
            if w[i] == w[j]:
                num = ord(w[i])-96
                return num*4
secretCode = input("Enter secret code : ")
print(bon(secretCode))