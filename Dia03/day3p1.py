with open("day3aoc.txt") as f:
    file = [el.strip('\n') for el in f.readlines()]
    c = [0] * 12
    for i in range(12):
        c[i] = sum([int(el[i]) for el in file])
    gamma = ''.join([str(int(x >= len(file) / 2)) for x in c])
    epsilon = ''.join([str(int(not(int(y)))) for y in gamma])
    print(f"The power consumption of the submarine is {int(gamma, 2) * int(epsilon, 2)}")
