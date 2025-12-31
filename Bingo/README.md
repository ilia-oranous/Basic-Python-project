🎯 Number Guessing Game (Python)

A simple number guessing game written in Python, where the computer randomly selects a number between 0 and 100 and the user tries to guess it.

📌 Project Overview

In this game:

The computer generates a random number between 0 and 100

The user enters a number as a guess

The program tells the user whether the guess is too low or too high

The game continues until the correct number is guessed

The total number of attempts is displayed at the end

🧠 Concepts Used

This project is great for practicing fundamental Python concepts such as:

Functions

while loops

Error handling with try / except

Recursion

User input validation

Random number generation

🛠 How the Program Works
1. Generate a Random Number

The computer randomly selects a number between 0 and 100.

2. Get User Input

The user is prompted to enter a number within the valid range.
Invalid inputs are handled gracefully.

3. Compare Numbers

If the guess is correct → the game ends

If the guess is too low → a hint is shown

If the guess is too high → a hint is shown

4. Count Attempts

Each guess is counted and displayed once the correct number is found.

▶️ How to Run

Make sure Python is installed (Python 3 recommended)

Save the file as Bingo.py

Run the program:

python Bingo.py

📂 File Structure
Bingo.py
README.md

🎉 Example Output
Enter a number between 0 and 100: 50
Your number is too low....
Attempt #2
Enter a number between 0 and 100: 75
Your number is too high....
Attempt #3
Enter a number between 0 and 100: 63
Congratulations! You guessed the number 63 in 3 attempts!

🚀 Future Improvements (Optional)

Add difficulty levels (easy / medium / hard)

Limit the number of attempts

Add a replay option

Convert the game to a GUI version

👤 Author

Ilia Oranous
Computer Science Student
Python Practice Project