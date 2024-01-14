#created by ishami sebgoya on december 12 2023 
import random

def guess_the_number():
    correct_number = random.randint(0, 9)

    while True:
        try:
            user_guess = int(input("Guess the number (between 0 and 9): "))
            
            if user_guess < 0 or user_guess > 9:
                print("Please enter a number between 0 and 9.")
                continue
            
            if user_guess == correct_number:
                print("Congratulations! You guessed the correct number.")
                break
            else:
                print("Incorrect. Try again.")
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()