# Szymon B. zadanie rekrutacyjne ImpiCode
import sys

if __name__ == "__main__":

    # Input file parsing
    content = str(sys.stdin.read())
    content.rstrip('\n')
    a_list = content.split()
    map_object = map(int, a_list)
    list_of_ints = list(map_object)

    # Initialization of lists and variables
    number_of_ele = list_of_ints[0]  # Number of elements
    weight = []  # List for a weights of elephants
    original = []  # Original order of elephants
    permutation = [
        0
    ] * number_of_ele  # Elephant [i] is going to be placed on a position of elephant perm[i]
    number = []  # Wanted order of elephants
    vis = [False] * number_of_ele  # Auxiliary variable
    min_w = 1000000000  # Variable for minimal weight storage

    # Processing list_of_ints:
    for i in range(1, len(list_of_ints)):

        # Indexes for original[] are always included in <n+1:2*n> , where n is number_of_ele
        if number_of_ele < i <= 2 * number_of_ele:
            original.append(list_of_ints[i])

        # <2*n+1:3*n> for number[]
        elif i > 2 * number_of_ele:
            number.append(list_of_ints[i])

        # <1:n> for weight[]
        else:
            weight.append(list_of_ints[i])

    for mass in weight:
        min_w = min(min_w, mass)

    for i in range(number_of_ele):
        original[i] -= 1

    for i in range(number_of_ele):
        number[i] -= 1
        permutation[number[i]] = original[i]

    outcome = 0

    for begin in range(number_of_ele):
        if not vis[begin]:
            min_c = 1000000000  # Minimal weight in cycle
            summed = 0  # Sum of the weights in cycle
            cur = begin
            length_of_cycle = 0
            while True:
                min_c = min(min_c, weight[cur])
                summed += weight[cur]
                cur = permutation[cur]
                vis[cur] = True
                length_of_cycle += 1
                if cur == begin:
                    break
            outcome += min(
                summed + (length_of_cycle - 2) * min_c,
                summed + min_c + (length_of_cycle + 1) * min_w,
            )

    print(outcome)
