import math
import random
import matplotlib.pyplot as plt 


global MAX_COL, MAX_ROW, EMERGENCY_MAP
MAX_COL = 10
MAX_ROW = 10
EMERGENCY_MAP = [   
                    [5, 2, 4, 8, 9, 0, 3, 3, 8, 7],
                    [5, 5, 3, 4, 4, 6, 4, 1, 9, 1],
                    [4, 1, 2, 1, 3, 8, 7, 8, 9, 1],
                    [1, 7, 1, 6, 9, 3, 1, 9, 6, 9],
                    [4, 7, 4, 9, 9, 8, 6, 5, 4, 2],
                    [7, 5, 8, 2, 5, 2, 3, 9, 8, 2],
                    [1, 4, 0, 6, 8, 4, 0, 1, 2, 1],
                    [1, 5, 2, 1, 2, 8, 3, 3, 6, 2],
                    [4, 5, 9, 6, 3, 9, 7, 6, 5, 10],
                    [0, 6, 2, 8, 7, 1, 2, 1, 5, 3] 
                ]

class Population:
    def __init__(self, population_size: int) -> None:
        self.population_size = population_size
        self.population = []

        itr = 0
        instances = 0
        while itr < self.population_size:
            x_value = random.randint(0, MAX_ROW - 1)
            y_value = random.randint(0, MAX_COL - 1)

            for i in self.population:
                if [x_value, y_value] == [i.x_value, i.y_value]:
                    instances += 1
            
            if instances > 0:
                instances = 0

            else:
                self.population.append(Coordinate(x_value, y_value, EMERGENCY_MAP))
                itr += 1

    # Find the initial parents for the initial generation (2 most elite)
    def initParents(self, population):
        temp_population = population.population

        best_unit1, temp_population = self.findInitParents(temp_population)
        best_unit2, temp_population = self.findInitParents(temp_population)
            
        return best_unit1, best_unit2

    # Find the specific parent for the initial generation
    def findInitParents(self, population):
        temp_population = population
        best_unit = temp_population[0]

        for unit in temp_population:
            if unit.cost_val > best_unit.cost_val:
                best_unit = unit
        
        temp_population.remove(best_unit)
        return best_unit, temp_population

class Coordinate:
    def __init__(self, x_value: int, y_value: int, matrix) -> None:
        self.x_value = x_value
        self.y_value = y_value
        self.matrix = matrix
        self.cost_val = self.costValue()

    # Function to get the cost value of the Coordinate
    def costValue(self):
        fitness = 0
        for y in range(MAX_COL):
            for x in range(MAX_ROW):
                fitness += self.matrix[y][x] * (math.sqrt(((x - self.x_value)**2) + ((y - self.y_value)**2)))

        return fitness
        
def mainFunc():
    population = Population(10)
    init_parent1, init_parent2 = population.initParents(population)

    gen = 1
    
    while gen < 501:
        # crossover
        # mutation
        # print the genes
        pass

if __name__ == "__main__":
    mainFunc()