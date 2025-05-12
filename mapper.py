def map_passenger_flights(lines):
    """
    Map phase: Convert input lines into (passenger_id, 1) key-value pairs.
    :param lines: List of rows, where each row is a list containing flight information.
    :return: List of tuples (passenger_id, 1).
    """
    mapped = []
    for row in lines:
        passenger_id = row[0]
        mapped.append((passenger_id, 1))
    return mapped