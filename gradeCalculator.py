#Emily Murphy
#2017-09-13
#gradeCalculator.py - input grade percentage and outputs letter grade

grade = int(input('Enter grade percentage: '))
if grade>0 and grade<59:
    print('You earned a F')
if grade>60 and grade<69:
    print('You earned a D')
if grade>70 and grade<79:
    print('You earned a C')
if grade>80 and grade<89:
    print('You earned a B')
if grade>90 and grade<100:
    print('You earned a A')