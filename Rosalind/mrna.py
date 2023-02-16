#The example file mrnadata.txt is uploaded in the same folder
#I ASSUME upon downloading mrna.py and mrnadata.txt, that they are put in the same directory

###I put number of possible codons for each a.a. in count dictionary as values for corresponding a.a.
###Then compare every element in peptide input string with keys and append their counts in a list.
###as every amino acid comes from one codon, so it is a combination but (k chooses 1)
###so basically I can just list the (k) possible codons for every element and multiply them

from numpy import prod

path = "mrnadata.txt"

code = {"A": ["GCU","GCC", "GCA","GCG"], "V": ["GUU","GUA","GUC","GUG"], "I": ["AUU", "AUC", "AUA"],"M":["AUG"], "L": ["CUU","CUC", "CUG", "CUA", "UUA","UUG"],"F": ["UUU", "UUC"], "S": ["UCU","UCC","UCA","UCG","AGU","AGC"], "P": ["CCU", "CCC","CCA","CCG"],"T": ["ACU","ACA","ACC","ACG"], "E": ["GAA","GAG"], "D":["GAU", "GAC"], "N":["AAU","AAC"],"K":["AAA","AAG"], "Q":["CAA", "CAG"], "H":["CAU","CAC"], "Y": ["UAU","UAC"], "C": ["UGU","UGC"], "W":["UGG"],"R":["CGA","CGC","CGU","CGG","AGA","AGG"], "G":["GGU","GGC","GGA","GGG"], "STOP":["UGA","UAA","UAG"]}
aa = "ACDEFGHIKLMNPQRSTVWY"

def mrna(path):
    count = {}
    total = []
    final = []
    for key in code:
            count[key] = len(code[key])

    with open(path) as file:
        for line in file:
            for i in line:
                for key in count:
                    if i == key:
                      total.append(count[key])
            final.append(str((prod(total)%1000000)*3))
    return "\n".join(final)

print(mrna(path))

######!!!!!There are 3 stop codons, so any possible outcome can end with either one of them, so the final ountput should be multiplied by 3

