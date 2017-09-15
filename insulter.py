#Emily Murphy
#2017-09-15
#insulter.py - input name then outputs random insult

from random import randint
name = input('Enter name: ')
insult = randint(1,5)
if insult == 1:
    print('You are a nerd')
if insult == 2:
    print('You are the worst person ever')
if insult == 3:
    print('You are not funny')
if insult == 4:
    print('I bet your sibling or parents are better than you')
if insult == 5:
    print('You are probably an awful athlete/person')



