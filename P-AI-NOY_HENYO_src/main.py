# GameMaster class
class GameMaster:
    def __init__(self, target_word) -> None:
        self.target_word = target_word
    
    # passes the length of the word provided by the user
    def passLen(self):
        return len(self.target_word)

    # calculates the cost values of the provided word
    def calculateCost(self):
        pass

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
    # Get input word
    input_word = input("Enter the magic word\t: ")
    gm = GameMaster(input_word)
    guesser = BotGuesser(gm.passLen())

    is_guessing = True

    while is_guessing:
        print(guesser.word_len)
        break

if __name__ == "__main__":
    mainFunc()