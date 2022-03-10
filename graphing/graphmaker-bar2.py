#!/usr/bin/env python3

import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def main():
    N = 3 
    Cats = ('shorthair', 'longhair', 'nohair') # Different types of cats
    Adopted = (13, 25, 4) # Number of adopted cats per type
    ind = np.arange(N) 
    width = 0.40

    pl = plt.bar(ind, Cats, width)
    p2 = plt.bar(ind, Adopted, width, bottom=Cats)

    # Describes the layout of the graph
    plt.ylabel("Number of Adopted Cats")
    plt.title("Cats Adopted 2021")
    plt.xticks(ind, ("Shorthairs", "Longhairs", "NoHairs"))
    plt.yticks(np.arange(13, 25, 4))
    plt.legend((p1[0], p2[0]), ("Cats", "Adopted"))

    plt.savefig("/home/student/mycode/graphing/AdoptedCats2021.png")
    plt.savefig("/home/student/static/AdoptedCats2021.png")

if __name__ == "__main__":
    main()

