# Copyright Maisy Jones - Student Grade Assigner
Score=input('What was the Students score? ')
Total=input('What was the Most Amount of Marks the Student could get? ')
print('The Student Got ' + Score + ' Out Of ' + Total + ' Marks')


#Working out the percetange
percentage: float = float(Score) / float(Total) * 100
print('Which is ' + str(percentage) + '%')

if percentage > 70:
    num = "A"
elif percentage > 60:
    num = "B"
elif percentage > 50:
    num = "C"
elif percentage > 40:
    num="D"
else:
    num="F"
print('The Student Got An ' + num + ' As a grade')
blah = input('Press Enter to Continue ')