def brojevi(n, parni=True):
    for i in range(n):
        if parni and i % 2 == 0:
            yield i
        elif not parni and i % 2 != 0:
            yield i

print(list(brojevi(10, True)))   # parni
print(list(brojevi(10, False)))  # neparni
