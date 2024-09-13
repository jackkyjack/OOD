print(' *** Wind classification ***')
num = input('Enter wind speed (km/h) : ')
wind = float(num)
if wind < 0:
    print("!!!Wrong value can't classify.")
elif 0 <= wind <= 51.99:
    print("Wind classification is Breeze.")
elif 52.00 <= wind <= 55.99:
    print("Wind classification is Depression.")
elif 56.00 <= wind <= 101.99:
    print("Wind classification is Tropical Storm.")
elif 102.00 <= wind <=208.99:
    print("Wind classification is Typhoon.")
else:
    print("Wind classification is Super Typhoon.")
    