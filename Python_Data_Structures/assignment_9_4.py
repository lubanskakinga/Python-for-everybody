name = input("Enter file:")
handle = open(name)

count = dict()

for email in handle:
    email = email.rstrip()
    if not email.startswith("From"):
        continue
    email = email.split()
    if len(email) < 2:
        continue
    commit = email[1]
    count[commit] = count.get(commit, 0) + 1
if count:
    max_commit = max(count, key=count.get)
    
    print(max_commit, count[max_commit])