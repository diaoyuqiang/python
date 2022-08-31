from basic import all

print("test", id(all))

def test(n):
    for i in range(n):
        if i + 1 == n:
            all.run(i)
            return n
