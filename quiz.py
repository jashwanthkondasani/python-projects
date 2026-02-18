import time
print("Welcome to the Quiz!")
time.sleep(2)
playing=input("Do you want to play?  ")

if playing !="yes":
    quit()  
print("Okay! Let's play :)")
answer=input("What does CPU stand for?  ")
if answer=="Central Processing Unit":
    print("Correct!")
else:
    print("Incorrect!")
answer=input("What does iam stand for?  ")
if answer=="Identity and Access Management":
    print("Correct!")
else:
    print("Incorrect!")
answer=input("What does vpc stand for?  ")
if answer=="Virtual Private Cloud":
    print("Correct!")
else:
    print("Incorrect!")