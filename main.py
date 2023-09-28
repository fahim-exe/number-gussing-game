import number_guess as Guess

#1- takes "easy" or "hard" input
#2- easy has 10 attempts, hard has 5 attempts
#3- if the number is greater it replies too high
#4- if the number is lower it replies too low
#5- if guess is wrong replies with remaining attempts and takes the guess again


while True:
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty level. Type 'easy' or 'hard' or type 'q' to exit : ")

    if level.lower()=="q":
        exit()
        break
        

    if level.lower()=="easy" or level.lower()=="hard":   

        Guess.guess_the_number(level)

        level = input("Want to go again???? Type 'y' to go again or 'q' to quit the game.")
        if level.lower()=="q":
            exit()

    else:
        print("Please enter a valid level")
        continue