#!/usr/bin/python2.7

#A Monty Hall simulator.

from random import randint, choice

def sim():
    
    doors = {1, 2, 3}
    car = randint(1, 3)
    mychoice = randint(1, 3)
    
    montychoice = choice(list(doors - {car} - {mychoice}))
    newchoice = list(doors - {montychoice} - {mychoice})[0]
    
    if newchoice == car:
        #print "You won!"
        return 1
    else:
        #print "You lost!"
        return 0

n, total, stick = 1000, 0, 0

for i in range(1, n + 1):
    result = sim()
    total += result
    stick += abs(result - 1)
    print i, 100 * total / float(i), 100 * stick / float(i)

