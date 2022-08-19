
from words import words
from hangman_visual import lives_visual_dict
import random
import string


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()


def hangman():
    
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 7

    while len(word_letters)>0 and lives>0:
        print('You used',lives ,'left and you used these letters ',' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word'," ".join(word_list))


        user_letter = input("Guess a letter:").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives -1
                print("not in the word",user_letter)
        elif user_letter in used_letters:
            print("You already used before")

        else:
            print("Invalid Character")

    if lives==0:
        print("You died sorry,the word was",word)
    else:
        print("you guessed the word!!!!!!!",word)
hangman()