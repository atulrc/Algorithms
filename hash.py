inp = [(1,2,3), (2,9,1),(3,5,2),(1,3,4),(8,1,4),(7,2,1)]
out = []
hash_t = []

for i in inp:
    a, b, c = i
    a = int(a)
    b = int(b)
    c = int(c)
    if (a+b+c) not in hash_t:
        out.append(i)
        hash_t.append(a+b+c)

print(inp)
print(out)
print(hash_t)
