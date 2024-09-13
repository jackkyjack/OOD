class Stack :
    def __init__(self, list=None): 
        if list == None:
            self.items = []
        else:
            self.items = list
    def isEmpty(self) :
        return not self.size()
    def push(self,data) :
        self.items.append(data)
    def pop(self) :
        return self.items.pop()
    def size(self) :
        return len(self.items)
    def peek(self) :
        return self.items[-1] if not self.isEmpty() else None

def infix2postfix(exp) :
    s = Stack()
    check_uqi = False 
    ans =''  
    for i in exp:
        if i != '+' and i != '-' and i != '*' and i != '/' and i != '(' and i != ')':
            if check_uqi:
                ans += str(i)
                ans += str(s.pop())
                check_uqi = False
            else:
                ans += str(i)
        else :
            if s.isEmpty() :
                s.push(i)
            else :
                if i =='*' or i == '/':
                    s.push(i)
                    check_uqi = True
                elif i == '(':
                    s.push(i)
                elif i == ')':
                    while s.peek() != '(':
                        ans += str(s.pop())
                else :
                    if s.peek() == '(':
                        s.push(i)
                    else:
                        ans += str(s.pop())
                        s.push(i)
                    
    while not s.isEmpty() :
        if s.peek() != '(' :
            ans += str(s.pop())
        else :s.pop()
    
    return ans

print(" ***Infix to Postfix***")
token = input("Enter Infix expression : ")
print("PostFix : ")
print(infix2postfix(token))