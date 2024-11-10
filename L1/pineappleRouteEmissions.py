portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def permutations(route, ports):
    global smallest  # Declare smallest as a global variable
    global bestroute  # Declare bestroute as a global variable

    if len(ports) < 1:
        currentCo2 = 0
        # Calculate emissions for the current route
        for i in range(len(route) - 1):
            currentCo2 += D[route[i]][route[i + 1]] * co2
        # Update global variables if current emissions are lower
        if currentCo2 < smallest:
            bestroute[:] = route  # Update the list in place
            smallest = currentCo2  # Update the smallest value
    else:
        for i in range(len(ports)):
            # Recursive call with the updated route and remaining ports
            permutations(route + [ports[i]], ports[:i] + ports[i + 1:])

def main():

    # Start the recursion
    permutations([0], list(range(1, len(portnames))))

    # Print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

# Example invocation
# Ensure D and co2 are defined before this call
main()
