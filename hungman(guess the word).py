import random


'''def hungman(guesses, guess, current_word, status):
    for i in range(len(current_word)):
        if guess == current_word[i]:
            status[i].append(current_word)
        else:
            status[i].append('*')
    return status'''

def hungman(guesses, guess, current_word):
    status = ''
    for letter in current_word:
        if letter in guesses:
            status += letter
        else:
            status += '*'
    return status



word = ['laptop', 'desktop', 'keyword', 'mouse', 'software', 'hardware', 'technology', 'disk']
current_word = random.choice(word)
print("Welcome to Guess the word(HUNGMAN)")
game = True
guesses = []
c = 0
print(f'The word conists of {len(current_word)} letters.')
#status = ''
while game:
    c += 1
    print("Enter your guess")
    guess = input()
    if len(guess)==len(current_word):
        #guesses.append(guess)
        #result = hungman(guesses, guess,current_word,)
        if guess == current_word:
            print(f'You guessed the correct word in {c} attempts. Congrats!')
            game = False
            break
        else:
            print('You are wrong')
            game = False
            break
    if len(guess) == 1:
        if guess in current_word:
            guesses.append(guess)
        else:
            print('Letter not found in word.')
        result = hungman(guesses,guess,current_word)
        if result == current_word:
            print(result)
            print(f'You guessed the correct word in {c} attempts. Congrats!')
            game = False
        else:
            print(result)
            status = result
    else:
        print('Invalid entry')

