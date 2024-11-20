name = input("Enter file:")
handle = open(name)

count = dict()

for time in handle:
    time = time.rstrip()
    if not time.startswith("From"):
        continue
    time = time.split()
    if len(time) > 3:
        tm = time[5][:2]
        count[tm] = count.get(tm, 0) + 1
        
for k, v in sorted(count.items()):      
    print(k,v)
    