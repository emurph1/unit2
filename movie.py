#Emily Murphy
#2017-09-13
#movie.py - input age and print out most scandalous type of movie they can watch

age = int(input('Enter age: '))
if age>18:
    print('You can watch rated R movies')
if age<18 and age>13:
    print('You can watch PG-13 movies')
if age<13 and age>8:
    print('You can watch PG movies')
if age<8:
    print('You can watch G movies')

