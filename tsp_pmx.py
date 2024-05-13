# mp = {{0, 10, 15, 20},
#      {10, 0, 35, 25},
#      {15, 35, 0, 30},
#      {20, 25, 30, 0}
#     }

def swap(arr1, arr2, start, end):
    for i in range(start, end + 1):
        arr1[i], arr2[i] = arr2[i], arr1[i]

def mutate(p1, p2):
    c1 = p1
    c2 = p2

    swap(c1, c2, 1,3)

    print(c1)
    print(c2)

    # for i in range(len(c1)):
    #     for j in range(len(c2)):
    #         c1[]


 
 
array1 = [1, 2, 3, 4, 5]
array2 = [6, 7, 8, 9, 10]
 
# start = int(input("Enter the starting index: "))
# end = int(input("Enter the ending index: "))
 
mutate(array1, array2)
 

