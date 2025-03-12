import json

src_path = '../docs/{}.json'
desc_path = '../docs/v2/{}'

for new_id in range(0, 10_000):
    src = src_path.format(new_id+1)
    dest = desc_path.format(new_id)

    # load json
    data = json.load(open(src))

    # update data
    data['name'] = "M.Aiden #{}".format(new_id)

    # write file
    print(dest)
    with open(dest, "w") as f:
        json.dump(data, f)
