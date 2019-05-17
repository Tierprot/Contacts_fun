def make_distances(list):
    res = []
    for el1 in list:
        for el2 in list:
            dist = ((((el1[1])[0]-(el2[1])[0])**2+((el1[1])[1]-(el2[1])[1])**2+((el1[1])[2]-(el2[1])[2])**2)**0.5)
            res.append((el1[0], el2[0], dist))
    return res
