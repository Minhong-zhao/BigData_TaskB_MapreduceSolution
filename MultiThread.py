import csv
import threading

from mapper import map_passenger_flights
from shuffle import shuffle
from reducer import reduce_passenger_flights



def threaded_map_reduce(filename, num_threads=2):
    """
    Perform the MapReduce process using multiple threads.

    :param filename: Path to CSV file containing flight records
    :param num_threads: Number of threads for parallel map processing
    :return: Tuple (top_passengers, max_flights) where:
             - top_passengers: List of passenger IDs with maximum flights
             - max_flights: Integer count of maximum flights taken
    """
    # Read input data from CSV file
    with open(filename, 'r', newline='') as file:
        reader = list(csv.reader(file))

    # Split data into chunks for parallel processing
    chunk_size = len(reader) // num_threads
    threads = []
    mapped_results = []

    def worker(data_chunk, output_list):
        """Thread worker function to perform map operation on a data chunk"""
        mapped = map_passenger_flights(data_chunk)
        output_list.extend(mapped)

    # Start threads for parallel map processing
    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = None if i == num_threads - 1 else (i + 1) * chunk_size
        chunk = reader[start_index:end_index]
        t = threading.Thread(target=worker, args=(chunk, mapped_results))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    # Perform shuffle and reduce operations
    shuffled = shuffle(mapped_results)
    reduced = reduce_passenger_flights(shuffled)

    # Find top passengers with maximum flights
    max_flights = max(reduced.values())
    top_passengers = [pid for pid, count in reduced.items() if count == max_flights]

    return top_passengers, max_flights