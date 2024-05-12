###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
filename = '/home/riley/6.0002/problem_sets/1/ps1_cow_data.txt'
#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
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
    # TODO: Your code here
    return_dic = {}

    with open(filename, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        values = line.strip().split(',')
        
        return_dic[values[0]] = int(values[1])
    
    return return_dic


# Problem 2
def non_optimized(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via a brute force method. The non_optimized algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
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
    
        


# Problem 3
def locally_optimal(cows,limit=10):
    """
    Uses a locally_optimal heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The locally_optimal heuristic should follow the following method:

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
    # TODO: Your code here
    pass
    

# Problem 4
def compare_cow_transport_algorithms(cows, limit=10):
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
    a = time.time()
    non_optimized(cows, limit)
    b = time.time()
    c = b - a

    a = time.time()
    locally_optimal(cows, limit)
    b = time.time()
    d = b - a

    # return "time elapsed (non_optimized):", c, "\n", "time elapsed (locally_optimal):", d
    # return "time elapsed 1: \n" + str(round(c, 46)) + "\ntime elapsed 2: \n" + str(round(d, 6))
    return "runtime difference:", round(abs(d - c), 6)



if __name__ == "__main__":
    cows = load_cows(filename)
    print(cows)
    print(locally_optimal(cows, 10))
    print(compare_cow_transport_algorithms(cows))