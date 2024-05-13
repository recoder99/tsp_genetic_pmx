import math

# mp = {{0, 10, 15, 20},
#      {10, 0, 35, 25},
#      {15, 35, 0, 30},
#      {20, 25, 30, 0}
#     }

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
 

