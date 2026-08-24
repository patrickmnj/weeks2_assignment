Number Guessing Game

A simple interactive **Python command-line number guessing game** where the player tries to guess a randomly generated number between **1 and 100**.

The game includes different difficulty levels, limited attempts, score tracking, input validation, and the option to play multiple rounds.

 Features

* 🎲 Randomly generated numbers
* 🎚️ Three difficulty levels:

  * **Easy** – 10 attempts
  * **Medium** – 7 attempts
  * **Hard** – 5 attempts
* 🏆 Score tracking
* 💡 Higher/Lower hints
* 🔢 Input validation
* ⚠️ Handles invalid user input
* 🔄 Play again option
* 📊 Tracks attempts and remaining score

 Technologies Used

* **Python 3**
* `random` module
* Conditional statements (`if`, `elif`, `else`)
* `while` loops
* Functions
* `try/except` error handling
* User input

## ▶️ How to Run
1. Clone the repository

```bash
git clone https://github.com/patrickmnj/weeks2_assignment.git
```

2. Open the project

```bash
cd weeks2_assignment
```

3. Run the game

```bash
python weeks2_assignment.py
```

 How to Play

1. Start the game.
2. Select a difficulty level.
3. The computer generates a random number between **1 and 100**.
4. Enter your guess.
5. The game tells you whether your guess is **Too High** or **Too Low**.
6. Continue guessing until you find the correct number or run out of attempts.
7. Your score is displayed at the end.
8. Choose whether to play again.

Scoring

The game starts each round with a score of **100 points**.

| Difficulty | Attempts | Points Lost        |
| ---------- | -------- | ------------------ |
| Easy       | 10       | 5 per wrong guess  |
| Medium     | 7        | 10 per wrong guess |
| Hard       | 5        | 20 per wrong guess |

The higher the difficulty and the fewer guesses you use, the better your score.

Example

```text
============================
     NUMBER GUESSING GAME
============================

Choose difficulty:
1. Easy - 10 attempts
2. Medium - 7 attempts
3. Hard - 5 attempts

Choose 1, 2, or 3: 2

Difficulty: Medium
You have 7 attempts.
Starting score: 100

Guess the number (1-100): 50
Too Low!

Attempts remaining: 6
Current score: 90

Guess the number (1-100): 75
Too High!

Guess the number (1-100): 63
🎉 Correct!

The number was 63.
Attempts used: 3
Final score: 80
```
What I Learned:

This project helped me practice:

* Python variables and data types
* User input
* Conditional statements
* `while` loops
* Functions
* Random number generation
* Error handling with `try/except`
* Input validation
* Basic game logic
* Git and GitHub

Future Improvements

Possible future features include:

* Add a leaderboard
* Save high scores
* Add hints
* Add different number ranges
* Add a timer
* Add multiplayer mode
* Store scores in a file or database


Patrick Njuguna

Built as part of my Python learning journey.




