#In this code, I start with a function GCprocess that outputs CG percentage rounded as requested in Rosalind.

def GCprocess(dna):
    dnau = dna.upper()
    x = (dnau.count("C")+dnau.count("G"))/(len(dnau))
    return round(100*x, 6)

#I put the example dataset in gcdata.txt file (uploaded in the same folder with gc.py)
##I ASSUME that if both files (gc.py and gcdata.txt) are downloaded, they are put in the same directory.
#I introduced the wrangle funtion to manipulate the data, no matter how dna string is divided among newlines, as long as the same structure of FASTA is maintained.
#wrangle will ouput a dictionary, whose keys are the IDs and values are the GC percentages.

path = "data.txt"
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

#Finally I processed the last output to show maximum value with corresponding ID, the same way Rosalind Requested.

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
