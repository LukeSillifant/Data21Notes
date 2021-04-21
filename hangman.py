import random
from lists import word_list
name_check = True
play_again = True

while name_check:
    name = input("Please enter your name: ")
    if name.isalpha():
        print("Success! Welcome to hangman!")
        name_check = False
    else:
        print(f"\"{name}\" is not a valid answer, try again")

while play_again:

    lives_remaining = 8
    chosen_word = word_list[int(random.uniform(0, len(word_list)))].lower()
    game_progress = ["_"] * len(chosen_word)
    already_guessed_wrong = set()
    already_guessed_right = set()
    print(chosen_word)
    print(*game_progress, sep='')
    game_progress_display = "".join(str(x) for x in game_progress)
    game_end_message = "Congratulations"

    while game_progress_display != chosen_word and lives_remaining > 0:

        guessed_letter = input("Enter your letter: ")
        same_turn = True

        while same_turn:
            if guessed_letter in already_guessed_right or guessed_letter in already_guessed_wrong:
                print(f"You've already guessed this, you still have {lives_remaining} lives remaining.")
                break
            elif guessed_letter in chosen_word:
                same_turn = False
                print(f"Correct, you still have {lives_remaining} lives remaining.")
                already_guessed_right.add(guessed_letter)
                for i in range(len(game_progress)):
                    if chosen_word[i:i+1] == guessed_letter:
                        game_progress[i:i+1] = guessed_letter
            else:
                same_turn = False
                lives_remaining -= 1
                print(f"Incorrect, you have {lives_remaining} lives remaining.")
                already_guessed_wrong.add(guessed_letter)

        game_progress_display = "".join(str(x) for x in game_progress)
        print(*game_progress, sep='')
        print(already_guessed_right)
        print(already_guessed_wrong)

        if lives_remaining == 0:
            game_end_message = "Sorry"

    try_again_var = input(f"{game_end_message}, try again? (Y/N): ")
    if try_again_var == "N":
        play_again = False
