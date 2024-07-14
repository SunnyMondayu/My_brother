print("Welcome to my computer Quiz!")

playing = input("Do you want to play?   ")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("You answered it correctly!")
    score += 1
else:
    print("That's quite incorrect : (")
    
   
answer = input("What does GPU stand for?  ")
if answer.lower() == "graphics processing unit":
    print("You answered it correctly!")
    score += 1
else:
    print("That's quite incorrect : (") 


answer = input("What does www stand for?  ")
if answer.lower() == "world wide web":
    print("You answered it correctly!")
    score += 1
else:
    print("That's quite incorrect : (")    

answer = input("What was the name of the first computer ")
if answer.lower() == "eniac":
    print("You answered it correctly!")
    score += 1
else:
    print("That's quite incorrect : (")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("You answered it correctly!")
    score += 1
else:
    print("That's quite incorrect : (")    

print("You got " + str(score) + " questions correct ! ")
print("Your final score out of 5 is equal to ")
print(score)



