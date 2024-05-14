import random
import math
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

def generate_initial_population():
    nodes = list(points.keys())
    permutations = itertools.permutations(nodes)
    population = [list(p) for p in permutations ]
    return population

population = generate_initial_population()


route_index = 200 
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

    print(c1)
    print(c2)
    print("\n")

def mutation(array):
    for idx in enumerate(array):
        x = random.randrange(idx[0], len(array))
        array[idx[0]], array[x] = array[x], array[idx[0]]
        print(array)
 
array1 = [2, 1, 3, 5, 4]
array2 = [2, 3 ,4, 1, 5]
 
# start = int(input("Enter the starting index: "))
# end = int(input("Enter the ending index: "))
 
crossover(array1, array2, 2, 3)
mutation(array1)
mutation(array2)

