import json

json_path = '../docs/{}.json'
ipfs_url  = 'https://bored-town.github.io/maiden-{}/{}.png'

for token_id in range(1, 10_000+1):
    src = json_path.format(token_id)

    # load json
    data = json.load(open(src))

    # update data
    section = (token_id-1) // 500
    new_ipfs = ipfs_url.format(section, token_id)
    data['image'] = new_ipfs

    # write file
    print(src, new_ipfs)
    with open(src, "w") as f:
        json.dump(data, f)
