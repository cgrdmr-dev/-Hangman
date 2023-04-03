import random
from art import logo,stages
from hangman_words import word_list

chosen_word = random.choice(word_list)

print(logo)
# print(chosen_word) #answer

lives = 6

display = []
word_lenght = len(chosen_word)
for _ in range(word_lenght):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:

    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed  {guess}")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])