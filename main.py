import random

def get_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.\n")

def create_target_number(min_value, max_value):
    return random.randint(min_value, max_value)

def play_game():
    print("Welcome to the guessing game!")

    while True:
        min_value = get_number("Enter the minimum value: ")
        max_value = get_number("Enter the maximum value: ")

        if min_value >= max_value:
            print("The minimum value should be less than the maximum value.\n")
            continue

        target_number = create_target_number(min_value, max_value)

        while True:
            guess = get_number(f"Enter a number between {min_value} and {max_value}: ")

            if guess == target_number:
                print(f"Congratulations! You guessed the correct number: {target_number}")
                break
            elif guess < min_value or guess > max_value:
                print(f"Your guess is out of the range. Try again.")
            else:
                print(f"Incorrect guess. Try again.")

        play_again = input("Do you want to play again? (y/n) ").lower()
        if play_again != "y":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()