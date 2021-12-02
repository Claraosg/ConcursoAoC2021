with open("day2.txt") as f:
    file = [el.strip('\n') for el in f.readlines()]
    depth_p2 = 0

    # PROBLEMAS 1 Y 2 DÍA 2

    coord_dict = {'f': 0, 'd': 0, 'u': 0}

    for coord in file:
        coord_dict[coord[0]] += int(coord[-1])
        if coord[0] == 'f':
            depth_p2 += ((coord_dict['d'] - coord_dict['u'])*int(coord[-1]))

    #coord_dict['f'] -> horizontal position
    #coord_dict['d'] - coord_dict['u'] -> depth para el problema 1
    #la depth en el problema 2 se calcula distinto -> aim * X

    print(coord_dict['f'] * (coord_dict['d'] - coord_dict['u'])) #SOLUCIÓN 1
    print(coord_dict['f'] * depth_p2) #SOLUCIÓN 2






