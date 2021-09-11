
# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
r = 1
p = 2
s = 3

if r==1:
	print("rock")

if p==2: 
	print("paper")

if p==3: 
	print("scissors")






