#Data Science Immersive
#April 10, 2019
#Laura Adam


#You will be creating an interactive chat-bot type program.
#Eliza is a therapist program that interacts with the user.
#Your program will need to evaluate what the user asks and
#turn the user's input into a question that sounds like the therapist really cares.

#Your first task is to develop a program with a running loop.
#If the user types in "I am feeling great" or enter "Q", the program will stop running.
#Your program should print out the last input (as an output) every time before accepting new input.
#Make sure you are accommodating for NO case-sensitivity. (Q is the same as q)


print (" Hello, I'm Eliza, your therabot.", "\n" + "I am here to listen to whatever is on your mind.")

chat = input ("Would you like to chat? or Please enter q to quit")
answer = chat.lower()
if answer == "q":
    print("Goodbye for now. Remember you are never alone with Eliza")
else:
    concern = input("What is on your mind today?")
    print (concern)
    if concern.lower() =="i am feeling great":
        print("Goodbye and keep looking at the positives")
    else:
        print ("So, you are concerned about", concern, "today?")

