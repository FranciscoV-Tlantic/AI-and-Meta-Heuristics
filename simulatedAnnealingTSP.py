import numpy as np
from random import random, shuffle
from numpy.random import randint
import matplotlib.pyplot as plt

class City:
    def __init__(self):
        self.x = 1000 * random()
        self.y = 1000 * random()

    def __repr__(self):
        return '(%s, %s)' % (round(self.x, 1), round(self.y, 1))

class SingleTour:
    def __init__(self):
        self.tour = []

    def set_tour(self, tour):
        self.tour.extend(tour)

    def swap(self, index1, index2):
        self.tour[index1], self.tour[index2] = self.tour[index2], self.tour[index1]

    def __repr__(self):
        return ''.join(str(e) for e in self.tour)

    def get_tour_size(self):
        return len(self.tour)

    def generate_tour(self, n):
        for _ in range(n):
            self.tour.append(City())

        shuffle(self.tour)

    @staticmethod
    def distance(city1, city2):
        return np.sqrt((city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2)
    
    def get_distance(self):
        tour_dist = 0
        for i in range(len(self.tour)):
            tour_dist += self.distance(self.tour[i % len(self.tour)], self.tour[(i + 1) % len(self.tour)])

        return tour_dist

class simulatedAnnealing:
    def __init__(self, num_cities, min_temp, max_temp, cooling_rate = 0.001):
        self.num_cities = num_cities
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.cooling_rate = cooling_rate

        self.actual_state = SingleTour()
        self.best_state = None
        self.next_state = None

    def run(self):
        self.actual_state.generate_tour(self.num_cities)
        print(f"Initial (random) dist : {round(self.actual_state.get_distance(), 3)}m")
        self.best_state = self.actual_state
        temp = self.max_temp
        while temp > self.min_temp:
            new_state = self.generate_random_state(self.actual_state)
            actual_energy = self.actual_state.get_distance()
            new_energy = new_state.get_distance()
            if random() < self.accept_prob(actual_energy, new_energy, temp):
                single_tour = SingleTour()
                single_tour.set_tour(new_state.tour)
                self.actual_state = single_tour
            if self.actual_state.get_distance() < self.best_state.get_distance():
                single_tour = SingleTour()
                single_tour.set_tour(self.actual_state.tour)
                self.best_state = single_tour

            temp *= (1 - self.cooling_rate)
        print("solution: %sm" % round(self.best_state.get_distance()))

    @staticmethod
    def generate_random_state(actual_state):
        new_state = SingleTour()
        new_state.set_tour(actual_state.tour)
        new_state.swap(randint(0, new_state.get_tour_size()), randint(0, new_state.get_tour_size()))
        return new_state

    @staticmethod
    def accept_prob(actual_energy, next_energy, temp):
        if next_energy < actual_energy:
            return 1
        return np.exp((actual_energy - next_energy) / temp)
    
    def plot_solution(self):
        xs = []
        ys = []
        self.best_state.tour.append(self.best_state.tour[0])
        for city in self.best_state.tour:
            xs.append(city.x)
            ys.append(city.y)

        plt.scatter(xs, ys)
        plt.plot(xs, ys)
        plt.show()

if __name__ == "__main__":
    alg = simulatedAnnealing(100, 1e-8, 100000)
    alg.run()
    alg.plot_solution()