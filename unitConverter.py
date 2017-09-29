#Emily Murphy
#2017-09-13
#unitCoverter.py - 

i = 1
while i<=4:
    i += 1
    num = int(input('Enter a number: '))
    if num == 1:
        km = float(input('Enter number of kilometers: '))
        print(km, 'kilometers is', (km*0.621371), 'miles')
    elif num == 2:
        kg = float(input('Enter number of kilograms: '))
        print(kg, 'kilograms is', (kg*2.20462), 'pounds')
    elif num == 3:
        L = float(input('Enter number of liters: '))
        print(L, 'liters is', (L*0.264172), 'gallons')
    elif num == 4:
        degrees = float(input('Enter degrees in Celsius: '))
        print(degrees,'degrees Celsius is', ((degrees*1.8) + 32),'degrees in Fahrenheit')
    elif num == 5:
        break
    else:
        print('Error, number must be integer between 1-4')


