import random
import hangman_words
import hangman_art

word_list=hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

while display.count("_")>0 and lives>=0:
    guess = input("Guess a letter: \n").lower()

    if(guess not in chosen_word):
      print(f"You guessed the letter {guess} which is not there in the word. You lose a life")
      print(hangman_art.stages[lives])
      lives-=1
    else:
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
      print(display)


if(display.count("_")==0):
  print("You win!!")
else:
  print("You lose!!")
