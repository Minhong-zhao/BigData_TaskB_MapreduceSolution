from thread import threaded_map_reduce

if __name__ == "__main__":
    filename = "AComp_Passenger_data_no_error.csv"
    reduced = threaded_map_reduce(filename, num_threads=4)