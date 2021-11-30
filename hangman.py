import random
import string

print("H A N G M A N")
while True:
    print("Type \"play\" to play the game, \"exit\" to quit:")

    answer = input()
    if answer == "exit":
        exit(0)
    elif answer != "play":
        continue

    answers = ("python", "java", "kotlin", "javascript")
    right_answer = answers[random.randint(0, len(answers) - 1)]
    right_answer_set = set(right_answer)

    called_letters = set()
    right_letters = set()

    lives = 8

    while True:
        print()
        for c in right_answer:
            if c in called_letters:
                print(c, end="")
            else:
                print("-", end="")
        print()
        letter = input("Input a letter: ")

        if len(letter) > 1:
            print("You should input a single letter")
            continue

        if letter not in string.ascii_lowercase:
            print("Please enter a lowercase English letter")
            continue

        if letter in called_letters:
            print("You've already guessed this letter")
        elif letter not in right_answer:
            print("That letter doesn't appear in the word")
            lives -= 1
        else:
            right_letters.add(letter)

        if lives == 0:
            print("You lost!\n")
            break

        called_letters.add(letter)

        if right_answer_set == right_letters:
            print(f"You guessed the word {right_answer}!")
            print("You survived!\n")
            break

