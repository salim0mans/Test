
#First, I deploy the genetic code into a dictionary with values as lists
#then along the string RNA, I move codon by codon.
#For each codon, I run a loop to inspect which is the correct key (a.a.) in the code that contains such codon.

code = {"A": ["GCU","GCC", "GCA","GCG"], "V": ["GUU","GUA","GUC","GUG"], "I": ["AUU", "AUC", "AUA"],"M":["AUG"], "L": ["CUU","CUC", "CUG", "CUA", "UUA","UUG"],"F": ["UUU", "UUC"], "S": ["UCU","UCC","UCA","UCG","AGU","AGC"], "P": ["CCU", "CCC","CCA","CCG"],"T": ["ACU","ACA","ACC","ACG"], "E": ["GAA","GAG"], "D":["GAU", "GAC"], "N":["AAU","AAC"],"K":["AAA","AAG"], "Q":["CAA", "CAG"], "H":["CAU","CAC"], "Y": ["UAU","UAC"], "C": ["UGU","UGC"], "W":["UGG"],"R":["CGA","CGC","CGU","CGG","AGA","AGG"], "G":["GGU","GGC","GGA","GGG"], "STOP":["UGA","UAA","UAG"]}
aa = "ACDEFGHIKLMNPQRSTVWY"

