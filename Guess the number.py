import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)
    max_attempts = 10
    attempts = 0
    
    print(f"Guess a number between {lower_bound} and {upper_bound}. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            if guess < lower_bound or guess > upper_bound:
                print(f"Please guess a number between {lower_bound} and {upper_bound}.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
