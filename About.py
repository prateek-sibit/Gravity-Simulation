# Accessing the files that inform about the Project

def about():
    print("\n")
    print(" About this project ")
    print(" 1. Introduction ")
    print(" 2. Problem statement")
    print(" 3. What this project hopes to achieve")
    print(" 4. Why and how this project was chosen")
    option=int(input("What do you wanna read : "))
    if(option==1):
        intro()
    elif(option==2):
        problem()
    elif(option==3):
        objective()
    elif(option==4):
        choose()
    else:
        print("Invalid input!")

def intro():
    print("\n")
    file = open('intro.txt', 'r')
    print file.read()
def problem():
    print("\n")
    file = open('problem.txt', 'r')
    print file.read()
def objective():
    print("\n")
    file = open('objective.txt', 'r')
    print file.read()
def choose():
    print("\n")
    file = open('choose.txt', 'r')
    print file.read()
