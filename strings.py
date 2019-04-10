# String Types Exercises

#1
repeat = "blah " * 10

print (repeat)

#2
#Make a variable with the phrase "Today is a nice day" and then slice the variable to only
#show the part of the string "nice".
phrase = "Today is a nice day"
print(phrase.index("n"))
# n=11
print(phrase[11:15])

#3

# school = "Wilson Senior High School"
# mascot = "Bulldog"

my_string = "I went to {}, and the mascot was a {}"

print(my_string.format("Wilson Senior High School", "Bulldog"))

#4

print(phrase.upper())
print(phrase.lower())

#5
print(phrase.isalpha())

#6
print(phrase.find("not"))

#7

print(phrase.find("Today"))
print(phrase.startswith("Today"))


#8
print(phrase.replace("Today", "Yesterday"))

#9

#Make a variable that holds the string Hello world. My name is {}. I am in the Immersive Data Analytics Class"
#then use the .split function to separate the string by  the period symbol(.)
name = "Laura Ann"
nine = "Hello world. My name is {}. I am in the Immersive Data Analytics Class".format(name)

# splits at period
ninesplit = nine.split(". ")
                 
for item in ninesplit:
    print (item + "\n")



#10

white = "  too much white space   ."
print (white.rstrip())
print (white.lstrip())
print (white.strip())


#11

languages = "Python\nJava\nPHP\nPerl\nJavascript\nC++"
print (languages)

#12

fav = input("What is your favorite color? ")
print ("Your favorite color is ", fav)


