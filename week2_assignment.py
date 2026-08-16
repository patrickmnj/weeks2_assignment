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
        