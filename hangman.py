import random
from lists import word_list
name_check = True
play_again = True
word_list = ['Word', 'another', 'other', 'something']


def game_display_update(game_progress_list):
    print("Guess the word: " + "".join(str(count) for count in game_progress_list) +
          "\nAlready played:", already_guessed or '{}')


def string_check(entry_context: str, negative_message: str,
                 max_length: int, expected_input: str = "abcdefghijklmnopqrstuvwxyz") -> str:
    while True:
        string_input = input(f"\nPlease enter your {entry_context}: ")
        if string_input.isalpha() and len(string_input) <= max_length and string_input[0:1].lower() in expected_input:
            return string_input
        else:
            print(f"\"{string_input}\" {negative_message}")


print("Welcome to hangman " + string_check("name", "is not a correct entry, try again", 30)
      + ", you start with 8 lives.")

# while name_check:
#     name = input("\nPlease enter your name: ").capitalize()
#     if name.isalpha():
#         print(f"\n{name}, welcome to hangman! \nYou have 8 attempts to guess the word:\n")
#         name_check = False
#     else:
#         print(f"\"{name}\" is not a valid answer, try again")

while play_again:

    game_end_message = "Congratulations"
    lives_remaining = 8

    chosen_word = word_list[int(random.uniform(0, len(word_list)))].lower()
    game_progress = ["_"] * len(chosen_word)
    already_guessed = set()

    while game_progress.count("_") > 0 and lives_remaining > 0:

        game_display_update(game_progress)
        guessed_letter = string_check("guess", "is not a correct entry, try again", 1)
        same_turn = True

        while same_turn:
            if guessed_letter in already_guessed:
                print(f"\nYou've already guessed this, you still have {lives_remaining} lives remaining.")
                break
            elif guessed_letter in chosen_word:
                same_turn = False
                print(f"\nCorrect, you still have {lives_remaining} lives remaining.")
                already_guessed.add(guessed_letter)
                for i in range(len(game_progress)):
                    if chosen_word[i:i+1] == guessed_letter:
                        game_progress[i:i+1] = guessed_letter
            else:
                same_turn = False
                lives_remaining -= 1
                print(f"\nIncorrect, you have {lives_remaining} lives remaining.")
                already_guessed.add(guessed_letter)

        if lives_remaining == 0:
            game_end_message = "Sorry"

    try_again_var = input(f"\n{game_end_message}, try again? (Y/N): ").upper()
    if try_again_var == "N":
        play_again = False


