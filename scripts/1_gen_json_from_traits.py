from pprint import pprint as pp
import glob, random, json

title       = 'M.Aiden'
desc        = 'An M.Aiden agent from Bored Town, here to illuminate your path on Aiden DeFAI. Discover her unique origin and wisdom.'
gynara      = 'Gynara'
json_path   = '../docs/{}.json'
trait_paths = [
    ( 'Planet',  '../traits/1_Planet/*.jpg' ),
    ( 'Mandala', '../traits/2_Mandala/*.png' ),
    ( 'Agent',   '../traits/3_Agent/*.png' ),
]

# load filenames to chunk
chunk = []
for (name, path) in trait_paths:
    chunk.append([ p.split('/')[-1].split('.')[0] for p in glob.glob(path) ])

# remove Gynara from list
chunk[2].remove(gynara)

# full-scan
fullscan = []
for a in chunk[0]:
    for b in chunk[1]:
        for c in chunk[2]:
            fullscan.append([ a, b, c ])

# random pick 10K
data = random.sample(fullscan, 10_000)

# random inject 3 gynaras
for token_id in [
    random.randint(1,     3_333), # range 1
    random.randint(3_334, 6_666), # range 2
    random.randint(6_667, 10_000) # range 3
]: data[token_id-1][2] = gynara

# gen json
for (idx, row) in enumerate(data):
    token_id = idx + 1
    (planet, mandala, agent) = row
    dest = json_path.format(token_id)

    # craft data
    data = {
        "name": "{} #{}".format(title, token_id),
        "description": desc,
        "image": "*** TODO ***",
        "attributes": [
            {
                "trait_type": "Agent",
                "value": agent,
            },
            {
                "trait_type": "Mandala",
                "value": mandala,
            },
            {
                "trait_type": "Planet",
                "value": planet,
            },
        ],
    }

    # write file
    print(dest)
    #pp(data)
    with open(dest, "w") as f:
        json.dump(data, f)
