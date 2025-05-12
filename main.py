from thread import threaded_map_reduce

if __name__ == "__main__":
    filename = "data/AComp_Passenger_data_no_error.csv"
    reduced = threaded_map_reduce(filename, num_threads=4)

    # Find top passengers with maximum flights
    max_flights = max(reduced.values())
    top_passengers = [pid for pid, count in reduced.items() if count == max_flights]
    print("Passenger IDs (with the most flights):", top_passengers)
    print("Number of flights:", max_flights)