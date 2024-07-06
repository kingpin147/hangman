import random

# Load wordlist from a file
with open('./hangman/wordlist.txt') as f:  # Assuming file is in the same directory
    wordlist = [line.strip().lower() for line in f]  # Read as lowercase words

word = random.choice(wordlist)
allowed_guesses = 7
guesses = []
done = False

while not done:
    # Display current state of the word
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")  # Newline after each word display

    # Check for win condition
    if all(letter in guesses for letter in word):
        done = True
        break

    # Get player's guess
    guess = input(f"Allowed Errors Left: {allowed_guesses}, Next Guess: ").lower()
    
    # Validate guess
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid guess. Please enter a single letter.")
        continue

    guesses.append(guess)

    # Check if guess is incorrect
    if guess not in word:
        allowed_guesses -= 1
        if allowed_guesses == 0:
            break

# Game over
if done:
    print(f"You Win! It was '{word}'!")
else:
    print(f"You Lose! It was '{word}'!")
