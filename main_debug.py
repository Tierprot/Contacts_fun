from make_coordinates import make_coordinates_from_text
from make_distances import make_distances
from build_graph import build_plot
import requests


def name():
    pdb_id=input('enter pdb code\n')
    chain = input('enter chain\n')
    return pdb_id, chain

if __name__ == '__main__':
   with open('config.txt') as inp:
       exec(inp.read())
   pdb_id, chain = name()
   #pdb_id = '1A6M'
   #chain = 'A'
   data = requests.get('https://files.rcsb.org/download/{}.pdb'.format(pdb_id))
   coordinates = make_coordinates_from_text(data.text, chain.upper())
   distances = make_distances(coordinates)
   build_plot(distances, pdb_id, min_dist=min_dist, max_dist=max_dist, resolution = resolution)
