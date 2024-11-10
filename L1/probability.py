import random

def main():
    catProbability = 0.80
    batProbability = 0.90
    rnd = random.random()

    if rnd < catProbability:
        favourite = "dogs"  # change this
    elif rnd < batProbability:
        favourite = "cats"  # change this
    else:
        favourite = "bats"
    
    print(rnd)
    print("I love " + favourite)

main()
