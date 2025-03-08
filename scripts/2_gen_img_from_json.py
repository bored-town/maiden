from common import *
from 1_gen_json_from_traits import trait_paths

# gen images
chars = [
    (
        trait_paths[0][1].split('*')[0] + a,
        trait_paths[1][1].split('*')[0] + b,
        trait_paths[2][1].split('*')[0] + c,
    ) for (a, b, c) in data
]
save_img(chars, './out/{}.png')
