name = input("Type your name : ")
print("Welcome", name ,"to this adventure!")

answer = input("You are on a dirt road, it has come to an end, it can go either left or right.Which way would you like to go  ").lower()

if answer == "left":
    answer = input("Type walk to walk around and swim to swim accross: (swim/walk) ").lower()

    if answer == "swim":
        print("You swam across and were eaten by a crocodile ")
    elif answer == "walk":
        print("You walked for several kilometers and ran out of food and water ")
    else:
        print("Choose a valid option ")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)").lower()
   
    if answer == "back":
        print("Your leg got struck in one of the wooden piers and you bled till death")
    elif answer == "cross":
     answer == input(" Choose if you really wa to take the risk of crossing the wobbly bridge (Yes/No)") 
    if answer == "yes":
        print("Hurrah! You crossed the wobbly bridhe and a vieled stranger gives you gold. YOU WON!!")
    elif answer == "no":
        print("You went back fearing the danger and you remain poor for life. ")    
    else:
        print("Please choose a valid option  ")        
else:
    print("Not a valid option. Please choose a valid option ")
print("Thanks for trying. Have an adventurous day ahead !! ")