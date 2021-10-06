import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("lets not die! :)")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("please gok een letter of woord: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("je hebt all is die letter gegokked", guess)
            elif guess not in word:
                print(guess, "is niet in het.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("goed gedaan,", guess, "is in het woord!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("je hebt het woord al geraden", guess)
            elif guess != word:
                print(guess, "is niet het woord.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Niet mogelijke gok.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("gefeliciteerd, je hebt het woord geraden! je hebt gewonnen!")
    else:
        print("Sorry, je hebt geen pogingen meer. het woord was " + word + ". Miss de volgende keer!")


def display_hangman(tries):
    stages = [  # laatste state
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # hoofd, torso, both arms, both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # hoofd, torso, both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # hoofd, torso, 1 arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # hoofd, torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # hoofd
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # leeg
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("opnieuw spelen? (J/N) ").upper() == "J":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()