#The example file protdata.txt is uploaded in the same folder
#I ASSUME upon downloading prot.py and mrnadata.txt, that they are put in the same directory

path = "protdata.txt"

#First, I deploy the genetic code into a dictionary with values as lists
#then along the string RNA, I move codon by codon.
#For each codon, I run a loop to inspect which is the correct key (a.a.) in the code that contains such codon.
## I put a warning for premature stop codon (nonsense mutation) that will stop all the process until repaired, However, if the user wants just to run the codes ignoring stop codon, They can just put (#) before line (32-34).

code = {"A": ["GCU","GCC", "GCA","GCG"], "V": ["GUU","GUA","GUC","GUG"], "I": ["AUU", "AUC", "AUA"],"M":["AUG"], "L": ["CUU","CUC", "CUG", "CUA", "UUA","UUG"],"F": ["UUU", "UUC"], "S": ["UCU","UCC","UCA","UCG","AGU","AGC"], "P": ["CCU", "CCC","CCA","CCG"],"T": ["ACU","ACA","ACC","ACG"], "E": ["GAA","GAG"], "D":["GAU", "GAC"], "N":["AAU","AAC"],"K":["AAA","AAG"], "Q":["CAA", "CAG"], "H":["CAU","CAC"], "Y": ["UAU","UAC"], "C": ["UGU","UGC"], "W":["UGG"],"R":["CGA","CGC","CGU","CGG","AGA","AGG"], "G":["GGU","GGC","GGA","GGG"], "STOP":["UGA","UAA","UAG"]}
aa = "ACDEFGHIKLMNPQRSTVWY"

def translate(path):
    k = 3
    peptide = []
    final = []
    with open(path) as file:
        for line in file:
            n = len(line.rstrip())
            if n%3 != 0:
                return "Error in length! final codon is not complete, or frame shift happened."
            for i in range(0,n-k+1,k):
                codon = line[i:i+k]
                for x in codon:
                    if not x in "ACGU":
                        return "Error in sequence at position " + str(i)
                for y in range(len(aa)):
                    symbol = aa[y]
                    if codon in code[symbol]:
                        peptide.append(symbol)
                    elif codon in code["STOP"] and i+3 < n:
                            final.append("".join(peptide))
                            return "\n".join(final)+"\n"+"Warning of premature Stop at position: " + str(i)
            final.append("".join(peptide))
            peptide = []
    return "\n".join(final)

print(translate(path))
