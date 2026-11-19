import numpy as np
from random import random

def f(x):
    return (x - 0.3) * (x - 0.3) * (x - 0.3) - 5 * x + x * x - 2

class simulatedAnnealing:
    def __init__(self, min_coord, max_coord, min_temp, max_temp, cooling_rate = 0.02):
        self.min_coord = min_coord
        self.max_coord = max_coord
        self.min_temp = min_temp
        self.max_temp= max_temp
        self.cooling_rate = cooling_rate

        self.actual_state = 0
        self.best_state = 0
        self.next_state = 0

    def run(self):
        temp = self.max_temp
        while temp > self.min_temp:
            new_state = self.generate_next_state()
            actual_energy = self.get_energy(self.actual_state)
            new_energy = self.get_energy(new_state)
            if random() < self.accept_prob(actual_energy, new_energy, temp):
                self.actual_state = new_state
            if f(self.actual_state) > f(self.best_state):
                self.best_state = self.actual_state

            temp = temp * (1 - self.cooling_rate)
        print("global maximum: x=%s f(x)=%s" % (self.best_state, f(self.best_state)))
    
    def generate_next_state(self):
        return self.min_coord + (self.max_coord - self.min_coord) * random()

    @staticmethod
    def accept_prob(actual_energy, next_energy, temp):
        if next_energy > actual_energy:
            return 1

        return np.exp((actual_energy - next_energy) / temp)
    
    @staticmethod
    def get_energy(x):
        return f(x)

if __name__ == "__main__":
    alg = simulatedAnnealing(-2, 2, 1, 100)
    alg.run()