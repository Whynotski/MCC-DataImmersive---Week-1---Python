#Laura Adam

# Write a program that prints the numbers from 1 to 100.
#For multiples of 3 print “Fizz” instead of the number.
#For the multiples of five print “Buzz”.
#For numbers which are multiples of both 3 and 5 print “FizzBuzz”.



for fizzbuzz in range(100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
	
