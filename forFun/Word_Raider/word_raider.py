import random

game_name = "Word Raider or Guess a Word"
word_bank = []

with open ("words.txt") as word_file:
    for line in word_file:
        word_bank.append(line.rstrip().lower())
        
selected_word = random.choice(word_bank)

incorrect_letters = []
misplaced_letters = []
max_turns = 6
used_turns = 0

print(f"Welcome to {game_name}!")
print(f"The word to guess has {len(selected_word)} letters.")
print(f"You have {max_turns} turns to guess the word!")

while used_turns < max_turns:
    guess = input("Guess a word (or type 'stop' to end game):").lower().strip()
    
    if guess == "stop":
        print("Game stopped. Tanks for playing!")
        break
        
    if len(guess) != len(selected_word) or not guess.isalpha():
        print(f"Please enter a {len(selected_word)}-letter word.")
        continue

index = 0

while used_turns < max_turns:
    guess = input("Guess a word: ").lower().strip()
    if guess == "stop":
        break
    if len(guess) != len(selected_word) or not guess.isalpha():
        print("Please enter a 5 letter word.")
        continue
        
    index = 0
    for letter in guess:
        if letter == selected_word[index]:
            print(letter, end=' ')
            if letter in misplaced_letters:
                misplaced_letters.remove(letter)
        elif letter in selected_word:
            if letter not in misplaced_letters:
                misplaced_letters.append(letter)
            print("_", end=' ')
        else:
            if letter not in incorrect_letters:
                incorrect_letters.append(letter)
            print("_", end=' ')
        index += 1
        
    if guess == selected_word:
        print("\n🎉 Congratulations! You guessed the word!")
        break
            
    used_turns += 1
    
    if used_turns == max_turns:
        print(f"Game over, you lost. The word was: {selected_word}")
        break
    
    print("\nMisplaced letters: ", misplaced_letters)
    print("Incorrect letters: ", incorrect_letters)
    print(f"You have {max_turns - used_turns} turns left.")
