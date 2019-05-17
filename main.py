from make_coordinates import make_coordinates
from make_distances import make_distances
from build_graph import build_plot

def name():
    pdb_id=input('enter pdb code\n')
    chain = input('enter chain\n')
    return pdb_id, chain

if __name__ == '__main__':
   pdb_id, chain = name()
   coordinates = make_coordinates(pdb_id, chain)
   distances = make_distances(coordinates)
   build_plot(distances)
