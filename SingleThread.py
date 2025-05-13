import csv
from mapper import map_passenger_flights
from shuffle import shuffle
from reducer import reduce_passenger_flights

def single_threaded_map_reduce(filename):
    with open(filename, 'r', newline='') as file:
        reader = list(csv.reader(file))

    mapped = map_passenger_flights(reader)
    shuffled = shuffle(mapped)
    reduced = reduce_passenger_flights(shuffled)

    max_flights = max(reduced.values())
    top_passengers = [pid for pid, count in reduced.items() if count == max_flights]

    return top_passengers, max_flights