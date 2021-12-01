with open("day1.txt") as f:
    file = f.readlines()
    file = [int(el.strip('\n')) for el in file]

    # DÍA 1 ; PROBLEMA 1
    # Count the number of times a depth measurement increases from the previous measurement

    count1 = sum(map(lambda actual, anterior: actual > anterior, file[1:], file[0:-1]))
    print(count1)

    # DÍA 1 ; PROBLEMA 2
    # Count the number of times the sum of measurements in this sliding window increases from the previous sum

    count2 = sum(
        map(lambda e1, e2, e3, e4: e2 + e3 + e4 > e1 + e2 + e3, file[0:-3], file[1:-2], file[2:-1], file[3:]))
    print(count2)
