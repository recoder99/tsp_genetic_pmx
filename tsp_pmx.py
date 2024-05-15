import random
import math
import heapq
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

points = {
    'A': (8, 6),
    'B': (-4, 11),
    'C': (4, 11),
    'D': (2, 7),
    'E': (-2, 5),
    'F': (8, 3),
    'G': (-5, -8),
    'H': (3, 6),
    'I': (4, -3),
    'J': (8, 4)
}

def time_travel(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'Traversal time: {t2}')
        # return t2
        return result

    return wrapper


# calculate distance between 2 points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# calculate total distance of route
def total_distance(route):
    total = 0
    for i in range(len(route) - 1):
        if route[i] in points and route[i + 1] in points:
            total += distance(points[route[i]], points[route[i + 1]])
        else:
            raise ValueError("Invalid route key found.")
    return total


def generate_initial_population(population_size):
    population = []

    while len(population) < population_size:
        route = list(points.keys())
        random.shuffle(route)

        # check if route already in population
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

    swap(c1, c2, start, end)

    index1 = []
    index2 = []

    for i in range(len(c1)):
        if i in range(start, end + 1):
            continue
        for j in range(len(c1)):
            if (c1[j] == c1[i]) and (i != j):
                index1.append(i)

    for i in range(len(c2)):
        if i in range(start, end + 1):
            continue
        for j in range(len(c2)):
            if (c2[j] == c2[i]) and (i != j):
                index2.append(i)

    index2.reverse()
    # crossing
    for i in range(len(index1)):
        c1[index1[i]], c2[index2[i]] = c2[index2[i]], c1[index1[i]]

    return (c1, c2)
    print("\n")


def mutation(array):
    mutationList = [array]
    for idx in enumerate(array):
        x = random.randrange(idx[0], len(array))
        array[idx[0]], array[x] = array[x], array[idx[0]]
        mutationList.append(array)
    return mutationList


def get_fitness(array):
    fitness = 0
    for i in range(len(array) - 1):
        fitness += distance(points[array[i]], points[array[i + 1]])
    return fitness


def graph(set, points, fitness):

    fig, ax = plt.subplots()

    line, = ax.plot([], [], lw=2)
    generation_text = ax.text(0.01, 0.98, '', ha='left', va='top', transform=ax.transAxes, fontsize=8)
    fitness_text = ax.text(0.01, 0.95, '', ha='left', va='top', transform=ax.transAxes, fontsize=8)

    def init():
        plt.xlabel("x")
        plt.ylabel("y")

        plt.plot(ax.get_xlim(), [0, 0], 'k--')
        plt.plot([0, 0], ax.get_ylim(), 'k--')

        plt.xlim(-13, 13), plt.ylim(-13, 13)

        x = [points[i][0] for i in set[0]]
        y = [points[i][1] for i in set[0]]
        plt.plot(x, y, 'co')

        for i in range(len(x) - 1):
            plt.annotate(f"{i}", (x[i], y[i]), xytext=(x[i] + 0.1, y[i] + 0.1), fontsize=10)

        line.set_data([], [])
        return line,

    def animate(frame):
        x = [points[i][0] for i in set[frame] + [set[frame][0]]]
        y = [points[i][1] for i in set[frame] + [set[frame][0]]]

        generation_text.set_text(f"Generation: {frame}")
        fitness_text.set_text(f"Fitness: {fitness[frame]}")

        line.set_data(x, y)

        return line

    anim = FuncAnimation(fig, animate, frames=range(0, len(set), 20),
                        init_func=init, interval=1, repeat=False)

    plt.show()

@time_travel
def TSP(start, itr):
    parent1 = math.inf
    parent2 = math.inf
    fitness = []
    population = []
    all_generations = []
    all_fitness = []

    population = generate_initial_population(2)
    for i in population:
        i.remove(start)
        i.insert(0, start)
        i.append(start)

    # get fitness of each population
    for i in range(len(population)):
        heapq.heappush(fitness, (get_fitness(population[i]), i))

    temp = heapq.heappop(fitness)
    parent1 = (temp[0], population[temp[1]])

    for m in range(itr):

        while True:
            # if len(fitness) > 0:
            temp = generate_initial_population(1)[0]
            temp.remove(start)
            temp.insert(0, start)
            temp.append(start)

            parent2 = (get_fitness(temp), temp)

            childs = crossover(parent1[1][1:len(parent1[1]) - 1], parent2[1][1:len(parent2[1]) - 1], 2, 6)

            mutations = mutation(childs[0]) + mutation(childs[1])
            random.shuffle(mutations)

            temp_child = (math.inf, 0)

            while (temp_child[0] >= parent1[0] + 2) or (temp_child[0] >= parent2[0] + 2):
                if len(mutations) <= 0:
                    break

                temp = mutations.pop()
                # apply start and end position
                temp.insert(0, start)
                temp.append(start)

                temp_child = (get_fitness(temp), temp)

            if len(mutations) <= 0:
                print(f"Gen #{m} current lowest path:{parent1[0]} ")
                all_generations.append(parent1[1])
                all_fitness.append(round(parent1[0], 3))
                break
            else:
                print(f"Gen #{m} current lowest path:{temp_child[0]} ")
                all_generations.append(temp_child[1])
                all_fitness.append(round(temp_child[0], 3))
                parent1 = temp_child
                break

    return all_generations, all_fitness


gene_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
array1 = [2, 1, 3, 5, 4]
array2 = [2, 3, 4, 1, 5]

testGene = ['A', 'B', 'C', 'D']
testGene2 = ['A', 'D', 'C', 'B']

# start = int(input("Enter the starting index: "))
# end = int(input("Enter the ending index: "))

# crossover(testGene, testGene2, 2, 3)
# mutation(testGene)
# mutation(testGene2)

# print(get_fitness(testGene))

#test
ag, af = TSP('A', 10000)
graph(ag, points, af)
