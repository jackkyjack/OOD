a,b = input("Enter your High and Weight : ").split()
num = float(b) / (float(a)*float(a))

if num < 18.50 :
    print('Less Weight')
elif 18.50<= num < 23:
    print('Normal Weight')
elif 23<= num <25:
    print('More than Normal Weight')
elif 25<= num <30:
    print('Getting Fat')
else:
    print('Fat')