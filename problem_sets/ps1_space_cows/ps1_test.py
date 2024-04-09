from ps1 import *

cows = load_cows("/workspaces/computational_thinking/problem_sets/ps1_space_cows/ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))