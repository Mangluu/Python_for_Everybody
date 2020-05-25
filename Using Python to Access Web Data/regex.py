import re

hand = open("regex_sum_554800.txt")
l = []
for line in hand:
    line = line.rstrip()
    l += re.findall('[0-9]+', line)
l = [int(i) for i in l]
print(sum(l))
