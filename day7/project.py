import random
from replit import clear
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
import hangman_word
anyf=random.choice(hangman_word.word)
print(anyf)
display=[]
live=6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
for _ in range(len(anyf)):
    display+="_"
print(display)
end_game=False
while not end_game: 
    guess=input("choose the letter : ").lower()
    clear()
    if guess in display:
      print(f"you've already selected {guess}")
    for pos in range(len(anyf)):
        letter =anyf[pos]
        if letter ==guess:
            display[pos]=letter
    print(display)
    if guess not in anyf:
        print(f"you choosed {guess} that's not in the word , you lose a life")
        live-=1
        if live==0:
            end_game=True
            print("you lose")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_game=True
        print("you win")
        # from hangman_stages import stages
print(stages[live])