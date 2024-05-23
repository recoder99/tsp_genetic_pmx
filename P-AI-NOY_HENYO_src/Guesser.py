import math
import random
from heapq import *


class Guesser:
    mutation_list = []

    heap = []

    parent1 = (math.inf, "")
    parent2 = (math.inf, "")

    num = 0

    def __init__(self, word_len) -> None:
        self.num = word_len
        self.curr_generation = 0
        self.guess_history = []
        x = self.gen_population(self.num, 10)
        for i in x:
            self.mutation_list.append([*i])

    def gen_population(self, num, itr):
        templist = []
        temp = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(itr):
            for i in range(num):
                temp += alphabet[random.randrange(0, len(alphabet))]
            templist.append(temp)
            temp = ""

        return templist

    def swap(self, arr1, arr2, start, end):

        for i in range(start, end + 1):
            arr1[i], arr2[i] = arr2[i], arr1[i]

    def crossover(self, p1, p2, start, end):
        c1 = p1
        c2 = p2

        self.swap(c1, c2, start, end)

        return (c1, c2)

    # def mutate(self, array):
    #     mutationList = [array]
    #     for idx in enumerate(array):
    #         for i in range(3):
    #             x = random.randrange(idx[0], len(array))
    #             array[idx[0]], array[x] = array[x], array[idx[0]]
    #             mutationList.append(array)
    #     return mutationList

    def mutate(self, array: list, start, end):
        x = []
        for i in range(20):
            temp = array
            random.shuffle(temp[start:end])
            x.append(temp)
        return x

    def get_initial_guess(self):
        init_guess = "".join(self.mutation_list.pop())
        return init_guess

    def append_history(self, generation, guess, cost):
        self.guess_history.append([generation, guess, cost])

    def eval_gene(self, text, cost):
        heappush(self.heap, (cost, text))
        # if mutations is not depleted
        if len(self.mutation_list) > 0:
            pops = "".join(self.mutation_list.pop())
            return pops
        else:  # if mutations are depleted
            temp = heappop(self.heap)
            if temp[0] < self.parent2[0] and temp[0] < self.parent1[0]:  # if there is a child better than original parent
                self.curr_generation += 1
                # set the child with the lowest cost as parent1
                self.parent1 = temp
                # set the child with the second lowest cost as parent2
                self.parent2 = heappop(self.heap)

                temp = [*self.parent1[1]]
                temp2 = [*self.parent2[1]]

                child = self.crossover(temp, temp2, math.floor(len(temp) * 0.30), math.floor(len(temp) * 0.60))
                self.mutation_list = self.mutate(child[0], math.floor(len(temp) * 0.30),
                                                 math.floor(len(temp) * 0.60)) + self.mutate(child[1], math.floor(
                    len(temp) * 0.30), math.floor(len(temp) * 0.60)) + [child[0]] + [child[1]]
                print(f"Generation {self.curr_generation}: {self.parent1[1]} Cost: {self.parent1[0]}")
                self.append_history(self.curr_generation, self.parent1[1], self.parent1[0])
            else:  # if there are no child better than original parent
                temp = self.gen_population(self.num, 1)
                self.parent2 = (math.inf, temp[0])

                temp = [*self.parent1[1]]
                temp2 = [*self.parent2[1]]

                child = self.crossover(temp, temp2, math.floor(len(temp) * 0.30), math.floor(len(temp) * 0.60))
                self.mutation_list = self.mutate(child[0], math.floor(len(temp) * 0.30),
                                                 math.floor(len(temp) * 0.60)) + self.mutate(child[1], math.floor(
                    len(temp) * 0.30), math.floor(len(temp) * 0.60)) + [child[0]] + [child[1]]

            return "".join(self.mutation_list.pop())

    # get parent with better cost
