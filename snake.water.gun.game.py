"""
Snake vs. Water: Snake drinks the water hence wins.
Water vs. Gun: The gun will drown in water, hence a point for water.
Gun vs. Snake: Gun will kill the snake and win.

1 for snake
-1 for water
0  for gun.

"""
import random
print("Welcome to Snake-Water-Gun Game!")
print("Choose one:\n1 for Snake\n-1 for Water\n0 for Gun")

try:
    computer = random.choice([1, -1, 0])
    user     = int(input("Enter a number:"))
    print(f"Computer choosed: {computer} and you choosed: {user} SO:")

    if(computer==user):
        print("You both choosed the same!,Its a tie")

    elif(user ==1 and computer ==-1 or user==-1 and computer==0 or user==0 and computer==1):
        print("You won")

    else:
        print("You lose")

except ValueError:
    print("Your value should be :[1,or -1,or 0")


