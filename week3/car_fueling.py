# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    numRefills, currentRefill = 0, 0
    stops = [0] + stops + [distance]
    if tank >= distance:
        return 0
    else:
        while currentRefill < len(stops)-1:
            lastRefill = currentRefill
            while currentRefill < len(stops)-1 and (stops[currentRefill+1] - stops[lastRefill]) <= tank:
                currentRefill += 1
            if currentRefill == lastRefill:
                return -1
            if currentRefill < len(stops)-1:
                numRefills += 1
    return numRefills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
