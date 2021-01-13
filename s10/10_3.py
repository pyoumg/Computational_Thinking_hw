words = [
    "courtyard",
    "alley",
    "landlady",
    "landlord",
    "tenant",
    "stairs",
    "fire escape",
    "trash bin",
    "hallway",
    "balcony",
    "doorknob",
    "peephole",
    "elevator",
    "lobby",
    "door chain",
    "realtor",
]


di = {}
for item in words:
    le = len(item)
    if di.get(le) is None:
        di[le] = [item]
    else:
        di[le].append(item)


for item in di.keys():
    print("[{}] words of length {} ->".format(len(di[item]), item), di[item])
