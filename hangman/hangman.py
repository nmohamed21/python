#Step 5
import hangman_art
import hangman_words
import random
from replit import clear 

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(hangman_art.logo)



#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
    if guess in display:
      print(f"you already guessed {guess} this letter")
    #Check if user is wrong.
    if guess not in chosen_word:
        
        lives -= 1
        print(f"the letter you choose {guess} is Not in the word")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"{chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    

    print(hangman_art.stages[lives])
play_again = input("do You Want to play agian y/n").lower()
if play_again =="y":
      end_of_game == False