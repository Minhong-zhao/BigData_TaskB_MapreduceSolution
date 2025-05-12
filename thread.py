import csv
import threading

from mapper import map_passenger_flights
from shuffle import shuffle
from reducer import reduce_passenger_flights



def threaded_map_reduce(filename, num_threads=2):
    """
    Perform the MapReduce process using multiple threads.

    :param filename: Path to the CSV file containing flight records.
    :param num_threads: Number of threads to use for parallel mapping.
    :return: A tuple containing:
             - List of passenger IDs with the highest number of flights.
             - Maximum number of flights taken.
    """
    with open(filename, 'r', newline='') as file:
        reader = list(csv.reader(file))

    chunk_size = len(reader) // num_threads
    threads = []
    mapped_results = []

    def worker(data_chunk, output_list):
        mapped = map_passenger_flights(data_chunk)
        output_list.extend(mapped)

    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = None if i == num_threads - 1 else (i + 1) * chunk_size
        chunk = reader[start_index:end_index]
        t = threading.Thread(target=worker, args=(chunk, mapped_results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    shuffled = shuffle(mapped_results)
    reduced = reduce_passenger_flights(shuffled)
    return reduced