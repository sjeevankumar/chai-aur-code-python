# Grade calculator
# Assign a letter grade based on a student's score: A(90-100),B(80-89),C(70-79),D(60-69),F(below 60)

score = int(input('Please enter the score = '))

if score<0 or score >=101:
    print('Please enter score between 0 to 100')
    exit()
    
if score>=90 and score<=100:
    grade = 'A'
elif score>=80 and score<=89:
    grade = 'B'
elif score>=70 and score<=79:
    grade = 'C'
elif score>=60 and score<=69:
    grade = 'D'
elif score<=59:
    grade = 'F'

print('your grade is '+grade)
    