fname = input("Enter file name: ")
fh = open(fname)

count = 0

for email in fh:
    email = email.rstrip()
    if not email.startswith("From"):
        continue
    email = email.split()
    for mes in email:
        if len(mes) == 1:
            count += 1
            print(email[1])
            
print("There were", count, "lines in the file with From as the first word")
