from random import randint

MAX_NUMBER = 100
MIN_NUMBER = 0

def get_number():
    try:
        number = int(input("Enter a number between 0 and 100: "))
        if number > 100 or number < 0:
            raise ValueError("Your number must be in range 0 to 100...\n")
        return number
    except ValueError as e:
        print(f"Invalid input: {e}")
        return get_number()  # Ask again for valid input

def generate_number():
    return randint(0, 100)

def compare(user: int, pc: int):
    if user == pc:
        return True
    elif user < pc:
        print("Your number is too low....")
        return False
    else:
        print("Your number is too high....")
        return False

def main():
    pc_number = generate_number()
    attempts = 1
    
    # First attempt
    user_number = get_number()
    if compare(user_number, pc_number):
        print(f"Good! You guessed the number at first attempt!")
        return
    
    # Continue guessing
    while True:
        attempts += 1
        print(f"Attempt #{attempts}")
        user_number = get_number()
        if compare(user_number, pc_number):
            print(f"Congratulations! You guessed the number {pc_number} in {attempts} attempts!")
            break

if __name__ == "__main__":
    main()
