###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport_copilot(cows, limit=10):
    """
    (1). Copilot
    Implements a greedy algorithm to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.

    The greedy algorithm should follow the following method:
    1. Sort the cows in descending order of weight.
    2. Initialize an empty list to store the trips.
    3. While there are still cows remaining:
        - Create a new trip list.
        - Iterate over the sorted cows and add the largest cow that will fit to the trip.
        - Remove the added cow from the remaining cows.
        - If the trip is full or there are no more cows, add the trip to the list of trips.
    4. Return the list of trips.

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    
    (2). OCW
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    sorted_cows = sorted(cows.items(), key=lambda x: x[1], reverse=True)

    trips = []

    while sorted_cows:
        trip = []
        remaining_weight = limit

        for cow, weight in sorted_cows:
            if weight <= remaining_weight:
                trip.append(cow)
                remaining_weight -= weight

        for cow in trip:
            sorted_cows.remove((cow, cows[cow]))

        trips.append(trip)

    return trips


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    return "in progress..."

    def greedy_cow_transport(cows, limit=10):
        """
        Implements a greedy algorithm to determine an allocation of cows that attempts to
        minimize the number of spaceship trips needed to transport all the cows. The
        returned allocation of cows may or may not be optimal.

        The greedy algorithm should follow the following method:
        1. Sort the cows in descending order of weight.
        2. Initialize an empty list to store the trips.
        3. While there are still cows remaining:
            - Create a new trip list.
            - Iterate over the sorted cows and add the largest cow that will fit to the trip.
            - Remove the added cow from the remaining cows.
            - If the trip is full or there are no more cows, add the trip to the list of trips.
        4. Return the list of trips.

        Does not mutate the given dictionary of cows.

        Parameters:
        cows - a dictionary of name (string), weight (int) pairs
        limit - weight limit of the spaceship (an int)

        Returns:
        A list of lists, with each inner list containing the names of cows
        transported on a particular trip and the overall list containing all the
        trips
        """

        sorted_cows = sorted(cows.items(), key=lambda x: x[1], reverse=True)

        trips = []

        while sorted_cows:
            trip = []
            remaining_weight = limit

            for cow, weight in sorted_cows:
                if weight <= remaining_weight:
                    trip.append(cow)
                    remaining_weight -= weight

            for cow in trip:
                sorted_cows.remove((cow, cows[cow]))

            trips.append(trip)

        return trips

def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cow_list = list(cows.keys())
    best_partition = None
    min_trips = float('inf')

    
    partitions = brute_force_partitions(cow_list)

    for partition in partitions:
        valid_partition = True
        for subset in partition:
            subset_weight = sum(cows[item] for item in subset)
            if subset_weight > limit:
                valid_partition = False
                break
        if valid_partition and len(partition) < min_trips:
            min_trips = len(partition)
            best_partition = partition

    return best_partition

def brute_force_partitions_copilot(items):
        """
        Generate all possible partitions of a set of items.

        Parameters:
        items - a list of items

        Returns:
        A list of all possible partitions, where each partition is represented
        as a list of subsets.
        """
        partitions = [[]]
        for item in items:
            new_partitions = []
            for partition in partitions:
                for i in range(len(partition) + 1):
                    new_partition = partition[:i] + [item] + partition[i:]
                    new_partitions.append(new_partition)
            partitions = new_partitions
        return partitions



# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


if __name__ == "__main__":
    cows = load_cows("/Users/riley/github/computational_thinking/problem_sets/ps1_space_cows/ps1_cow_data.txt")

    print(sorted(cows.items(), key = lambda x: x[1], reverse=False))
    print(sorted(cows.items(), key = lambda x: x[1], reverse=True))
    print("limit: 10", greedy_cow_transport_copilot(cows, 10))