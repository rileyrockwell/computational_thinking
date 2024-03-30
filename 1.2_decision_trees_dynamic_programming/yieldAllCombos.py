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

items = list(range(4))
print(powerSet(items))

x = [0, 1]
for i in powerSet(x):
    print(i)


def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each 
    item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as 
    a list of which item(s) are in each bag.
    
    yields: a generator object?
    """
    


x = [0, 1]
y = [1, 0]
print(yieldAllCombos(x))


print("###")

x = [0, 1]
for i in powerSet(x):
    print(i)