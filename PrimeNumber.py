#Laura Adam
#April 8, 2019

# Write and application that will show a list of numbers and indicate whether ir not they are prime.
# the user will input the last number in the range
# The application will print all of the numbers from 1 to that number
# and indicate if they are prime or not


#Python hates tabs (5 spaces) Python likes four spaces!!

# Enter the upper limit
r=int(input("Enter upper limit: "))


for a in range(2,r+1):
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
			
    if(k<=0):
        print(a, " is a prime number")
    else:
	    print(a, "is Not a prime number")
		
#Yaay!