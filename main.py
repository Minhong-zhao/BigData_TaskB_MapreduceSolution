from MultiThread import threaded_map_reduce
from SingleThread import single_threaded_map_reduce

import time

if __name__ == "__main__":
    filename = "data/AComp_Passenger_data_no_error_2.csv"

    # Count the time-consuming of multithreading
    start_multi = time.time()
    top_passengers_multi, max_flights_multi = threaded_map_reduce(filename, num_threads=4)
    end_multi = time.time()

    # Count the time-consuming of singlethreading
    start_single = time.time()
    top_passengers_single, max_flights_single = single_threaded_map_reduce(filename)
    end_single = time.time()

    # Print results
    print("\n--- Multithreaded processing results ---")
    print("Passenger IDs (with the most flights):", top_passengers_multi)
    print("Number of flights:", max_flights_multi)
    print("Timing: {:.4f} seconds".format(end_multi - start_multi))

    print("\n--- Singlethreaded processing results ---")
    print("Passenger IDs (with the most flights):", top_passengers_single)
    print("Number of flights:", max_flights_single)
    print("Timing: {:.4f} seconds".format(end_single - start_single))

    print("\n--- Acceleration ratio ---")
    speedup = (end_single - start_single) / (end_multi - start_multi)
    print("Acceleration ratio (Single-thread time / Multithread time) : {:.2f}x".format(speedup))