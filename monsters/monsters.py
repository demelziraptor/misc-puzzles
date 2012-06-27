import argparse
from random import randint

"""
Assumptions:
- Two monsters can start in the same place
- If two monsters start in the same place, they destroy (and the town) immediately before any movement
- All monsters move at each iteration
"""

def main():
    """ run main functions to do stuff """
    parse_args()
    init()
    run_iterations()
    print_map()
    

def parse_args():
    """ get cli arguments and add to arg variable """
    parser = argparse.ArgumentParser(description='Monsters, destroying stuff!')
    parser.add_argument('map_file', metavar='M', type=file, help='the map file')
    parser.add_argument('--num', metavar='n', type=int, default=6, help='number of monsters to add to the map (default: 6)', dest='num_monsters')
    
    args = parser.parse_args()
    print args.map_file
    
def init():
    """ read map file, add map and monster dictionaries """
    monsters = {}
    cities = {}
    for line in args.map_file:
        pass
    for num in range(args.num_monsters):
        monsters[num] = randint(0, count(cities))

def run_iterations():
    """ do an iteration until all monsters die or each monster moves 10,000 times """
    pass
    
def print_map():
    """ print out remaining map in correct format """
    for city in city_map:
        #format and print stuff
        pass

if __name__ == "__main__":
    main()
