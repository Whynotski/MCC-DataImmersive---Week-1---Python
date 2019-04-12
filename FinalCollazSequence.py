# April 9, 2019
#MCC-Immersive Data Science

# Collatz Sequence 
# https://en.wikipedia.org/wiki/Collatz_conjecture

##  The Collatz conjecture, is named after Lothar Collatz, who introduced the idea in 1937,  
# is a conjecture in mathematics that concerns a sequence defined as follows: 
# start with any positive integer n. Then each term is obtained from the previous term as follows: 
# if the previous term is even, the next term is one half the previous term. 
# If the previous term is odd, the next term is 3 times the previous term plus 1. 
#The conjecture is that no matter what value of n, the sequence will always reach 1.

# Use this website to check your program's output
# https://www.dcode.fr/collatz-conjecture


#def question():
q = input(" Would you like to evaluate a number against the Collatz conjecture?  Enter Y or N: ")
#if q == "Y":
if q == "N":
      print (" Thanks for remembering Lothar Collatz, Goodbye!")
else:
      #collatz(num)

    def collatz(num):
        while num != 1:
            print(num)
            if num % 2 == 0:
                num = int(num / 2)
            else:
                num = int(3 * num + 1)
        else:
            print(num)
            print('Done!')

def main():
    num = int(input('Input an integer: '))
    collatz(num)

main()

