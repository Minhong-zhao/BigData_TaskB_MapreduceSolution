def reduce_passenger_flights(shuffled_data):
    """
    Reduce phase: Aggregate the number of flights per passenger.
    :param shuffled_data: Dictionary where key is passenger_id and value is list of flight counts.
    :return: Dictionary mapping passenger_id to total number of flights.
    """
    reduced = {}
    for key, values in shuffled_data.items():
        reduced[key] = sum(values)
    return reduced