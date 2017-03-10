# File: sim_tournament.py
# Author: Siddhartha Nutulapati
#
# Goal: simulate a march madness tournament based solely on the seeding
# of the inital teams, assuming that each team wins with a probability
# proportional to the difference in seeding

import csv
import matplotlib.pyplot as plt

def main():
    # read in file
    f4irl = read_file()
    # init tournament
    # sim tournament
    # plot results
    plot(f4irl, [])
    return 0


def read_file():
    # parse through, find seeds of final four for evey year
    file = open('NCAA Mens March Madness Historical Results.csv')
    array = []
    csv_reader = csv.reader(file)
    line = 0
    for row in csv_reader:  # read in all rows from csv file
        line += 1
        if line == 1:  # ignore first row, that's the column names
            continue  # skip rest of the code for the first row
        if row[1] == 'Elite Eight':
            array.append(int(row[3]))

    return array


def generate_bracket():
    return 0


def sim_tournament():
    # until bracket length == 4, sim games
    return 0


def sim_round():
    return 0


def sim_game(high, low):
    return 0


def plot(irl, sim):
    plt.hist(irl, bins='auto')
    plt.show()
    return 0



main()
