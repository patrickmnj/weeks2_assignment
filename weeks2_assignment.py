
import random


while True:

    secret_number = random.randint(1, 100)

print("==")
print("number guessing game")
print("===")

    # print("Secret number:", secret_number)


# print("Secret number:", secret_number)

print("Choose difficulty:")
print("1. Easy - 10 attempts")
print("2. Medium - 7 attempts")
print("3. Hard - 5 attempts")

difficulty = input("Choose 1, 2, or 3: ")

score = 100

if difficulty == "1":
    max_attempts = 10
    print("score:", score)
elif difficulty == "2":
    max_attempts = 7
    
    print("score:", score)
elif difficulty == "3":
    max_attempts = 5

    print("score:", score)
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
        score -= 10
        print("score:", score)
        break

    elif guess > secret_number:
        print("Too High!")
        print("Attempts:", attempts)
        score -= 10
        print("score:", score)

    else:
        print("Too Low!")
        print("Attempts:", attempts)
        score -= 10
        print("score:", score)

    if attempts == max_attempts:
        print("Game over!")
        print("The secret number was:", secret_number)
        
print("\nThanks for playing!")
while True:


    print("\nThanks for playing!")

    play_again = input("Would you like to play again? (y/n): ").lower()

    if play_again == "y":
        print("starting a new game...")
        continue
    else:
        print("Goodbye!")
        break
