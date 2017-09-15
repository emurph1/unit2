#Emily Murphy
#2017-09-15
#warmUp3.py - asks for number, say if it is divisible by 3,2, neither, or both

num= float(input('Enter a number: '))
if num%2 == 0 and num%3 == 0:
    print(num, 'is divisible by both')
elif num%2 == 0:
    print(num, 'is divisible by 2')
elif num%3 == 0:
    print(num, 'is divisble by 3')
else:
    print('Number is not divisble by 3 or 2')
