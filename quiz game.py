print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() !="yes":
    quit()

print("Okay! let's play ")  
score = 0  

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score = score+1
else: 
    print("incorrect!")

answer = input("What does ALU stands for? ")
if answer.lower() == "arithmetic logical unit":
    print('correct!')
    score = score+1
else: 
    print("incorrect!")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score = score+1
else: 
    print("incorrect!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print('correct!')
    score = score+1
else: 
    print("incorrect!")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply":
    print('correct!')
    score = score+1
else: 
    print("incorrect!")
    
print("your got " + str(score) + " questions correct!") 
print("your got " + str((score / 5) * 100) + " %.") 
k=input()
print("thank you for playing")
l=input()
