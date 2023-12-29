import sys
data = set()
for line in sys.stdin:
    data.add(line[0])
print(sorted(list(data)))

