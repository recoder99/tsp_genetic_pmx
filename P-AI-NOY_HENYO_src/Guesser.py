import math
import random
import numpy as np
from heapq import *


class Guesser:
    mutation_list = []
    mutate_history = []

    heap = []

    parent1 = (math.inf, "")
    parent2 = (math.inf, "")

    num = 0
    swap_start = 0.40
    swap_end = 0.80

    crossover_start = 0.3
    crossover_end = 0.70

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

    def mutate(self, array: list, start, end, mode='a'):
        x = []
        current_mutate = []
        temp = 0

        for i in range(30):
            # temp = array
            # random.shuffle(temp[start:end])
            # x.append(temp)
            temp = list(array)
            for i in range(start,end):
                val = random.randrange(i, end)
                temp[i], temp[val] = temp[val], temp[i]

            joins = "".join(temp)   # join char arrays into one string
            x.append(temp)
            current_mutate.append(joins)

        if mode == 'p':
            new_mutates = self.discard_old_mutation_python(current_mutate)
            print(new_mutates)
            return new_mutates
        elif mode == 'n':
            new_mutates = self.discard_old_mutation_numpy(current_mutate)
            return new_mutates
        else:
            return x

    def discard_old_mutation_numpy(self, array: list):
        unique_array = set(array)   # remove duplicates
        np_arr = np.array(list(unique_array))   # convert to np array

        # print('hist', self.mutate_history)
        np_mutation_hist = np.array(self.mutate_history)     # convert history to np array

        unique = np_arr[~np.in1d(np_arr, np_mutation_hist)]     # remove from np_arr members found in history

        self.mutate_history.extend(unique.tolist())     # convert unique to list and append to history

        str_to_char = list(map(list, unique.tolist()))   # convert to 2d list of chars

        return str_to_char

    def discard_old_mutation_python(self, array: list):
        no_duplicate = list(set(array))
        unique = [x for x in no_duplicate if x not in self.mutate_history]

        self.mutate_history.extend(unique)

        str_to_char = list(map(list, unique))  # convert to 2d list of chars

        return str_to_char

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
            if temp[0] < self.parent2[0]:  # if the elite child better than parent 2

                if temp[0] < self.parent1[0]: #if the elite child is better than parent 1
                    self.parent1 = temp
                    self.parent2 = heappop(self.heap) # get the second elite child as parent2

                else:
                    self.parent2 = temp # replace the parent2 with elite child
                # # set the child with the lowest cost as parent1
                temp = [*self.parent1[1]]
                temp2 = [*self.parent2[1]]

                child = self.crossover(temp, temp2, math.floor(len(temp) * self.crossover_start), math.floor(len(temp) * self.crossover_end))
                self.mutation_list = self.mutate(child[0], math.floor(len(temp) * self.swap_start),
                                                 math.floor(len(temp) * self.swap_end)) + self.mutate(child[1], math.floor(
                    len(temp) * self.swap_start), math.floor(len(temp) * self.swap_end)) + [child[0]] + [child[1]]

                self.curr_generation += 1
                # print(f"Generation {self.curr_generation}: {self.parent1[1]} Cost: {self.parent1[0]}")
                self.append_history(self.curr_generation, self.parent1[1], self.parent1[0])
            else:  # if there are no child better than original parent
                temp = self.gen_population(self.num, 1)
                self.parent2 = (math.inf, temp[0])

                temp = [*self.parent1[1]]
                temp2 = [*self.parent2[1]]

                child = self.crossover(temp, temp2, math.floor(len(temp) * self.crossover_start), math.floor(len(temp) * self.crossover_end))
                self.mutation_list = self.mutate(child[0], math.floor(len(temp) * self.swap_start),
                                                 math.floor(len(temp) * self.swap_end)) + self.mutate(child[1], math.floor(
                    len(temp) * self.swap_start), math.floor(len(temp) * self.swap_end)) + [child[0]] + [child[1]]

            return "".join(self.mutation_list.pop())

    # get parent with better cost