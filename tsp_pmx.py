import random
import math
import heapq
import itertools

points = {
    'A': (8, 6),
    'B': (-4, 11),
    'C': (4, 11),
    'D': (2, 7),
    'E': (2, 5),
    'F': (8, 3),
    'G': (5, 2),
    'H': (3, 6),
    'I': (4, 3),
    'J': (8, 4)
}

# calculate distance between 2 points 
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# calculate total distance of route
def total_distance(route):
    total = 0
    for i in range(len(route) - 1):
        if route[i] in points and route[i+1] in points:
            total += distance(points[route[i]], points[route[i+1]])
        else:
            raise ValueError("Invalid route key found.")
    return total

def generate_initial_population(population_size):
    population = []

    while len(population) < population_size:
        route = list(points.keys())
        random.shuffle(route)
        
        #check if route already in population
        if route not in population:
            population.append(route)

    return population


route_index = 5
population = generate_initial_population(10)
selected_route = population[route_index]

print("Selected Route:", selected_route)
print("Total Distance of Selected Route:", total_distance(selected_route))

def swap(arr1, arr2, start, end):
    for i in range(start, end + 1):
        arr1[i], arr2[i] = arr2[i], arr1[i]

def crossover(p1, p2, start, end):
    c1 = p1
    c2 = p2

    swap(c1, c2, start,end)

    index1 = []
    index2 = []
                

    for i in range(len(c1)):
        if i in range(start, end+1):
            continue
        for j in range(len(c1)):
            if (c1[j] == c1[i]) and (i != j):
                index1.append(i)

    for i in range(len(c2)):
        if i in range(start, end+1):
            continue
        for j in range(len(c2)):
            if (c2[j] == c2[i]) and (i != j):
                index2.append(i)

    index2.reverse()
    #crossing
    for i in range(len(index1)):
        c1[index1[i]], c2[index2[i]] = c2[index2[i]], c1[index1[i]]

    return (c1,c2)
    print("\n")

def mutation(array):
    mutation = []
    mutation.append(array)
    for idx in enumerate(array):
        x = random.randrange(idx[0], len(array))
        array[idx[0]], array[x] = array[x], array[idx[0]]
        mutation.append(array)
    return mutation

def get_fitness(array):
    fitness = 0
    for i in range(len(array)-1):
        fitness += distance(points[array[i]], points[array[i+1]])
    return fitness


def TSP(start, itr):

    parent1 = math.inf
    parent2 = math.inf

    for m in range(itr):

        population = generate_initial_population(10)
        fitness = []
        if len(fitness) <= 0:
            for i in population:
                i.remove(start)
                i.insert(0, start)
                i.append(start)
            #get fitness of each population
            
            for i in range(len(population)):
                heapq.heappush(fitness, (get_fitness(population[i]), i))

        temp = heapq.heappop(fitness)
        parent1 = (temp[0], population[temp[1]])

        while(True):
            #if len(fitness) > 0:
            temp = heapq.heappop(fitness)
            parent2 = (temp[0], population[temp[1]])


            childs = crossover(parent1[1][1:len(parent1[1]) - 1], parent2[1][1:len(parent2[1]) -1], 2,6)

            mutations = mutation(childs[0]) + mutation(childs[1])
            random.shuffle(mutations)
            
            temp_child = (math.inf, 0)

            while (temp_child[0] >= parent1[0] - 2)  and (temp_child[0] >= parent2[0] - 2):
                if len(mutations) <= 0:
                    break

                temp = mutations.pop()
                #apply start and end position
                temp.insert(0, start)
                temp.append(start)

                temp_child = (get_fitness(temp), temp)
            
            if len(mutations) <= 0:
                break
            else:
                print(f"Gen #{m} current lowest path:{temp_child[0]} ")
                parent1 = temp_child
                break

    


        

    




    


gene_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
array1 = [2, 1, 3, 5, 4]
array2 = [2, 3 ,4, 1, 5]

testGene = ['A', 'B', 'C', 'D']
testGene2 = ['A', 'D', 'C', 'B']
 
# start = int(input("Enter the starting index: "))
# end = int(input("Enter the ending index: "))
 
# crossover(testGene, testGene2, 2, 3)
# mutation(testGene)
# mutation(testGene2)

# print(get_fitness(testGene))

TSP('A', 5000)
