#psudocode
#ask user for input/their answer
#if score is between 90 to 100, output A
#else if score is between 80 to 89, output B
#else if score is between 70 to 79, output C
#and so on

answer=int(input("What number between 1-100 is your grade?"))

if(answer <= 100 and answer >= 90):
    print("Your grade is an A")
elif(answer < 90 and answer >= 80):
    print("Your grade is a B")
elif(answer < 80 and answer >=70):
    print("Your  grade is a C")
elif(answer <70 and answer >= 60):
    print("Your grade is a D")
else:
    print("Your grade is a F")
