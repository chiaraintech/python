import sys

def generator(n):
    for x in range(n):
        yield x ** 3

values = generator(3000000)
print(sys.getsizeof(values))

#Get the next value but long list whilst doing it
#print(next(values))

