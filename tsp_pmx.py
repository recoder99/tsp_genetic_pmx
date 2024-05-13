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

def crossover(p1, p2):
    c1 = p1
    c2 = p2

    swap(c1, c2, 1,2)

    index1 = []
    index2 = []

    for i in range(len(c1)):
        for j in range(len(c1)):
            if (c1[j] == c1[i]) and (i != j) and ():
                index1.append(j)

    for i in range(len(c2)):
        for j in range(len(c2)):
            if (c2[j] == c2[i]) and (i != j):
                index2.append(j)

    index2 = index2.reverse()
    #crossing
    for i in range(len(index1)):
        c1[index1[i]], c2[index1[i]] = c2[index1[i]], c1[index1[i]]


    print(c1)
    print(c2)

 
array1 = [2, 3, 5, 1]
array2 = [5, 4 ,2, 1]
 
# start = int(input("Enter the starting index: "))
# end = int(input("Enter the ending index: "))
 
crossover(array1, array2)
 

