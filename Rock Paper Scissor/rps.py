# Rock Paper Scissor Game (Python)

A simple console-based Rock-Paper-Scissor game written in Python.  
This project is part of my Python learning journey and focuses on basic programming concepts and input validation.

## 🎯 Project Goals
- Practice Python fundamentals
- Work with functions and conditionals
- Handle user input and validation
- Use random choice for computer moves

## ▶️ How to Run

Make sure Python is installed on your system, then run:

```bash
python rps.py

from random import choice

# Available choices for the game
available_vaules = ['paper', 'rock', 'scissor']

user_value = ''
pc_value = ''

def is_correct(s: str):
    """
    Validates user input.
    Returns True if input is one of the allowed values.
    """
    if not s:
        print("Input cannot be empty.")
        return False

    s = s.strip().lower()

    if s in available_vaules:
        return True

    print(f"Invalid input. Choose from {available_vaules}.")
    return False


def get_user_value():
    """
    Gets and validates user input.
    Keeps asking until a valid value is entered.
    """
    global user_value
    while True:
        s = input("Choose between (paper, rock, scissor): ")
        if is_correct(s):
            user_value = s.strip().lower()
            break


def get_pc_value():
    """
    Randomly selects computer choice.
    """
    global pc_value
    pc_value = choice(available_vaules)


def compare():
    """
    Compares user and computer choices and returns the result.
    """
    if user_value == pc_value:
        return "Draw...\n"

    if (user_value == 'rock' and pc_value == 'scissor') or \
       (user_value == 'paper' and pc_value == 'rock') or \
       (user_value == 'scissor' and pc_value == 'paper'):
        return f"User with {user_value} wins pc with {pc_value}\n"

    return f"PC with {pc_value} wins user with {user_value}\n"
