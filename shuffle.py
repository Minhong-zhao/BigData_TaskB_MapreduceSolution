from collections import defaultdict

def shuffle(mapped_data):
    """
    Shuffle phase: Group mapped key-value pairs by passenger_id.
    :param mapped_data: List of (passenger_id, 1) tuples.
    :return: Dictionary mapping passenger_id to list of values [1, 1, ...].
    """
    shuffled = defaultdict(list)
    for key, value in mapped_data:
        shuffled[key].append(value)
    return shuffled