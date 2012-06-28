import argparse
from random import randint

"""
Assumptions:
- Two monsters can start in the same place
- If two monsters start in the same place, they ignore eachother and start by moving!
- All monsters move at each iteration
- For some reason, the monsters always move in the same order...
- This monster world runs python 2.7
"""

class Main:

    monsters = {}
    cities = {}
    
    def __init__(self):
        self.parse_args
        self.setup_monsters_and_cities
    
    def parse_args(self):
        """ get cli arguments and add to arg variable """
        parser = argparse.ArgumentParser(description='Monsters, destroying stuff!')
        parser.add_argument('map_file', metavar='M', type=file, help='the map file')
        parser.add_argument('--num', metavar='n', type=int, default=6, help='number of monsters to add to the map (default: 6)', dest='num_monsters')
        
        self.args = parser.parse_args()
        print self.args
        
    def setup_monsters_and_cities(self):
        """ read map file, add map and monster dictionaries """
        for line in args.map_file:
            pass
        for num in range(args.num_monsters):
            self.monsters[num] = random.choice(list(self.cities.keys()))

    def run_iterations(self):
        """ do an iteration until all monsters die or each monster moves 10,000 times """
        self._move
        self._destroy
        
    def print_map(self):
        """ print out remaining map in correct format """
        for city in city_map:
            #format and print stuff
            pass
            
    def _move(self):
        for monster, location in self.monsters.iteritems():
            options = self.cities[location]
            direction = random.choice(list(options.keys()))
            new_location = options[direction]
            self.monsters[monster] = new_location
            print "Monster #{n} has moved {d} to {l}".format(n = monster, d = direction, l = new_location)
            
    def _destroy(self):
        pass
            

if __name__ == "__main__":
    main = Main
    main.run_iterations
    main.print_map
