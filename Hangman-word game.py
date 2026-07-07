import time
import random

def choose_word():
    words = ['python', 'programming', 'treasure', 'creative', 'medium', 'horror']
    return random.choice(words)

def wordDisplay(word, guesses):
    display_word = ''
    for char in word:
        if char in guesses:
            display_word += char + ' '
        else:
            display_word += '_ '
    return display_word.strip()

def winningCondition(updated_word, turns):
    if '_' not in updated_word:
        return 1 
    elif turns == 0:
        return 0

if __name__ == '__main__':
    name = input("What is your name? ")
    print("Hello, " + name + ", time to play hangman!")
    time.sleep(1)
    print("Start guessing...\n")
    time.sleep(0.5)

    word = choose_word()
    turns = len(word)  
    guesses = ''

    while turns > 0:
        print("\nYou have", turns, 'guesses remaining')
        print(wordDisplay(word, guesses))
        guess = input("\nguess a character: ").lower()

        if guess in guesses:
            print("\nYou have already tried this letter")
            continue
        else:
            guesses += guess

        if guess not in word:
            print("\nWrong, Try again")

        updated_word = wordDisplay(word, guesses)
        turns -= 1
        flag = winningCondition(updated_word, turns)

        if flag == 0:
            print("\nYou Lose")
            print("The word was", word)
            break
        elif flag == 1:
            print("\nYou won!")
            print("You guessed", word, "correctly")
            break
    else:
        print("\nYou Lose")
        print("The word was", word)
