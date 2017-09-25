#Emily Murphy
#2017-09-25
#quiz2.py

num1 = float(input('Enter a number:'))
num2 = float(input('Enter another number:'))
if num1 == num2:
    print('Numbers are the same')
if num1 > num2:
    print('The first number is greater than the second')
elif num2 > num1:
    print('The second number is greater than the first')
if num1//3 and num2//3:
    print('Numbers are divisible by 3')
elif num1//3 and (num2!= num2//3):
    print('First number is divisible by 3')
elif num2//3 and (num1!= num1//3):
    print('Second number is divisble by 3')
elif (num2!= num2//3) and (num1!= num1//3):
    print('Neither numbers are divisible by 3')
product = float(input('Enter the product of the two numbers: '))
if product == num1*num2:
    print('You are correct')
elif product!= num1*num2:
    print('You are wrong')

