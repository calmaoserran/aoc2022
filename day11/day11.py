#!/usr/bin/python3

import sys
from itertools import groupby
from math import prod
import time

class Monkey:
    """
    Starting items lists your worry level for each item the monkey is currently holding in the order they will be inspected.
    Operation is done to human worry level after monkey inspects an item.
    Test shows how the monkey uses your worry level to decide where to throw an item next.
    """
    modulo = 1
    def __init__(self,unparsed_list,modifier):
        self.name = unparsed_list[0][-2]
        self.inventory = list(map(int,unparsed_list[1].replace(' ','').split(':')[1].split(',')))
        self.operation_str = unparsed_list[2].split(' ')[-2:]
        self.test = [int(unparsed_list[3].split(' ')[-1]),int(unparsed_list[4][-1]),int(unparsed_list[5][-1])]
        self.business = 0
        self.modifier = modifier
        if Monkey.modulo % self.test[0] != 0:
            Monkey.modulo *= self.test[0]
        

    def __repr__(self) :
        return (f'Monkey {self.name} | Inv: {self.inventory} | Operation: {self.operation_str} | Test: {self.test}')

    def operation(self,item):
        outcome = 0
        if self.operation_str[1] == 'old':
            outcome = item
        else:
            outcome = int(self.operation_str[1])
        if self.operation_str[0] == '+':
            outcome += item
        else: # There are only + and *
            outcome *= item
        return outcome

    def inspect_item(self):
        """
        Inspect items and performs operation over it to change the worry level.
        Updates business level each iteration by 1
        """
        #self.inventory[0] = self.modifier(self.inventory[0])
        self.inventory[0] = self.modifier((self.operation(self.inventory[0])))
        self.business +=1

    def test_and_throw(self):
        # if item is divisible by test[0]
        # if true send to test[1]
        # if false send to test[2]
        if self.inventory[0] % self.test[0] == 0:
            monkeys[self.test[1]].inventory.append(self.inventory.pop(0))
        else:
            monkeys[self.test[2]].inventory.append(self.inventory.pop(0))

    def turn(self):
        for item in range(len(self.inventory)):
            self.inspect_item()
            self.test_and_throw()

def challenge(input_file,rounds) -> int:
    for r in range(rounds):
        for monkey in monkeys:
            monkey.turn()
    return(prod(sorted([m.business for m in monkeys])[-2:]))
    
  
if __name__ == "__main__":
    # Read file into a list of lists using blank lines as separators. Each list contains all the monkey specs
    file_name = 'input'
    input_file = [list(group) for k, group in groupby([line.rstrip() for line in open(file_name)],bool) if k]
    modifier = lambda x: x // 3
    monkeys = [Monkey(a,modifier) for a in input_file]
    start_time = time.time()
    print(f'Challenge 1 solution: {challenge(input_file,20)}')
    modifier = lambda x: x % Monkey.modulo
    monkeys = [Monkey(a,modifier) for a in input_file]
    print(f'Challenge 2 solution: {challenge(input_file,10000)}')
    print(f'Completed in {(time.time() - start_time)} seconds')
