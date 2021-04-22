import random
import math

# from lists import word_list
name_check = True
play_again = True
word_list = ['Word', 'another', 'other', 'something', 'seemed']


def game_display_update(game_progress_list):
    print("\nGuess the word: " + "".join(str(count) for count in game_progress_list) +
          "\nAlready played:", already_guessed or '{}')


def string_check(entry_context: str, negative_message: str,
                 max_length: int, expected_input: str = "abcdefghijklmnopqrstuvwxyz") -> str:
    while True:
        string_input = input(f"\n{entry_context}")
        if string_input.isalpha() and len(string_input) <= max_length and string_input[0:1].lower() in expected_input:
            return string_input
        else:
            print(f"\"{string_input}\" {negative_message}")


print("\nWelcome to hangman " + string_check("Hello, please enter your name: ", "is not a correct entry, try again", 30)
      .capitalize() + f", each of your games will have a random word to guess. Good luck!")

while play_again:

    game_end_message = "SUCCESS Congratulations, you guessed the word "

    chosen_word = word_list[int(random.uniform(0, len(word_list)))].lower()

    lives_remaining = 5 + round(0.25 * math.log(len(chosen_word), 1.25))

    game_progress = ["_"] * len(chosen_word)
    already_guessed = set()

    print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-INITIALISED"
          "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    while game_progress.count("_") > 0 and lives_remaining > 0:

        game_display_update(game_progress)
        guessed_letter = string_check("Please enter your guess: ",
                                      f"is not a correct entry, try again. You still have"
                                      f" {lives_remaining} lives remaining.", 1).lower()
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
                    if chosen_word[i:i + 1] == guessed_letter:
                        game_progress[i:i + 1] = guessed_letter
            else:
                same_turn = False
                lives_remaining -= 1
                print(f"\nIncorrect, you have {lives_remaining} lives remaining.")
                already_guessed.add(guessed_letter)

        if lives_remaining == 0:
            game_end_message = "FAILURE Sorry, you didn't guess the word "
    print(f"\n\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-{game_end_message[0:7]}"
          f"-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n\n"
          f"{game_end_message[8:]}-> {chosen_word}")
    try_again_var = string_check("Would you like to play again? (Y/N): ",
                                 "is not a correct entry, try again.", 1, "ny").upper()
    if try_again_var == "N":
        play_again = False
