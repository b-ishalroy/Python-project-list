import random

def guess_the_number():
    # Define the range
    lower_bound = 1
    upper_bound = 100

    # Generate a random number within the range
    target_number = random.randint(lower_bound, upper_bound)

    print(f"Welcome to 'Guess the Number'!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

    attempts = 0
    while True:
        # Increment the attempt counter
        attempts += 1

        # Get the user's guess
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check if the guess is correct
        if guess < target_number:
            print("Your guess is too low.")
        elif guess > target_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
