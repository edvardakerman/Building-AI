import random
import math

def accept_prob(S_old, S_new, T):
    # this is the acceptance "probability" in the greedy hill-climbing method
    # where new solutions are accepted if and only if they are better
    # than the old one.
    # change it to be the acceptance probability in simulated annealing

    if S_new > S_old:
        return 1.0
    else:
        return math.exp((S_new - S_old) / T)

# the above function will be used as follows. this is shown just for
# your information; you don't have to change anything here
def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)
        

# test the above functions with for loop
for T in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
    print("Testing for T = ", T)
    for _ in range(5):
        S_old = random.randint(0, 100)
        S_new = random.randint(0, 100)
        print("S_old = ", S_old, "S_new = ", S_new)
        accept(S_old, S_new, T)
        print()
