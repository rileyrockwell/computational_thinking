def powerSet(items):
    N = len(items)

    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])

        yield combo

# define a 1-dimensional row vector
x = [0, 1]

# iterate over the generator object to display the results
for i in powerSet(x):
    print(i)


def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each 
    item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as 
    a list of which item(s) are in each bag.
    
    yields: a generator object?

    hint: w/ 2 bags there are 3**N "possible combinations" (subsets)?

    """
    N = len(items)

    # iterate over the total number of subsets in the powerset
    for i in range(3**N):
        bag1 = []
        bag2 = []

        # iterate over the length of items, disregarding the value of each element in items
        for j in range(N):
            # condition for bag1: ...
            if (i // (3**j)) % 3 == 1:
                # explain...
                bag1.append(items[j])
            # condition for bag2: ...
            elif (i // (3**j)) % 3 == 2:
                # explain...
                bag2.append(items[j])
        
        # return the generator object to iterate over (in order to display the output)
        # rather than using a function and having all results stored in memory.
        yield (bag1, bag2)


print("###")        

# define a 1-dimensional row vector
x = [0, 1]

# iterate over the generator object to display the results
for i in yieldAllCombos(x):
    print(i)