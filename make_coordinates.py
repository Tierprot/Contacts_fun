def make_coordinates(file, chain):
    coords = []
    with open(file, 'r') as pdb:
        for line in pdb:
            if 'ATOM' in line and 'CA' in line and line.split()[4]==chain:
                line = line.split()
                for n in line:
                    n = int(line[5])
                for numbers in line:
                    numbers = []
                for x in line:
                    x = float(line[6])
                for y in line:
                    y = float(line[7])
                for z in line:
                    z = float(line[8])
                    numbers = [x, y, z]
                combo = n, numbers
                coords.append(combo)
    return coords

def make_coordinates_from_text(data, chain):
    coords = []
    data = data.split('\n')
    for line in data:
            if 'ATOM' in line and 'CA' in line and line.split()[4]==chain:
                line = line.split()
                for n in line:
                    n = int(line[5])
                for numbers in line:
                    numbers = []
                for x in line:
                    x = float(line[6])
                for y in line:
                    y = float(line[7])
                for z in line:
                    z = float(line[8])
                    numbers = [x, y, z]
                combo = n, numbers
                coords.append(combo)
    return coords

