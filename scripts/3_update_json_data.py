import json

json_path   = '../docs/{}.json'

for token_id in range(1, 10_000+1):
    src = json_path.format(token_id)

    # load json
    data = json.load(open(src))

    # update data
    attr = data['attributes'][1]
    attr['value'] = attr['value'].removesuffix(' Mandala')

    # write file
    print(src)
    with open(src, "w") as f:
        json.dump(data, f)
