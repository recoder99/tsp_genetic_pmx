import os
import random
import string
import matplotlib.pyplot as plt

# Class for the GameMaster Agent 
class GameMaster:
    def __init__(self, target_word):
        self.target_word = target_word
        self.cost_history = []

    # Calculates the cost of the given word
    def get_cost(self, word):
        cost = sum((ord(a.lower()) - ord(b.lower())) ** 2 for a, b in zip(word, self.target_word))
        return cost

    # Records the cost of the best child per generation
    def record_cost(self, cost):
        self.cost_history.append(cost)

    # Plots the cost after execution
    def plot_cost(self):
        plt.plot(self.cost_history)
        plt.xlabel('Generation')
        plt.ylabel('Cost')
        plt.title('Cost Function Over Generations')
        plt.show()

# The class for the Guesser Agent
class Guesser:
    def __init__(self, target_length, population_size=20, crossover_prob=0.7, mutation_prob=0.01):
        self.target_length = target_length
        self.population_size = population_size
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        self.population = self._initialize_population()
        self.best_guess = None
        self.best_cost = float('inf')

    # Create an initial population through randomization
    def _initialize_population(self):
        return [''.join(random.choice(string.ascii_lowercase + " ") for _ in range(self.target_length)) for _ in range(self.population_size)]

    # Select parents through tournament selection
    def _select_parents(self):
        tournament_size = 5
        tournament = random.sample(list(zip(self.population, self.costs)), tournament_size)
        parent1 = min(tournament, key=lambda x: x[1])[0]
        parent2 = min(random.sample(list(zip(self.population, self.costs)), tournament_size), key=lambda x: x[1])[0]
        return parent1, parent2

    # Single point crossover
    def _crossover(self, parent1, parent2):
        if random.random() < self.crossover_prob:
            point = random.randint(1, self.target_length - 1)
            child1 = parent1[:point] + parent2[point:]
            child2 = parent2[:point] + parent1[point:]
            return child1, child2
        else:
            return parent1, parent2

    # Mutate a specific letter in the word
    def _mutate(self, word):
        word = list(word)
        for i in range(self.target_length):
            if random.random() < self.mutation_prob:
                word[i] = random.choice(string.ascii_lowercase + " ")
        return ''.join(word)

    # Generate a new population for the new generation
    def generate_new_population(self):
        new_population = []
        for _ in range(self.population_size // 2):
            parent1, parent2 = self._select_parents()
            child1, child2 = self._crossover(parent1, parent2)
            new_population.append(self._mutate(child1))
            new_population.append(self._mutate(child2))
        self.population = new_population

    # Get the lowest cost in the population and compare the lowest guess in history vs the lowest guess of current generation
    def evaluate_population(self, get_cost):
        self.costs = [get_cost(word) for word in self.population]
        min_cost = min(self.costs)
        if min_cost < self.best_cost:
            self.best_cost = min_cost
            self.best_guess = self.population[self.costs.index(min_cost)]

    # Check if the current cost is the best cost
    def get_optimize(self):
        return self.best_cost == 0

# Main Game Loop+
def run_game(target_word):
    game_master = GameMaster(target_word)
    guesser = Guesser(target_length=len(target_word))

    generations = 5000

    for generation in range(generations):
        guesser.evaluate_population(game_master.get_cost)
        guesser.generate_new_population()
        game_master.record_cost(guesser.best_cost)

        print(f'Generation {generation}: Best Guess = {guesser.best_guess}, Cost = {guesser.best_cost}')
        if guesser.get_optimize():
            break
    
    print("Voila! The word", guesser.best_guess, "was found! Congratulations!")

    game_master.plot_cost()

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
    os.system('cls')
    titleScreen()
    target = input("Enter the target word: ")
    run_game(target)