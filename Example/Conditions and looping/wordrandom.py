import random

# List of words to choose from
words = ["apple", "banana", "cherry", "durian", "elderberry"]

# Select a random word from the list
word = random.choice(words)

# Number of attempts allowed
max_attempts = 5

# Initialize the guessed word with underscores
guessed_word = "_" * len(word)

# Loop until the word is guessed or the maximum attempts are reached
while max_attempts > 0 and guessed_word != word:
    print("Guess the word:", guessed_word)
    print("Attempts left:", max_attempts)
    
    # Get user input for a letter
    letter = input("Enter a letter: ")
    
    # Check if the letter is in the word
    if letter in word:
        # Update the guessed word with the correctly guessed letter
        new_guessed_word = ""
        for i in range(len(word)):
            if word[i] == letter:
                new_guessed_word += letter
            else:
                new_guessed_word += guessed_word[i]
        guessed_word = new_guessed_word
        print("Correct guess!")
    else:
        print("Wrong guess!")
        max_attempts -= 1
    
    print()  # Empty line for readability

# Check if the player won or lost
if guessed_word == word:
    print("Congratulations! You guessed the word correctly:", word)
else:
    print("Game over! The word was:", word)
