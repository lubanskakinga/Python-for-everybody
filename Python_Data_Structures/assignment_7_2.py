# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

s = 0
count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):  
        continue
    fl = float(line[20:])
    s += fl
    count += 1

average = s / count
print("Average spam confidence:", average)