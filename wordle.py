import random

def read_words():
    
    with open("words.txt",'r') as file:
        words = file.readlines()
        words = [word.strip() for word in words]
        return(words)

def target_word():
    words = read_words()
    target = random.choice(words)
    return target

def game_state():
    attempts = 6
    guessed_words = []
    guessed_feedback = []
    return attempts, guessed_words, guessed_feedback

def feedback(target, guess):
    feedback = ""
    for i, letter in enumerate(guess):
        if letter == target[i]:
            feedback += "🟩"
        elif letter in target:
            feedback += "🟨"
        else:
            feedback += "⬜"
    return feedback



def game_loop(target):

    attempts, guessed_words, guessed_feedback = game_state()

    while attempts > 0 and target not in guessed_words:
        
        print("you have {} attempts left".format(attempts))
        
        if guessed_words:
            print("\nYour guesses so far:")
            for word, fb in zip(guessed_words, guessed_feedback):
                print(f"{word}\n{fb}\n")

        guess = input("Please enter a word: ").strip().lower()
        
        if len(guess) != 5:
            print("Invalid guess! Your word must be exactly 5 letters long.")
            continue
        
        if not guess.isalpha():
            print("Invalid guess! Please enter a word with only letters.")
            continue

        if guess not in read_words():
            print("Invalid guess! Your word must be a valid English word.")
            continue

        if guess in guessed_words:
            print("You have already guessed that word")
            continue

        guessed_words.append(guess)
        fb = feedback(target, guess)
        guessed_feedback.append(fb)

        if guess == target:
            print("You win!")
            break
        else:
            print("Incorrect guess.")
            print("Feedback: ", feedback(target, guess))
            attempts -= 1
            
        if attempts == 0:
            print("Game over! The word was '{}'.".format(target))

def wordle():
    target = target_word()
    game_loop(target)

try:
    wordle()
except KeyboardInterrupt:
    print("\nGame aborted.")
except FileNotFoundError as e:
    print("Error: File not found.")
except Exception as e:
    print("An error occured:", e)