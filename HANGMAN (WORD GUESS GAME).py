import random 

words = ["apple", "brain", "code"] 
word = random.choice(words) 
guessed = [] 
attempts = 6 

print("Welcome to the Word Guessing Game")

while attempts > 0: 
    display_word = "".join([c if c in guessed else "_" for c in word])
    print(f"Word: {display_word}")
    print(f"Attempts remaining: {attempts}")
    
    letter = input("Guess a letter: ").lower() 
    
    if letter in guessed:
        print("You already guessed that letter!")
        continue

    if letter in word: 
        guessed.append(letter)
        print(f"Good job! '{letter}' is in the word.")
    else: 
        attempts -= 1 
        print(f"Sorry, '{letter}' is not there.")

    if all(c in guessed for c in word):
        print(f"Congratulations! You win! The word was: {word}")
        break
else:
    print(f"You lose! Out of attempts. The word was: {word}")
