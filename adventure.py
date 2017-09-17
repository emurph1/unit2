#Emily Murphy
#2017-09-15
#adventure.py - create an adventure

print('You are walking home from work')
print('You happen to notice a creepy clown standing at the edge of a sidewalk and is staring directly at you.')
choice1 = input('Do you go and say hi? ')
ans1= 'Yes' or 'yes'
ans2 = 'No' or 'no'
if choice1 == ans1:
    print('The clown smiles at you then murders you with a knife. :(')
elif choice1 == 'No' or 'no':
    print('You could run like hell')
choice2 = input('Do you run like hell? ')
if choice2 == ans1:
    print('You get to live to see another day. The clown did not chase after you. :)')
elif choice2 == ans2:
    print('You end up having a staring contest with the clown and the clown gets bored and leaves.')
            
