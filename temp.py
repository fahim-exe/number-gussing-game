import random as R

def guess_the_number(level:str):
    number = R.randint(1,100)

    ez = 10
    hr = 5
    counter = 0

 
        

    while True:

        if counter>=1 and level.lower() == "easy":
            
            print(f"You have {ez-counter} attempts to guess the number.")
            user = int(input("Make a guess: "))
            counter+=1

        if counter>=1 and level.lower() == "hard":
            
            print(f"You have {hr-counter} attempts to guess the number.")
            user = int(input("Make a guess: "))
            counter+=1
        
        if counter==0 and level.lower()=="easy":            
            print(f"You have {ez-counter} attempts to guess the number.")
            user = int(input("Make a guess: "))
            counter +=1

        
        if counter==0 and level.lower()=="hard":
            counter+=1
            print(f"You have {hr-counter} attempts to guess the number.")
            user = int(input("Make a guess: "))
            counter +=1


        


        if counter>=1:


            if user>number:
                print("Too high.")
                if counter>9 and level.lower()=="easy":
                    print("You've run out of guesses, you lose.")
                    break
                if counter>5 and level.lower()=="hard":
                    print("You've run out of guesses, you lose.")
                    break
                
                else:
                    print("Guess again.")
                    continue

            if user<number:
                print("Too low.")
                if counter>5 and level.lower()=="hard":
                    print("You've run out of guesses, you lose.")
                    break
                if counter>9 and level.lower()=="easy":
                    print("You've run out of guesses, you lose.")
                    break

                else:
                    print("Guess again.")
                    continue

            if user==number:
                print(f"You got it. The answer was {number}")
                break


        


        
