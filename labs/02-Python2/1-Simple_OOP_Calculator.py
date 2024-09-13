class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, num):
        return self.value + num.value
        

    def __sub__(self, num):
        return self.value - num.value

    def __mul__(self, num):
        return self.value * num.value

    def __truediv__(self, num):
        return self.value / num.value


x, y = input("Enter num1 num2 : ").split(",")

x = Calculator(int(x))
y = Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")