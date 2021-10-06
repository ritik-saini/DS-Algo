#Game of guessing numbers between two ranges with limited chances
import random
import math

lower = int(input('Enter lower bound : '))
upper = int(input('Enter upper bound : '))
x = random.randint(lower, upper)
print("\nyou've only", round(math.log(upper-lower+1, 2)),"chances to get the integer.")
count = 0
while (count<math.log(upper-lower+1, 2)): #chances to guess the correct number
    count+=1
    guess = int(input('\tGuess the number : '))
    if x == guess:
        print('Congratulations you did it in',count,'try')
        break
    elif x>guess:
        print('You guessed too small')
    elif x<guess:
        print('You guessed too high')
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")