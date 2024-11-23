import re

hand = open('regex_sum_2122790.txt')
text = hand.read()

regex = re.findall('[0-9]+', text)

total = 0
for num in regex:
    total += int(num)

print(total)