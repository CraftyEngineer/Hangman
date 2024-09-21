import random
import game_data as gd
from game_data import lives

print(gd.hangman_art)
chosen_word=random.choice(gd.word_list)
# print(chosen_word)

placeholder=""
for i in chosen_word:
  placeholder+="_ "
print(placeholder)

game_over=False
correct_letters=[]
# lives=6

while not game_over:
  guess=input("Enter a letter to guess: ")
  guess=guess.lower()

  display=""
  for j in chosen_word:

    if j==guess:
      display+=j
      display+=" "
      correct_letters.append(j)
    elif j in correct_letters:
      display+= j
    else:
      display+="_ "
  if guess not in chosen_word:
    lives-=1
    print(f"you have {lives} lives left")

    if lives==0:
      game_over=True
      print("You Lost!")
      print(chosen_word)
  print(display)
  if "_" not in display:
    game_over=True
    print("You Win!")
  print(gd.level_art[6-lives])