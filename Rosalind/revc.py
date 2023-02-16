#The example file revcdata.txt is uploaded in the same folder
#I ASSUME upon downloading revc.py and revcdata.txt, that they are put in the same directory
path = "revcdata.txt"
def comp(path):
    seq = []
    with open(path) as file:
        for line in file:
            for i in range(len(line)):
                x = line[i]
                if x == "T":
                    seq.insert(0, "A")
                elif x == "A":
                    seq.insert(0, "T")
                elif x == "C":
                    seq.insert(0, "G")
                elif x == "G":
                    seq.insert(0, "C")
                else:
                    return "Error in sequence at position " + str(i)
    return "".join(seq)
  
print(comp(path))
