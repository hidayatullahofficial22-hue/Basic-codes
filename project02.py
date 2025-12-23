  from random import randint
choice = input("Do you want to play the game?(yes/no)")

while(choice != "no"):

    n = randint (1,100)
    
    max_guess = 6

    print("Note: You only have 6 attempts.")

    user = int(input("Guess a Number in range of (1....100) please!"))

    guess = 0

    while(guess < max_guess):

        guess = guess + 1

        if(user == n):
        
         print(f"Great! you guess number in {guess} attempts.")

         break

        elif(user > n):

            user = int(input("Guess a lower number please!"))

        else:

            user = int(input("Guess a higher number please!"))

    if(guess == max_guess):
                
                print("You used your full attempts without guessing correct number")

    choice = input("Do you want to play the game again?(yes/no)")

print(" Thanks for playing the game. ")

