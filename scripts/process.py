from pprint import pprint as pp
import glob, random
from common import *

trait_paths = [
    ( 'Planet',  '../traits/1_Planet/*.jpg' ),
    ( 'Mandala', '../traits/2_Mandala/*.png' ),
    ( 'Agent',   '../traits/3_Agent/*.png' ),
]

# load filenames to chunk
chunk = []
for (name, path) in trait_paths:
    chunk.append([ p.split('/')[-1] for p in glob.glob(path) ])

# remove Gynara from list
chunk[2].remove('Gynara.png')

# full-scan
fullscan = []
for a in chunk[0]:
    for b in chunk[1]:
        for c in chunk[2]:
            fullscan.append((a, b, c))

# random pick 10K
data = random.sample(fullscan, 10_000)

# random inject gynara 3 times

# gen json, image
"""
chars = [
    (
        trait_paths[0][1].split('*')[0] + a,
        trait_paths[1][1].split('*')[0] + b,
        trait_paths[2][1].split('*')[0] + c,
    ) for (a, b, c) in data
]
save_img(chars, './out/{}.png')
"""
