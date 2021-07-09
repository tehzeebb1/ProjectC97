import random 
chances=0
number= random.randint(1,9)
print("Number Guessing Game")
print("Guess a number (Between 1 and 9)")

while chances<5:
    guess= int(input("Enter your guess:"))

    if guess == number: 
    #if number is the same as the generated 
    #number by randint function then break from loop using loop
    #control statement  break
        print("Congratulations you WON!")
        break
    elif guess < number:
        print("Your guess is to LOW: Guess a higher number than", guess)

    else:
        print("Your guess is to HIGH: Guess a lower number than", guess)
    chances += 1

if not chances <5: 
    print("You LOSE! The number was", number)