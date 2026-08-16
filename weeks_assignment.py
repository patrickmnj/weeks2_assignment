
# # =========================================
# # NUMBER GUESSING GAME
# # =========================================

# # -----------------------------------------
# # STEP 1: IMPORT RANDOM
# # -----------------------------------------

# # The random module allows Python to
# # generate random numbers.
# import random


# # -----------------------------------------
# # STEP 2: GENERATE SECRET NUMBER
# # -----------------------------------------

# # Generate a random number between 1 and 100.
# secret_number = random.randint(1, 100)


# # -----------------------------------------
# # STEP 3: WELCOME THE PLAYER
# # -----------------------------------------

# print("================================")
# print("     NUMBER GUESSING GAME")
# print("================================")

# print("I have chosen a number between 1 and 100.")
# print("Try to guess the number!")


# # -----------------------------------------
# # STEP 4: CHOOSE DIFFICULTY
# # -----------------------------------------

# print("\nChoose your difficulty:")
# print("1. Easy   - 10 attempts")
# print("2. Medium - 7 attempts")
# print("3. Hard   - 5 attempts")

# difficulty = input("Enter 1, 2, or 3: ")


# # -----------------------------------------
# # STEP 5: SET MAXIMUM ATTEMPTS
# # -----------------------------------------

# if difficulty == "1":

#     max_attempts = 10
#     print("You selected Easy.")

# elif difficulty == "2":

#     max_attempts = 7
#     print("You selected Medium.")

# elif difficulty == "3":

#     max_attempts = 5
#     print("You selected Hard.")

# else:

#     # If the user enters an invalid choice,
#     # Easy will be selected automatically.
#     max_attempts = 10
#     print("Invalid choice. Easy difficulty selected.")


# # -----------------------------------------
# # STEP 6: CREATE ATTEMPT COUNTER
# # -----------------------------------------

# # The player has not made any guesses yet.
# attempts = 0


# # -----------------------------------------
# # STEP 7: CREATE GAME LOOP
# # -----------------------------------------

# # The while loop keeps the game running
# # while the player still has attempts.
# while attempts < max_attempts:

#     # Ask the player for a guess.
#     guess = int(input("\nEnter your guess: "))

#     # Add one to the attempt counter.
#     attempts += 1

#     # Calculate how many attempts remain.
#     remaining = max_attempts - attempts

#     print("Attempts used:", attempts)
#     print("Attempts remaining:", remaining)


#     # -------------------------------------
#     # STEP 8: CHECK IF GUESS IS CORRECT
#     # -------------------------------------

#     if guess == secret_number:

#         print("\nCorrect! 🎉")
#         print("You guessed the number!")
#         print("Attempts used:", attempts)

#         # break stops the while loop.
#         break


#     # -------------------------------------
#     # STEP 9: CHECK IF GUESS IS TOO HIGH
#     # -------------------------------------

#     elif guess > secret_number:

#         print("Too High!")


#     # -------------------------------------
#     # STEP 10: GUESS IS TOO LOW
#     # -------------------------------------

#     else:

#         print("Too Low!")


# # -----------------------------------------
# # STEP 11: CHECK FOR GAME OVER
# # -----------------------------------------

# # If all attempts have been used and
# # the player did not guess correctly,
# # the game is over.
# if attempts == max_attempts and guess != secret_number:

#     print("\nGAME OVER!")
#     print("You used all your attempts.")
#     print("The secret number was:", secret_number)


# # -----------------------------------------
# # END OF GAME
# # -----------------------------------------

# print("\nThanks for playing!")





import random

secret_number = random.randint(1, 100)

print("Secret number:", secret_number)

print("Choose difficulty:")
print("1. Easy - 10 attempts")
print("2. Medium - 7 attempts")
print("3. Hard - 5 attempts")

difficulty = input("Choose 1, 2, or 3: ")

if difficulty == "1":
    max_attempts = 10
elif difficulty == "2":
    max_attempts = 7
elif difficulty == "3":
    max_attempts = 5
else:
    print("Invalid choice. Using Easy.")
    max_attempts = 10

attempts = 0

# while True:
    # guess = int(input("Guess the number: "))
while attempts < max_attempts:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess == secret_number:
        print("Correct!")
        print("Attempts:", attempts)
        break

    elif guess > secret_number:
        print("Too High!")
        print("Attempts:", attempts)

    else:
        print("Too Low!")
        print("Attempts:", attempts)
    if attempts == max_attempts:
        print("Game over!")
        print("The secret number was:", secret_number)
        
print("\nThanks for playing!")


