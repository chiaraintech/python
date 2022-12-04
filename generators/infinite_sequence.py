def infinite():
    result = 1
    while True:
        yield result
        result += 5

values = infinite()

for x in range(500):
    print(next(values))