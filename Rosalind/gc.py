def GCprocess(dna):
    dnau = dna.upper()
    x = (dnau.count("C")+dnau.count("G"))/(len(dnau))
    return round(100*x, 6)

def wrangle(path):
    keydict = {}
    valdict = {}
    pairdict = {}
    seq = ""
    with open(path) as file:
        for line in file:
            if line.startswith(">"):
                keydict[line[1:].rstrip()] = 0
    with open(path) as file:
        for line in file:
            if not line.startswith(">"):
                seq += line.rstrip()
            elif seq != "":
                valdict[GCprocess(seq)] = 0
                seq = ""
        valdict[GCprocess(seq)] = 0
    for i in range(len(valdict.keys())):
        k = list(keydict.keys())[i]
        v = list(valdict.keys())[i]
        pairdict[k] = v
    return pairdict

def IDprocess(path):
    pairs = wrangle(path)
    val = list(pairs.values())
    mx = max(val)
    id = ""
    for k,v in pairs.items():
        if v == mx:
            id = k
    return id + "\n" + str(mx)

print(IDprocess(path))
