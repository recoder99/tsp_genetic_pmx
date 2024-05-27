import random 
import matplotlib.pyplot as plt 
from math import sqrt 

#specifications 

grid_size = 10 
population_size = 20 
max_generations = 5000
crossover_rate = 0.8 
mutation_rate = 0.2 
convergence_threshold = 1e-6
max_no_improvement_generations = 100

#fitness

def fitness(population, emergency_frequency): 

    #calculate center of each cells
    grid_coordinates = []

    for i in range(grid_size): 
        for j in range(grid_size):
            grid_coordinates.append((i + 0.5, j + 0.5))

    #distance between each grid center and each proposed coords for ERU
    cost =[]       

    for ind in population: 
        total_cost = 0

        for i in range(grid_size): 
            for j in range(grid_size): 
                x,y = grid_coordinates[i * grid_size + j]
                total_cost += emergency_frequency [i][j] * sqrt((x - ind[0]) **2 + (y - ind[1]) ** 2)
        
        cost.append(total_cost)
    
    return cost

# generate initial population 

def generate_population(size, grid_size): 

    population = []

    for _ in range(size):
        x = random.uniform(0, grid_size)
        y = random.uniform(0, grid_size)

        population.append([x,y])
    
    return population 

#crossover operator (single-point crossover)
def crossover(parent1, parent2): 

    if random.random() < crossover_rate: 
        crossover_point = random.randint(0,1)
        offspring = parent1[:crossover_point] + parent2[crossover_point:]

        return offspring 
    
    return parent1

#mutation operator 

def mutate(individual, mutation_rate, grid_size): 

    if random.random() < mutation_rate: 
        mutation_amount = [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)]
        x_new = min(max(individual[0] + mutation_amount[0], 0), grid_size)
        y_new = min(max(individual[1] + mutation_amount[1], 0), grid_size)

        return [x_new, y_new]
    return individual

#genetic algo 

def genetic_algorithm(): 

    #generation of random emergency frequency grid
    emergency_frequency = []

    for _ in range(grid_size): 
        row = []
        for _ in range(grid_size):
            row.append(random.randint(0,10))
        emergency_frequency.append(row)

    population = generate_population(population_size, grid_size)
    generations_list = []
    coordinates_list = []
    cost_values_list = []
    response_times_list = []

    best_fitness = float('inf')
    no_improvement_generations = 0

    for generation in range(max_generations): 

        fitness_values = fitness(population, emergency_frequency)
        sorted_indices = sorted(range(len(fitness_values)), key=lambda k: fitness_values[k])
        population = [population[i] for i in sorted_indices]

        # select only the top half of new population
        next_generation = population[:population_size // 2]

        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(population[:population_size //2], 2)
            offspring = mutate(crossover(parent1, parent2), mutation_rate,grid_size)
            next_generation.append(offspring)
        
        population = next_generation

        current_best_fitness = fitness_values[sorted_indices[0]]
        best_individual = population[0]
        best_response_time = 1.7 + 3.4 * sqrt((best_individual[0]- grid_size /2) ** 2 + (best_individual[1] - grid_size/2) ** 2)

        #check for convergence 

        if abs(current_best_fitness - best_fitness) < convergence_threshold: 
            no_improvement_generations += 1
        
        else:
            no_improvement_generations = 0
            best_fitness = current_best_fitness

        if no_improvement_generations >= max_no_improvement_generations: 
            print("Converged after {} generations".format(generation + 1))
            break

        #store results 
        generations_list.append(generation + 1)
        coordinates_list.append([round(best_individual[0]), round(best_individual[1])])
        cost_values_list.append(current_best_fitness)
        response_times_list.append(best_response_time)

        print(f"Generation {generation + 1}, Best Coordinate: {coordinates_list[-1]}, Cost Value: {current_best_fitness:.2f}, Response Time {best_response_time:.2f} minutes.")

if __name__ == "__main__":
    genetic_algorithm()



