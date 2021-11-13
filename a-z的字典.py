# a-z: 97-122 | dic.items()
a = dict.fromkeys([chr(x) for x in range(97, 123)], 0)  # a-z: 97-122
count = 0
for key, val in a.items():
    count += 1
    a[key] = count

print(a)