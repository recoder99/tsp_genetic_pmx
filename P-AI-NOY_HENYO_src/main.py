import os

# GameMaster class
class GameMaster:
    def __init__(self, target_word) -> None:
        self.target_word = target_word
        self.target_len = None
    
    # passes the length of the word provided by the user
    def passLen(self):
        self.target_len = len(self.target_word)
        return self.target_len

    # calculates the cost values of the provided word
    def calculateCost(self, guess_word):
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        guess_cost = []

        # for loop that iterates through each character in a word to calculate each cost
        for i in range(self.target_len):
            char_cost = (ALPHABET.index(self.target_word[i].lower()) - ALPHABET.index(guess_word[i].lower()))**2
            guess_cost.append(char_cost)

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
    guesser = BotGuesser(gm.passLen())

    is_guessing = True

    while is_guessing:
        print(guesser.word_len)
        break

def titleScreen():
    print("\n    /$$$$$$$          /$$$$$$  /$$$$$$       /$$   /$$  /$$$$$$  /$$     /$$       /$$   /$$ /$$$$$$$$ /$$   /$$ /$$     /$$ /$$$$$$ ")
    print("   | $$__  $$        /$$__  $$|_  $$_/      | $$$ | $$ /$$__  $$|  $$   /$$/      | $$  | $$| $$_____/| $$$ | $$|  $$   /$$//$$__  $$")
    print("   | $$  \ $$       | $$  \ $$  | $$        | $$$$| $$| $$  \ $$ \  $$ /$$/       | $$  | $$| $$      | $$$$| $$ \  $$ /$$/| $$  \ $$")
    print("   | $$$$$$$//$$$$$$| $$$$$$$$  | $$ /$$$$$$| $$ $$ $$| $$  | $$  \  $$$$/        | $$$$$$$$| $$$$$   | $$ $$ $$  \  $$$$/ | $$  | $$")
    print("   | $$____/|______/| $$__  $$  | $$|______/| $$  $$$$| $$  | $$   \  $$/         | $$__  $$| $$__/   | $$  $$$$   \  $$/  | $$  | $$")
    print("   | $$             | $$  | $$  | $$        | $$\  $$$| $$  | $$    | $$          | $$  | $$| $$      | $$\  $$$    | $$   | $$  | $$")
    print("   | $$             | $$  | $$ /$$$$$$      | $$ \  $$|  $$$$$$/    | $$          | $$  | $$| $$$$$$$$| $$ \  $$    | $$   |  $$$$$$/")
    print("   |__/             |__/  |__/|______/      |__/  \__/ \______/     |__/          |__/  |__/|________/|__/  \__/    |__/    \______/ \n\n")
    
if __name__ == "__main__":
    mainFunc()