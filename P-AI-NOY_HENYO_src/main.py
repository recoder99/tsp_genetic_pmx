import os
import time
import matplotlib.pyplot as plt
from Guesser2 import Guesser


# GameMaster class

def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'time: {t2}')
        # return t2
        return result

    return wrapper


class GameMaster:
    def __init__(self, target_word):
        self.target_word = target_word
        self.target_len = len(self.target_word)

    # passes the length of the word provided by the user
    def passLen(self):
        self.target_len = len(self.target_word)
        return self.target_len

    # calculates the cost values of the provided word
    def calculateCost(self, guess_word):
        ALPHABET = "abcdefghijklmnopqrstuvwxyz "
        guess_cost = []
        x = 0

        # for loop that iterates through each character in a word to calculate each cost and append to guess_cost
        for i in range(self.target_len):
            char_cost = (ALPHABET.index(self.target_word[i].lower()) - ALPHABET.index(guess_word[i].lower())) ** 2
            guess_cost.append(char_cost)

        for i in guess_cost:
            x += i

        return x


# GuesserAgent
class BotGuesser:
    def __init__(self, word_len) -> None:
        self.word_len = word_len
        self.parent_1 = None
        self.parent_2 = None

    # generates initial population
    def generatePopulation(self):
        pass

    # crosses over the parents
    def cxFunc(self):
        pass

    # mutates the children
    def mutateChild(self):
        pass

    # returns the child that was conceived
    def returnChild(self):
        pass


# Main function (The Game Loop itself)
def mainFunc():
    os.system('cls')

    # Title Screen
    titleScreen()

    # Get input word
    input_word = input("Enter the magic word\t: ")
    gm = GameMaster(input_word)
    guesser = Guesser(len(input_word))

    guess_word = guesser.get_initial_guess()
    guesser.append_history(0, guess_word, gm.calculateCost(guess_word))
    # print(guess_word)
    # print('hold on, he\'s thinking')

    while gm.calculateCost(guess_word) != 0 and guesser.curr_generation < 5000:
        guess_word = guesser.eval_gene(guess_word, gm.calculateCost(guess_word))

    guesser.append_history(guesser.curr_generation + 1, guess_word, gm.calculateCost(guess_word))

    if gm.calculateCost(guess_word) == 0:
        print(f"Word \"{gm.target_word}\" is successfully guessed in {guesser.curr_generation + 1} guesses!!")
    else:
        print(f"Word \"{gm.target_word}\" was failed to be guessed!! Last guess was '{guess_word}' with cost {gm.calculateCost(guess_word)}")

    costs = [item[2] for item in guesser.guess_history]
    gen = list(range(1, len(costs) + 1))

    plt.plot(gen, costs, marker='o')
    plt.xlabel('Generation')
    plt.ylabel('Cost')
    plt.title('Cost vs Generation')
    plt.grid(True)
    plt.show()


def titleScreen():
    print(
        "\n    /$$$$$$$          /$$$$$$  /$$$$$$       /$$   /$$  /$$$$$$  /$$     /$$       /$$   /$$ /$$$$$$$$ /$$   /$$ /$$     /$$ /$$$$$$ ")
    print(
        "   | $$__  $$        /$$__  $$|_  $$_/      | $$$ | $$ /$$__  $$|  $$   /$$/      | $$  | $$| $$_____/| $$$ | $$|  $$   /$$//$$__  $$")
    print(
        "   | $$  \ $$       | $$  \ $$  | $$        | $$$$| $$| $$  \ $$ \  $$ /$$/       | $$  | $$| $$      | $$$$| $$ \  $$ /$$/| $$  \ $$")
    print(
        "   | $$$$$$$//$$$$$$| $$$$$$$$  | $$ /$$$$$$| $$ $$ $$| $$  | $$  \  $$$$/        | $$$$$$$$| $$$$$   | $$ $$ $$  \  $$$$/ | $$  | $$")
    print(
        "   | $$____/|______/| $$__  $$  | $$|______/| $$  $$$$| $$  | $$   \  $$/         | $$__  $$| $$__/   | $$  $$$$   \  $$/  | $$  | $$")
    print(
        "   | $$             | $$  | $$  | $$        | $$\  $$$| $$  | $$    | $$          | $$  | $$| $$      | $$\  $$$    | $$   | $$  | $$")
    print(
        "   | $$             | $$  | $$ /$$$$$$      | $$ \  $$|  $$$$$$/    | $$          | $$  | $$| $$$$$$$$| $$ \  $$    | $$   |  $$$$$$/")
    print(
        "   |__/             |__/  |__/|______/      |__/  \__/ \______/     |__/          |__/  |__/|________/|__/  \__/    |__/    \______/ \n\n")


if __name__ == "__main__":
    mainFunc()
