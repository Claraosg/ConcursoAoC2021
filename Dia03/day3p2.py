with open("day3aoc.txt") as f:
    file = [el.strip('\n') for el in f.readlines()]
    filtrado1 = file
    i = 0
    while len(filtrado1) != 1:
        count = 0
        for el in filtrado1:
            count += int(el[i])
        condicion = int(count >= len(filtrado1) / 2)
        filtrado1 = [x for x in filtrado1 if int(x[i]) == condicion]
        i += 1
    oxigeno = filtrado1[0]
    print(f"oxigeno: {oxigeno}")

    filtrado2 = file
    j = 0
    while len(filtrado2) != 1:
        count = 0
        for el in filtrado2:
            count += int(el[j])
        condicion2 = int(count >= len(filtrado2) / 2)
        filtrado2 = [x for x in filtrado2 if int(x[j]) != condicion2]
        j += 1
    co2 = filtrado2[0]
    print(f"co2: {co2}")
    print(f"Life support rating is: {int(oxigeno,2)*int(co2,2)}")
