import json

json_path = '../docs/{}.json'
ipfs_url  = 'https://some-ipfs.com/maiden/{}.png' # TODO

for token_id in range(1, 10_000+1):
    src = json_path.format(token_id)

    # load json
    data = json.load(open(src))

    # update data
    new_ipfs = ipfs_url.format(token_id)
    print(token_id, data['image'], new_ipfs)

    """
    # write file
    print(src)
    with open(src, "w") as f:
        json.dump(data, f)
    """
