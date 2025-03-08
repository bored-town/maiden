from pprint import pprint as pp
from common import *
import json

chars     = []
json_path = '../docs/{}.json'
out_path  = './out/{}.png'

# craft chars from json
for token_id in range(1, 10_000+1):
    src = json_path.format(token_id)
    data = json.load(open(src))
    (_agent, _mandala, _planet) = data['attributes']
    chars.append((
        '../traits/1_Planet/{}.jpg'.format(_planet['value']),
        '../traits/2_Mandala/{}.png'.format(_mandala['value']),
        '../traits/3_Agent/{}.png'.format(_agent['value']),
    ))

# render images
save_img(chars, out_path)
