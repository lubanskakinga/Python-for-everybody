fname = input("Enter file name: ")
fh = open(fname)

lst = []

for line in fh:
    line = line.strip().split()
    lst.append(line)
    list = [item for sublist in lst for item in sublist]
    
print(sorted(set(list)))